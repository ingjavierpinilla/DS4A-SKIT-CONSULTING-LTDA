

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import json

import pandas as pd
import plotly.express as px
import plotly 
import plotly.graph_objs as go 
from datetime import datetime, timedelta
import warnings
from data import new_variables, original

from sqlalchemy import create_engine

from app import app

#Load datasets DataBase
#engine = create_engine("postgresql+psycopg2://postgres:7$col&ds0@ds4a-70-db.cgxzuy7k08ix.us-east-2.rds.amazonaws.com/")
#original = pd.read_sql_table('skit_final',engine)
#new_variables = pd.read_sql_table('new_variables',engine)

#get projects from db
def get_proy(proyectos):
    r = []
    for p in proyectos:
        r. append({"label": p, "value": p})
    return r
    

#Values in Cards
var_poy = original["proyecto"].nunique()
var_avg_cli = round(original.groupby(original["proyecto"]).count()["nombre cliente"].mean())
var_avg_pro = round(original[["proyecto", "horas"]].groupby(original["proyecto"]).sum().mean())[0]
var_avg_act = round(pd.DataFrame((original[["proyecto", "actividad"]].drop_duplicates())["proyecto"].value_counts()).reset_index()["proyecto"].mean(),0)

#Graph pie
def get_clients_proyects():
	aux = original[["nombre cliente", "proyecto"]].drop_duplicates().groupby('nombre cliente').count().reset_index()
	aux = aux[aux["proyecto"]>2]
	fig = px.pie(aux, values="proyecto", names="nombre cliente", color="proyecto", color_discrete_sequence = px.colors.sequential.Blues)#, title="Clients with more than 3 projects")
	#fig.update_layout(autosize = True, title = {"text": "Horas Ejecutadas Vs Etapas del Proyecto", "font": {"color": "black", "size": 25}, 'x': 0.5})
	#fig.update_traces(textposition="inside", textinfo="percent+label", title = {"text": "Clients with more than 3 projects", "font": {"color": "black", "size": 25}})
	#fig.show()
	return fig

#Graph treemap
def get_active_proyects():
	#tome 89 para que me diera 11/08/2020 dado que la fecha maxima del log que tenemos es 11/09/2020, pero deberis quedar 30 fijo
	fecha_min_cond=datetime.now() - timedelta(days=89)
	original['fecha'] = pd.to_datetime(original['fecha'])
	gr = original[original['fecha']>fecha_min_cond][['funcionario', 'proyecto']].drop_duplicates()
	gr2 = pd.DataFrame(gr['funcionario'].value_counts().reset_index())
	gr2.columns = ['funcionario', 'num_projects']
	fig = px.treemap(gr2, path=["funcionario"], values="num_projects", color='num_projects', color_continuous_scale='Blues')#, title='Number of active projects in the last month per staff member')
	#fig.update_traces(autosize = True, title = {"text": "Number of active projects in the last month per staff member", "font": {"color": "black", "size": 25}})
	#fig.show()
	return fig	

#Layout Cards
layout_Cards = html.Div([
		dbc.Row([
		dbc.Col(
			dbc.Card([
				dbc.CardHeader("Number of projects in data base"),
				dbc.CardBody([
					html.H4(var_poy, className="card-title"),
					#html.Label("Poner las diviones aca 1"),
				])	
			], 
			color="light", 
			#inverse=True
			), 
			width=3 
		),
		dbc.Col(
			dbc.Card([
				dbc.CardHeader(["Average number of activity records per project is:", html.Br()]),
				dbc.CardBody([
					html.H4(var_avg_cli, className="card-title"),
					#html.Label("Poner las diviones aca 2"),
				])	
			], 
			color="light", 
			#inverse=True
			), 
			width=3 #width="auto"
		),
		dbc.Col(
			dbc.Card([
				dbc.CardHeader(["Average number of hours per project is:", html.Br()]),
				dbc.CardBody([
					html.H4(var_avg_pro, className="card-title"),
					#html.Label("Poner las diviones aca 3"),
				])	
			], 
			color="light", 
			#inverse=True
			), 
			width=3 
		),
		dbc.Col(
			dbc.Card([
				dbc.CardHeader("Average number of types of activities is:"),
				dbc.CardBody([
					html.H4(var_avg_act, className="card-title"),
					#html.Label("Poner las diviones aca 4"),
				])	
			], 
			color="light", 
			#inverse=True
			), 
			width=3 
		)
	], className='justify-content-center'
	),
])

#-------------------------------
#Main Layout
#-------------------------------
layout = html.Div([
    html.Br(),
	layout_Cards, 
	html.Br(),
	html.Div([
        html.H4("Clients with more than 3 projects"),
		dcc.Graph(
            id = "Clients_with_more_than_3_projects",
			figure = get_clients_proyects()
        )
    ]),
	html.Div([
        html.H4("Number of active projects in the last month per staff member"),
		dcc.Graph(
            id = "Number_of_active_projects_in_the_last_month_per_staff_member",
			figure = get_active_proyects()
        )
    ]),
	html.Div([
         html.H4("Projects"),
        dcc.Dropdown(
            id = "proy_selector",
            options = get_proy(original.proyecto.sort_values().unique()),
            multi = True, value = original.proyecto.sort_values().unique()[1]
        )
    ]),
    html.Div([
        html.Label('Activity Graph'),#generate_table(original)
        dcc.Graph(id = "actividades_por_proyecto")                    
    ])
])


# CallBack de Panorama General
@app.callback(
    Output(component_id="actividades_por_proyecto", component_property="figure"),
    [Input(component_id="proy_selector",            component_property="value")])
def update_graph_scatter(proyectos):
    # print(proyectos)
    if isinstance(proyectos, str):
        proyectos = [proyectos]
        
    fig = go.Figure()
    for p in proyectos:
        aux = original[original["proyecto"] == p]
        aux["fecha"] = pd.to_datetime(aux["fecha"], errors = "coerce")
        aux = aux.groupby([aux["fecha"].dt.year, aux["fecha"].dt.month])["actividad"].count().to_frame()#.plot(kind="bar", title  = t)
        aux.index.set_names(["año", "mes"], inplace = True)
        aux.reset_index(inplace = True)
        aux["periodo"] = pd.to_datetime(aux[["año","mes"]].astype(str).agg('-'.join, axis = 1))
        X = aux.periodo
        Y = aux.actividad

        fig.add_trace( 
            go.Scatter( 
            x = list(X), 
            y = list(Y), 
            name=p, 
            mode= "lines+markers"
            )
        )

    fig.update_layout(autosize=True, title = {"text": "Activity in Projects", "font": {"color": "black", "size": 25}, 'x': 0.5}, xaxis_title = 'project date', yaxis_title = 'Number of projects')
    return fig