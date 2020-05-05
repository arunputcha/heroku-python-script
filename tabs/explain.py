from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app


layout = [dcc.Markdown("""

### Project context and model selection

This project is created as an assignment for the Data-x course in UC Berkeley. We splitted the data into train and 
test set, and experimented with different models before choosing one with the lowest loss. The table below shows the 
different models that we tried and their corresponding train and test Root Mean Squared Error (RMSE).

As seen, the XGBoost model has the lowest train and test RMSE and therefore is used as the chosen model to forecast,
active layer thickness in the Samoylov region in Russia.


|         Model         | Train RMSE | Test RMSE |
|-----------------------|------------|-----------|
|  Autoregression (p=31)|   10.637   |   13.690  |
|   ARIMA (p=2, q=0)    |   11.601   |   13.716  |
|         SARIMA        |   15.415   |   14.436  |
|     Random Forest     |   5.651    |   8.998   |
|        XGBoost        |   2.194    |   7.342   |

"""),
    


html.Div(children= [dcc.Markdown("**Image of the XGBoost model performance against the test data,**"),

html.Img(src='https://github.com/yangluanne/datax/blob/master/Webapp/xgboost%20model%20against%20test%20data.png', style = {'width':'50%', 'height':'50%'}),
    dcc.Markdown("*XGBoost performance against test data (Date on the x-axis, ALT in centimeters on the y-axis)*")],
    style = {'textAlign':'center'})

]


