from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app


layout = [dcc.Markdown("""

### Project context and model selection

This project is created as an assignment for the Data-x course in UC Berkeley. We splitted the data into train and 
test set, and experimented with different models before choosing one with the lowest loss. The table below shows the 
different models that we tried and their corresponding train and test Root Mean Squared Error (RMSE).


|         Model         | Train RMSE | Test RMSE |
|-----------------------|------------|-----------|
|  Autoregression (p=31)|   10.637   |   13.690  |
|   ARIMA (p=2, q=0)    |   11.601   |   13.716  |
|         SARIMA        |   15.415   |   14.436  |
|     Random Forest     |   5.651    |   8.998   |
|        XGBoost        |   2.194    |   7.342   |

As seen, the XGBoost model has the lowest train and test RMSE and therefore is used as the chosen model to forecast,
active layer thickness in the Samoylov region in Russia.


"""),
    


dcc.Markdown("""


**Image of the XGBoost model performance against the test data,**"""),


html.Div(children= [

html.Img(src='https://raw.githubusercontent.com/yangluanne/datax-Enviroment-B/master/Webapp/xgboost%20model%20against%20test%20data.png?token=ANXZA3YQPFT4GLQE6UAATZ26XLYK2', style = {'width':'100%', 'height':'100%'}),
    dcc.Markdown("*XGBoost performance against test data (Date on the x-axis, ALT in centimeters on the y-axis)*")],
    style = {'textAlign':'left'})

]


