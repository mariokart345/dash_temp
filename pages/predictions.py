# Imports from 3rd party libraries
import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import category_encoders as ce
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.H1("Predictions"),
        html.Div([
            html.H5("Publisher"),
            dcc.Dropdown(id='publisher',options=[
                {'label':'Nintendo','value':'Nintendo'},
                {'label':'Electronic Arts','value':'Electronic Arts'},
                {'label':'Activision','value':'Activision'},
                {'label':'Sony Computer Entertainment','value':'Sony Computer Entertainment'},
                {'label':'Ubisoft','value':'Ubisoft'},
                {'label':'Sega','value':'Sega'},
                {'label':'Square Enix','value':'Square Enix'},
                {'label':'Capcom','value':'Capcom'},
                {'label':'Namco','value':'Namco Bandai Games'},
                {'label':'Take-Two Interactive','value':'Take-Two Interactive'},
                {'label':'Bethesda Softworks','value':'Bethesda Softworks'},
                {'label':'id Software','value':'id Software'},
                {'label':'LucasArts','value':'LucasArts'},
                {'label':'Paradox Interactive','value':'Paradox Interactive'},
                {'label':'Idea Factory','value':'Idea Factory'},
                {'label':'PQube','value':'PQube'},
                {'label':'THQ','value':'THQ'},
                {'label':'Konami Digital Entertainment','value':'Konami Digital Entertainment'},
                {'label':'Spike','value':'Spike'},
                {'label':'Hasbro Interactive','value':'Hasbro Interactive'},
                {'label':'Disney Interactive Studios','value':'Disney Interactive Studios'}],value='Activision'),
            html.Br(),
            html.H5("Genre"),
            dcc.Dropdown(id='genre',options=[
                {'label':'Simulation','value':'Simulation'},
                {'label':'Shooter','value':'Shooter'},
                {'label':'Fighting','value':'Fighting'},
                {'label':'Role-Playing','value':'Role-Playing'},
                {'label':'Puzzle','value':'Puzzle'},
                {'label':'Action','value':'Action'},
                {'label':'Platform','value':'Platform'},
                {'label':'Strategy','value':'Strategy'},
                {'label':'Sports','value':'Sports'},
                {'label':'Adventure','value':'Adventure'},
                {'label':'Racing','value':'Racing'},
                {'label':'Misc','value':'Misc'},
            ],value='Shooter'),
            html.Br(),
            html.H5("Platform"),
            dcc.Dropdown(id='platform',options=[
                {'label':'PC','value':'PC'},
                {'label':'PS','value':'PS'},
                {'label':'PS2','value':'PS2'},
                {'label':'PS3','value':'PS3'},
                {'label':'PSP','value':'PSP'},
                {'label':'Xbox','value':'XB'},
                {'label':'Xbox 360','value':'X360'},
                {'label':'Dreamcast','value':'DC'},
                {'label':'Gamecube','value':'GC'},
                {'label':'GameBoy Advanced','value':'GBA'},
                {'label':'Nintendo DS','value':'DS'},
                {'label':'Wii','value':'Wii'},
            ],value='X360'),
            html.Br(),
            html.H5("Has a good critic score?"),
            dcc.Dropdown(id='critic',options=[
            {'label':'Yes','value':'1'},
            {'label':'No','value':'0'},
            ],value='1'),
            html.Br(),
                 ]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.P(["For the publisher dropdown menu, It would take way too long to incorperate all ~600 unique publishers present in the data so only 20 were provided"],),
        
        
     ],)

column2 = dbc.Col(
    [
        html.H4("How much your game is predicted to make:"),
        html.Br(),
        html.H5(id='prediction')
    ],
)

layout = dbc.Row([column1,column2])

@app.callback(Output('prediction', 'children'),
              [Input('publisher', 'value'),Input('genre','value'),Input('platform','value'),Input('critic','value')])

def predict(publisher,genre,platform,critic):
    data = {'Publisher': [publisher], 'Genre': [genre], 'Platform': [platform],'Year_of_Release': [2020],'Above_Average_Critic_Score': [critic],'Above_Average_User_Score': [1]}
    X = pd.DataFrame(data=data)
    prediction = regress.predict(X)
    prediction = np.exp(prediction[0])
    return '${} million'.format(prediction)

base = pd.read_csv('assets/trainingdata.csv')
basey = base['Log_Global_Sales']
baseX = base.drop('Log_Global_Sales',axis=1)
regress = make_pipeline(ce.OrdinalEncoder(),SimpleImputer(strategy='mean'),DecisionTreeRegressor(max_depth=7,criterion='mae'))
regress.fit(baseX,basey)