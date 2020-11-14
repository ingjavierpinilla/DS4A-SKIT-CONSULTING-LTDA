

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
    fig = px.box(new_variables, x = "etapa",  y = "Horas Ejecutadas Propias Proyecto" , points = 'all')
    fig.update_layout(autosize = True, title = {"text": "Hours Executed Own Project", "font": {"color": "black", "size": 25}, 'x': 0.5}, xaxis_title='Stage', yaxis_title='Hours')
    return fig

# Figura Lina (Horas promedio por Etapas)
fig = go.Figure()
fig.update_layout(autosize = True, title = {"text": "Avarage Hours Executed Vs Project Stages", "font": {"color": "black", "size": 25}, 'x': 0.5})
fig.add_trace(go.Violin(y=new_variables['capacitacion'],                           name='Training',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['capacitacion interna'],                   name = 'Internal Training',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['consultoria'],                            name = 'Consultancy',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['desarrollo'],                             name = 'Development',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['garantia'],                               name = 'Warranty',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['infraestructura skit'],                   name = 'Infrastructure skit',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['instalaciones'],                          name = 'Installations',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['investigacion'],                          name = 'investigation',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['mercadeo'],                               name = 'Marketing',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['post venta'],                             name = 'After Sales',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['preventa'],                               name = 'Presales',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['pruebas'],                                name = 'Test',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['reprocesos'],                             name = 'Reprocesses',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['requerimientos'],                         name = 'Requirements',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['seguimiento ofertas koncilia'],           name = 'Offer Tracking koncilia',
                marker_color = 'indianred'))
fig.add_trace(go.Violin(y=new_variables['soporte'],                                name = 'Support',
                marker_color = 'lightseagreen'))
fig.add_trace(go.Violin(y=new_variables['venta'],                                  name = 'Sales',
                marker_color = 'indianred'))

# Figuta 2 (Horas promedio por Etapas 2 Parte)
fig2 = go.Figure()
fig2.add_trace(go.Violin(y=new_variables['capacitacion_funcionarios'],             name='Official Training',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['capacitacion interna_funcionarios'],     name = 'Internal training of Officials',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['consultoria_funcionarios'],              name = 'Consulting officials',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['desarrollo_funcionarios'],               name = 'Development officials',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['garantia_funcionarios'],                 name = 'Officials Guarantee',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['infraestructura skit_funcionarios'],     name = 'Infrastructure Skit officials',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['instalaciones_funcionarios'],            name = 'Official Facilities',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['investigacion_funcionarios'],            name = 'Investigation Officials',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['mercadeo_funcionarios'],                 name = 'Marketing Officials',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['post venta_funcionarios'],               name = 'After sales Officials',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['preventa_funcionarios'],                 name = 'Presales Officials',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['pruebas_funcionarios'],                  name = 'Officials Test',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['reprocesos_funcionarios'],               name = 'Reprocessing Officials',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['requerimientos_funcionarios'],           name = 'Officials Requirements',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['seguimiento ofertas koncilia_funcionarios'], name = 'Officials Offer Tracking koncilia',
                marker_color = 'indianred'))
fig2.add_trace(go.Violin(y=new_variables['soporte_funcionarios'],                  name = 'Officials Support',
                marker_color = 'lightseagreen'))
fig2.add_trace(go.Violin(y=new_variables['venta_funcionarios'],                    name = 'Officials Sales',
                marker_color = 'indianred'))




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
