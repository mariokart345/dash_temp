# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.H3("Can we be able to predict how much a videogame will make globally?"),
        html.Br(),
        dcc.Link(dbc.Button('How I attempted it', color='primary'), href='/process'),
        html.Br(),
        dcc.Link(dbc.Button('Make a prediction', color='secondary'),href='/predictions')
    ],
    md=5,
)

basey = pd.read_csv('assets/graph.csv')

fig = px.histogram(basey)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])