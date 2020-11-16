import dash
import dash_table
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import base64
import datetime
import io

import pandas as pd

import warnings
from data import new_variables, original
from app import app

df = original.head(20)

# Tabla de Datos
layout_dash_Table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.head(20).to_dict("rows"),
)

# Importar Archivos csv --------------------------------
layout_Importar_CSV = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files UTF-8 (*.csv o *.xlsx)')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

# Titulo -----------------------------------------------
title = html.Div([ html.H1(["Administration of Project Development for Skit Consulting LTDA",])])

# Formulario -------------------------------------------
layout_form = dbc.Row([
                dbc.Col(
                        dbc.Form(
                                    [
                                        dbc.FormGroup(
                                                        [
                                                            dbc.Label("Estimated Downtime", html_for="Downtime", width=20),
                                                            dbc.Col(
                                                                dbc.Input(type="number", id='downtime', placeholder="Enter estimated downtime [5 - 120]", min=5, max=120, step=1, value=30, className="mb-3", size='10px', bs_size ="sm"),
                                                            )
                                                        ],                                                        
                                                    ),
                                        html.Button("Submit", id='button-01'),
                                        html.Div(id='my-div')
                                    ],
                                    
                                )
                        )
                ])  


layout =  html.Div([
    html.Br(),
	dbc.Alert(["Enter the number of days of inactivity (no activity log) so that data exploration is on closed projects." ], 
		color = "secondary", 
	),
	title, 
    layout_Importar_CSV,
    layout_form,
    layout_dash_Table
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        df.rename(columns={'Nombre Cliente': 'nombre cliente', 'Versión': 'version', 'Responsable': 'responsable', 'Actividad': 'actividad', 'Importancia': 'importancia', 'Fecha': 'fecha', 'Horas': 'horas', 'Funcionario': 'funcionario', 'Proyecto': 'proyecto', 'Horas planeadas': 'horas planeadas', 'Activo': 'activo', 'Año': 'ano', 'Mes': 'mes', 'Día': 'dia'}, inplace=True)
        df['fecha'] = pd.to_datetime(df.fecha)
        
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.head(10).to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],            
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='button-01', component_property='n_clicks'), State(component_id='downtime', component_property='value')]
)

def update_output2(n_clicks,  value_downtime):
    return 'The input value was "{}" , and the button has been clicked {}  times'.format(        
        value_downtime,
        n_clicks
    )        