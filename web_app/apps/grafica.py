	

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from   dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import json


import pandas as pd
import plotly.express as px
import plotly 
import plotly.graph_objs as go 
import warnings
from data import new_variables


from app import app


#Load datasets Archivo Plano
#original      = pd.read_hdf("./data.h5", "original")
#new_variables = pd.read_hdf("./data.h5", "new_variables")
#univariado    = pd.read_hdf("./data.h5", "univariado")

#Load datasets DataBase
#engine = create_engine("postgresql+psycopg2://postgres:7$col&ds0@ds4a-70-db.cgxzuy7k08ix.us-east-2.rds.amazonaws.com/")
#df_model = pd.read_sql_table('df_model',engine)
#original = pd.read_sql_table('skit_final',engine)
#SKIT_FINAL = pd.read_sql_table('skit_final',engine)
#Table_Stage = pd.read_sql_table('table_stage',engine)
#new_variables = pd.read_sql_table('new_variables',engine)


# Define Funtions
def get_Horas_Ejecutadas_Propias_Proyecto():
	pl=new_variables.groupby(new_variables['etapa']).agg({'Horas Ejecutadas Propias Proyecto':'mean'}).reset_index()
	pl['etapa']=pl['etapa'].apply(str)
	fig = px.scatter(pl, x="etapa", y="Horas Ejecutadas Propias Proyecto",size="Horas Ejecutadas Propias Proyecto", color="etapa",size_max=60,color_discrete_sequence=px.colors.sequential.Blues)
	return fig
''' 
	fig = px.box(new_variables, x = "etapa",  y = "Horas Ejecutadas Propias Proyecto" , points = 'all')
    fig.update_layout(autosize = True, title = {"text": "Hours Executed Own Project", "font": {"color": "black", "size": 25}, 'x': 0.5}, xaxis_title='Stage', yaxis_title='Hours')
    return fig
'''

# Figura Lina (Horas promedio por Etapas)
fig = go.Figure()
fig.update_layout(autosize = True, title = {"text": "Avarage Hours Executed Vs Project Stages", "font": {"color": "black", "size": 25}, 'x': 0.5})
fig.add_trace(go.Violin(y=new_variables['preventa'],box_visible=True, name = 'preventa'))
fig.add_trace(go.Violin(y=new_variables['mercadeo'],box_visible=True, name = 'mercadeo'))
fig.add_trace(go.Violin(y=new_variables['venta'], box_visible=True,name = 'venta'))
fig.add_trace(go.Violin(y=new_variables['seguimiento ofertas koncilia'],box_visible=True, name = 'seguimiento ofertas koncilia'))
fig.add_trace(go.Violin(y=new_variables['requerimientos'], box_visible=True,name = 'requerimientos'))
fig.add_trace(go.Violin(y=new_variables['consultoria'],box_visible=True, name = 'consultoria'))
fig.add_trace(go.Violin(y=new_variables['desarrollo'],box_visible=True, name = 'desarrollo'))
fig.add_trace(go.Violin(y=new_variables['pruebas'],box_visible=True, name = 'pruebas'))
fig.add_trace(go.Violin(y=new_variables['instalaciones'],box_visible=True,name = 'instalaciones'))
fig.add_trace(go.Violin(y=new_variables['infraestructura skit'],box_visible=True, name = 'infraestructura skit'))
fig.add_trace(go.Violin(y=new_variables['capacitacion'],box_visible=True, name='capacitacion'))
fig.add_trace(go.Violin(y=new_variables['soporte'],box_visible=True, name = 'soporte'))
fig.add_trace(go.Violin(y=new_variables['garantia'],box_visible=True, name = 'garantia'))
fig.add_trace(go.Violin(y=new_variables['reprocesos'],box_visible=True, name = 'reprocesos'))
fig.add_trace(go.Violin(y=new_variables['post venta'],box_visible=True, name = 'post venta'))
fig.add_trace(go.Violin(y=new_variables['capacitacion interna'], box_visible=True,name = 'capacitacion interna'))
fig.add_trace(go.Violin(y=new_variables['investigacion'],box_visible=True, name = 'investigacion'))
fig.update_traces(fillcolor='White', line_color='royalblue')


# Figuta 2 (Horas promedio por Etapas 2 Parte)
fig2 = go.Figure()
fig2.add_trace(go.Violin(y=new_variables['preventa_funcionarios'], box_visible=True, name = 'preventa_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['mercadeo_funcionarios'], box_visible=True,name = 'mercadeo_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['venta_funcionarios'],box_visible=True, name = 'venta_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['seguimiento ofertas koncilia_funcionarios'],box_visible=True, name = 'seguimiento ofertas koncilia_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['requerimientos_funcionarios'],box_visible=True, name = 'requerimientos_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['consultoria_funcionarios'],box_visible=True, name = 'consultoria_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['desarrollo_funcionarios'],box_visible=True, name = 'desarrollo_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['pruebas_funcionarios'],box_visible=True, name = 'pruebas_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['instalaciones_funcionarios'],box_visible=True, name = 'instalaciones_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['infraestructura skit_funcionarios'],box_visible=True, name = 'infraestructura skit_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['capacitacion_funcionarios'], box_visible=True,name='capacitacion_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['soporte_funcionarios'],box_visible=True, name = 'soporte_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['garantia_funcionarios'],box_visible=True, name = 'garantia_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['reprocesos_funcionarios'],box_visible=True, name = 'reprocesos_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['post venta_funcionarios'],box_visible=True, name = 'post venta_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['capacitacion interna_funcionarios'],box_visible=True, name = 'capacitacion interna_funcionarios'))
fig2.add_trace(go.Violin(y=new_variables['investigacion_funcionarios'], box_visible=True,name = 'investigacion_funcionarios'))
fig2.update_traces(fillcolor='White', line_color='salmon')


#Layout Grap "Horas Ejecutadas"
layout_Horas_Ejecutadas_Propias_Proyecto = html.Div(
    #className = "row", 
    children = [
        html.Div(
            
            children = [
                #html.H4(children = "Horas Ejecutadas Propias Proyecto"),
                dcc.Graph(
                id = "Hours Executed Own Project",
                figure = get_Horas_Ejecutadas_Propias_Proyecto()
                )
            ],style = {"text-align": "center"}
        )
    ]
)



#Layout "Figura 1 Horas por Proyecto parte 1"
layout_Lina = html.Div(
    #className = "row", 
    children = [
    # html.H4(children = "Etapas vs Horas Promedio"),
    dcc.Graph(
        id='example-graph-2',        
        figure=fig
    )
])


#Layout "Figura 2 Horas por Proyecto parte 2"
layout_Proyecto2 = html.Div(
    #className = "row", 
    children = [
    # html.H4(children = "Etapas vs Horas Promedio"),
    dcc.Graph(
        id='example-graph-3',        
        figure=fig2
    )
])

layout =  html.Div([
            layout_Lina,
            layout_Proyecto2,
			layout_Horas_Ejecutadas_Propias_Proyecto
        ])
