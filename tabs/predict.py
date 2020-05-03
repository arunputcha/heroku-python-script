import pandas as pd
import numpy as np
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


from joblib import load
from app import app

style = {'padding': '1.5em'}

def find_month(user_input):
    """Returns all months between June and August between our last observed date up to the user input date"""
    dt = datetime.strptime(user_input, '%Y-%m-%d')
    dt2 = pd.to_datetime(lv1_df.index[-1])
    num_years = dt.year - dt2.year
    
    index = pd.date_range(lv1_df.index[-1], user_input, num_years*25).to_series()
    month = index[(index.dt.month == 6) | (index.dt.month == 7) | (index.dt.month == 8) | (index.dt.month == 9)]
    
    return(month)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#training_data = joblib.load("../code/X_train.pkl")
#training_labels = joblib.load("../code/y_train.pkl")

layout = html.Div(children=[
    dcc.Markdown("""
        ### Predict
        Enter a Date below to predict the Active Layer Thickness (ALT) for Samoylov Site in Russia.\n
        **Note:** *As Active Layer Thickness is measured sporadically during June-September each year, 
                our model will only predict ALT within those 4 months. You may enter dates between
                2018 to 2050.*
        """),

                    #html.Div(style={'backgroundColor': 'black'},
                      #          children=[
                       #         html.H1('Permafrost Thawing Rate', style = {'textAlign': 'center', 
                        #                                                    'color' : colors['text'] })]),
    
    
                        html.Div(children=[html.Label("Enter Date:"),
                        dcc.DatePickerSingle(id = 'user_input',
                                             min_date_allowed = dt(2018,1,1),
                                             max_date_allowed = dt(2050,1,1),
                                             date = dt.today().date(), clearable = False),
                        html.Div(id = 'result')],
              style={'textAlign': 'center', 'color' : colors['text'], 'font-size':'20px'}),
              
              html.Div(id = "prediction-output_1", style = {'fontweight':'bold', 'font-size':'26px'}),
              
              html.Div(id = "prediction-output_2", style = {'fontweight':'bold', 'font-size':'26px'}),
              
    
              dcc.Graph('fig', config = {'displayModeBar': False}, style = {'height': '550px'})])



@app.callback(
    [Output(component_id= 'fig', component_property='figure'),
     Output('prediction-output_1','children'), Output('prediction-output_2','children')],
    [Input(component_id='user_input', component_property='date')])


def find_output(user_input):
    
    """uses find_month to get dates between June and Sepetember and 
    forecasts the active layer thickness in cm"""
    
    month = pd.DataFrame(find_month(user_input)).reset_index(drop = True).rename({0:'Date'}, axis = 1)
    month['Month'] = month['Date'].dt.month
    month['Year'] = month['Date'].dt.year
    month['dayofweek'] = month['Date'].dt.dayofweek
    month = month.set_index('Date')
    
    
    model = joblib.load("/Users/arunputcha/Documents/GitHub/datax/code/joblib_xgboost_reg_1.pkl")
    pred = model.predict(month)
    predf = pd.DataFrame({'pred': pred})
    
    predf['Date'] = month.index
    predf = predf.set_index('Date')
    
    alt = round(predf.iloc[-1,:].pred,2)
    
    result_1 = f'Date: {str(predf.index[-1])[0:10]}'
    result_2 = f'Active Layer Thickness: {alt}'
   
    #predf['Date'] = month.index
    #predf = predf.set_index('Date')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x =X_test.index, y = y_test, name = 'Observed'))
    fig.add_trace(go.Scatter(x = month.index, y = predf['pred'], name = 'Forecast'))
    fig.update_layout(title = {
                            
                            'text' : "Forecasted Active Layer Thickness(cm)",
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
    }, xaxis_title = "Year", yaxis_title = "Active Layer Thickness(cm)")
    
    return fig, result_1, result_2




lv1_df = pd.read_csv('/Users/arunputcha/Documents/GitHub/datax/data/Final_data/samoylov_final')
lv1_df = lv1_df.rename(columns = {'UTC': 'Date', 'Dal_01_01': 'Alt_in_cm'})
lv1_df['Date'] = pd.to_datetime(lv1_df['Date'])
lv1_df['Month'] = lv1_df.Date.dt.month
lv1_df['Year'] = lv1_df.Date.dt.year
lv1_df['dayofweek'] = lv1_df['Date'].dt.dayofweek
lv1_df = lv1_df.set_index('Date')

### interpolation ###
lv1 = lv1_df.copy()

idx = pd.date_range(min(lv1_df.index), max(lv1_df.index))
lv1 = lv1.reindex(idx)
#df = df.fillna(x.interpolate(method = 'time'))
#df = melted.assign(RollingMean=df1.Alt_in_cm.fillna(data.Alt_in_cm.rolling(24, min_periods=1,).mean()))
lv1 = lv1.interpolate(method='time')[['Alt_in_cm']]
########

lv1_train = lv1_df.iloc[:100]
lv1_test = lv1_df.iloc[101:]

X_train = lv1_train.drop('Alt_in_cm', axis = 1)
y_train = lv1_train['Alt_in_cm']
X_test = lv1_test.drop('Alt_in_cm', axis = 1)
y_test = lv1_test['Alt_in_cm']


