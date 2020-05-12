import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output, State
from sklearn.externals import joblib
from datetime import datetime
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import xgboost as xgb
from datetime import datetime as dt

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]


app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.title = "Data-X: Environment-B Permafrost"
app.config.suppress_callback_exceptions = True
server = app.server

