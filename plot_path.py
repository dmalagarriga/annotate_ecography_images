import numpy as np
from skimage import io
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import dash_html_components as html
#from dash_canvas import DashCanvas
#from dash_canvas.utils import array_to_data_url, parse_jsonstring
import base64
import json
import matplotlib.patches as patches
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#from svg.path import parse_path
from svgpath2mpl import parse_path
import plotly.express as px
from skimage import io


with open ("results_annotation/BPD/data_BPD_tst_0.json",'r') as read_file:
    data = json.load(read_file)
filename = "images/BPD/BPD_tst_0.jpg"
img = mpimg.imread(filename)



def parse_path_data(path_data):
    digit_exp = '0123456789eE'
    comma_wsp = ', \t\n\r\f\v'
    drawto_command = 'MmZzLlHhVvCcSsQqTtAa'
    sign = '+-'
    exponent = 'eE'
    float = False
    entity = ''
    for char in path_data:
        if char in digit_exp:
            entity += char
        elif char in comma_wsp and entity:
            yield entity
            float = False
            entity = ''
        elif char in drawto_command:
            if entity:
                yield entity
                float = False
                entity = ''
            yield char
        elif char == '.':
            if float:
                yield entity
                entity = '.'
            else:
                entity += '.'
                float = True
        elif char in sign:
            if entity and entity[-1] not in exponent:
                yield entity
                float = False
                entity = char
            else:
                entity += char
    if entity:
        yield entity

path2 = parse_path(data[0]["path"])
print(path2)
print(data[0]["path"])

'''patch = patches.PathPatch(path2,facecolor='None',edgecolor='red',alpha=1.0,lw=3)
fig, ax = plt.subplots()
ax.imshow(img)
patch.set_transform(ax.transData)
ax.add_patch(patch)
ax.set_xlim([0,  300])
ax.set_ylim([300, 0])

plt.show()'''

import numpy as np
import plotly.graph_objects as go

fig = go.Figure()
fig = px.imshow(io.imread(filename), binary_backend="jpg")

fig.update_layout(width =600, height=600,
           xaxis_range=[0, 300], 
           yaxis_range=[300, 0],       
    shapes=[
           dict(type="path",
           path= data[0]["path"],
           line_color="RoyalBlue"),
           dict(type="path",
                path = data[0]["path"],
                fillcolor=None,
                line_color="red")
        ]
        )#;
fig.show()
''''''