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
        html.H1("Insights"),
        html.Div([
            "While investigating the dataset the incredibly high Nan count in some of the columns cut down the data from about ~16k observations down to ~6k, but I seem to still have enough data to work with and it's better than working with a massive amount of imputed data."          
       ]),
        html.Br(),
        html.Img(src='assets/High_Missing.png'),
        html.Br(),
        html.Br(),
        html.Div([
        "Looking at the permutation importances of my best model, I find it interesting that Platform, Above_Average_Critic_Score and Publisher had the most impact for predicting game sales and thinking that games would be able to get more sales from one of the publishing giants the more recent the game is."
        ]),
        html.Br(),
        html.Img(src='assets/Importance.png'),
        html.Br(),
        html.Div([
        "Unfortuanly the model isn't as useful as I had hoped probably requiring more data and features to be more useful or be able to be able to predict more accuratly. If it went as I'd hoped, it could've been able to predict the sales of games that are not released yet or are just released"
        ]),
    ],
)

layout = dbc.Row([column1])