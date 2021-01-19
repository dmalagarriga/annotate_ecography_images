import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import BPD, CLR , NT


button_howto = dbc.Button(
    "View Code on github",
    outline=True,
    color="primary",
    href="https://github.com/dmalagarriga/annotate_ecography_images",
    id="gh-link",
    style={"text-transform": "none"},
)
button_CLR = dbc.Button(
    "Annotate CLR",
    outline=True,
    color="light",
    href="/apps/CLR",
    #id="gh-link",
    style={"text-transform": "none"},
)
button_NT = dbc.Button(
    "Annotate NT",
    outline=True,
    color="light",
    href="/apps/NT",
    #id="gh-link",
    style={"text-transform": "none"},
)
button_BPD = dbc.Button(
    "Annotate BPD",
    outline=True,
    color="light",
    href="/apps/BPD",
    #id="gh-link",
    style={"text-transform": "none"},
)
# Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            html.Img(
                                #src=app.get_asset_url("/assets/Plotly_Dash_logo.png"),
                                src=("/assets/plotly-logomark.png"),
                                height="30px",
                            ),
                            href="https://plot.ly",
                        )
                    ),
                    dbc.Col(
                        dcc.Link(

                        dbc.NavbarBrand("Image Annotation App"), href="/"
                        )
                    
                    ),
                ],
                align="center",
            ),
            dbc.Row(
                    dbc.Col(
                    [
                        dbc.NavbarToggler(id="app-0-navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [dbc.NavItem(button_BPD),dbc.NavItem(button_CLR),dbc.NavItem(button_NT)],
                                className="ml-auto",
                                navbar=True,
                            ),
                            id="app-0-navbar-collapse",
                            navbar=True,
                        ),
                        #modal_overlay,
                    ]
                ),

            ),
            dbc.Row(
                dbc.Col(
                    [
                        dbc.NavbarToggler(id="app-1-navbar-toggler"),
                        dbc.Collapse(
                            dbc.Nav(
                                [dbc.NavItem(button_howto)],
                                className="ml-auto",
                                navbar=True,
                            ),
                            id="app-1-navbar-collapse",
                            navbar=True,
                        ),
                        #modal_overlay,
                    ]
                ),
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
    className="mb-5",
)
index_page = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Image annotation app"),
                width={"size": 6, "offset": 5},
            )
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                            html.H2(dcc.Link('Annotate BPD', href='/apps/BPD')),
                            html.Br(),
                            html.A(
                            html.Img(
                                #src=app.get_asset_url("/assets/Plotly_Dash_logo.png"),
                                src=("/assets/BPD_tst_1.png"),
                                height="200px",
                            ),
                            href="/apps/BPD",
                        ),
                
                ]),
                    width={"size": 3, "order": 1, "offset": 2.0},
                ),
                dbc.Col(
                    html.Div([
                            html.H2(dcc.Link('Annotate CLR', href='/apps/CLR')),
                            html.Br(),
                            html.A(
                            html.Img(
                                #src=app.get_asset_url("/assets/Plotly_Dash_logo.png"),
                                src=("/assets/CLR_tst_1.png"),
                                height="200px",
                            ),
                            href="/apps/BPD",
                        ),
                
                ]),
                    width={"size": 3, "order": 2, "offset": 0},
                ),
                dbc.Col(
                    html.Div([
                            html.H2(dcc.Link('Annotate NT', href='/apps/NT')),
                            html.Br(),
                            html.A(
                            html.Img(
                                #src=app.get_asset_url("/assets/Plotly_Dash_logo.png"),
                                src=("/assets/NT_tst_1.png"),
                                height="200px",
                            ),
                            href="/apps/NT",
                        ),
                
                ]),
                    width={"size": 3, "order": 2,"offset": 0},
                ),
            ]
        ),
                
])

app.layout = html.Div([
    navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/BPD':
        return BPD.layout
    elif pathname == '/apps/CLR':
        return CLR.layout
    elif pathname == '/apps/NT':
        return NT.layout
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True)