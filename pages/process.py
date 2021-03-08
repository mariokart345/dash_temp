# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.H3("Process"),
        html.Div([
            html.H4("Cleaning the data"),
            html.P("I start by using pandas profiling to quickly explore the data and get an idea of each of the columns and start looking for a column to be my target for my model. There were a few problems with this dataset, one of them being that a few of columns had only half of the observations in them(Which I ended up dropping to make my models more accurate), making imputing going to be a problem down the line later and other columns have really high cardinality(one of them have ~11k unique observations!). Using the insight from the profile report, I determined the columns to drop would be the Critic and User scores and amount, Rating and Developer. Lastly I converted the years they are released into pandas datetime so I can use it to split the data later"),
            html.P("After finding my target, I looked at the distribution of my target. It is heavily skewed to the right, so I look the logrithmic of it. Then I filtered out the upper and lower 0.05% of the dataset out to try to further center the distribution.(Which doesnt really center it but more scale it)")
        ]),
        html.Img(src='assets/RightSkewed.png'),
        html.Img(src='assets/NotSoSkewed.png'),
        html.Div([
            html.P("After failing to correct the skew it was time to see if I could build any features that could possibly releate to how much a game could sell, such as if the critic and user score of the game is above average(which is above 75/100 and 7.5/10 respectivly)."),
            html.H4("Modeling"),
            html.P("Next is preparing to train a model, first on my list is how to split the dataset into training, validation and test sets. Since I have already converted the year of release column, I can try splitting it using the year. After some fiddling around with how much data is going to be in each data subset. I chose everything before 2009(~4k observations) for training, 2009-2013(~2k observations) for validation and after 2013(~1k observations) for testing. Now its time to train the regression model. While I'm doing that, I think about the scoring metics I'll be using, which will be R^2 for measuring the fitment of my model and MAE for observing the error between the baseline and my model(When mentioning the MAE, they will be exponentially multiplied to undo the log)."),
            html.Img(src='assets/MAE.png'),
            html.P("Before making a linear regression model, I made the baseline and it had a MAE of ~1.355(in millions)."),
            html.P("My regression model had an MAE of ~1.263(in millions) and an R^2 score of ~0.351"),
            html.P("Using Random Forest Regressor with hyperparameter tuning I managed to get the MAE down to ~1.041(in millions). Trying Decision Tree Regressor before deciding on my final model, it lowered the MAE even further to ~0.887(in millions) making it my final and best model. So then I used my test set wtih the Random Forest Regressor and got an MAE of ~0.218(in millions)"),
            
        ]),
        

    ],
)

layout = dbc.Row([column1])