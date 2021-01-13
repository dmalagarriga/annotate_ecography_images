import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import BPD, CLR , NT


index_page = html.Div([
    dcc.Link('Annotate BPD', href='/apps/BPD'),
    html.Br(),
    dcc.Link('Annotate CLR', href='/apps/CLR'),
    html.Br(),
    dcc.Link('Annotate NT', href='/apps/NT'),
])

app.layout = html.Div([
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