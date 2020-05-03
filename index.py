import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output, State
from sklearn.externals import joblib
from datetime import datetime
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import xgboost as xgb
from datetime import datetime as dt


from app import app, server
from tabs import intro, predict, explain

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Permafrost Thawing Rate Prediction'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'),
        dcc.Tab(label='Predict', value='tab-predict'),
        dcc.Tab(label='Explain', value='tab-explain'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
              
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    

if __name__ == '__main__':
    model = joblib.load("/Users/arunputcha/Documents/GitHub/datax/code/joblib_xgboost_reg_1.pkl")
    app.run_server(debug=True)