

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output
import pandas as pd
import numpy as np
import pandas as pd
from app import app
import pickle
pkl_filename = "apps/xgboost_skit.pkl"

def scoring(v, model):
    with open(model, 'rb') as output:
        xgb_model = pickle.load(output)
    X = pd.DataFrame(v)
    predicciones = xgb_model.predict(X)
    return np.exp(predicciones)

title = dbc.Row([
            dbc.Col(
                html.Div([ html.H1(["Prediction", dbc.Badge("model", className = "ml-1")])]), 
                width = {"size": 12, "offset": 5}, 
            )
        ])

row1 = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Number of Activities"), 
                    dbc.Select(
                        id = "Numero de Actividades", 
                        options = [
                            {"label": "1", "value": 1}, 
                            {"label": "2", "value": 2}, 
                            {"label": "3", "value": 3}, 
                            {"label": "4", "value": 4}, 
                            {"label": "5", "value": 5}, 
                            {"label": "6", "value": 6}, 
                            {"label": "7", "value": 7}, 
                            {"label": "8", "value": 8}, 
                            {"label": "9", "value": 9}, 
                            {"label": "10", "value": 10}, 
                            {"label": "11", "value": 11}, 
                            {"label": "12", "value": 12}, 
                            {"label": "13", "value": 13}, 
                            {"label": "14", "value": 14}, 
                            {"label": "15", "value": 15}, 
                            {"label": "16", "value": 16}, 
                            {"label": "17", "value": 17}, 
                            {"label": "18", "value": 18}, 
                            {"label": "19", "value": 19}, 
                            {"label": "20", "value": 20}
                        ], 
                    ), 
                    dbc.FormText(
                    "It is the number of activities that will be developed in this project", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.FormGroup(
                        [
                            dbc.Label("Development", html_for = "slider"), 
                            dcc.Slider(id = "desarrollo", min = 0, max = 1, step = 0.05, value = 0, 
                            marks = {
                                    0: {'label': '0'}, 
                                    0.20: {'label': '20%'}, 
                                    0.40: {'label': '40%'}, 
                                    0.60: {'label': '60%'}, 
                                    0.80: {'label': '80%'}, 
                                    1: {'label': '100%'}
                                }
                            ), 
                        ]
                    ), 
                    dbc.FormText(id = 'desarrollo_output', color = "primary"), 
                    dbc.FormText(
                    "It is the percentage of dedication that \"Development\" will have in the project", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
    ], 
    form = True, 
)

row2 = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                  dbc.Label("Pre-sale", html_for = "slider"), 
                    dcc.Slider(id = "preventa", min = 0, max = 1, step = 0.05, value = 0, 
                    marks = {
                            0: {'label': '0'}, 
                            0.20: {'label': '20%'}, 
                            0.40: {'label': '40%'}, 
                            0.60: {'label': '60%'}, 
                            0.80: {'label': '80%'}, 
                            1: {'label': '100%'}
                        }
                    ), 
                    dbc.FormText(id = 'preventa_output', color = "primary"), 
                    dbc.FormText(
                    "It is the percentage of dedication that \"Pre-sale\" will have in the project", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
        dbc.Col(
            dbc.FormGroup(
                [
                  dbc.Label("Requirements", html_for = "slider"), 
                    dcc.Slider(id = "requerimientos", min = 0, max = 1, step = 0.05, value = 0, 
                    marks = {
                            0: {'label': '0'}, 
                            0.20: {'label': '20%'}, 
                            0.40: {'label': '40%'}, 
                            0.60: {'label': '60%'}, 
                            0.80: {'label': '80%'}, 
                            1: {'label': '100%'}
                        }
                    ), 
                    dbc.FormText(id = 'requerimientos_output', color = "primary"), 
                    dbc.FormText(
                    "It is the percentage of dedication that \"Requirements\" will have in the project", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
    ], 
    form = True, 
)

row3 = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                  dbc.Label("Support", html_for = "slider"), 
                    dcc.Slider(id = "soporte", min = 0, max = 1, step = 0.05, value = 0, 
                    marks = {
                            0: {'label': '0'}, 
                            0.20: {'label': '20%'}, 
                            0.40: {'label': '40%'}, 
                            0.60: {'label': '60%'}, 
                            0.80: {'label': '80%'}, 
                            1: {'label': '100%'}
                        }
                    ), 
                    dbc.FormText(id = 'soporte_output', color = "primary"), 
                    dbc.FormText(
                    "It is the percentage of dedication that \"Support\" will have in the project", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Minimum importance"), 
                    dbc.Select(
                        id = "Min_Importancia", 
                        options = [
                            {"label": "3", "value": 3}, 
                            {"label": "4", "value": 4}, 
                            {"label": "5", "value": 5}, 
                            {"label": "6", "value": 6}, 
                            {"label": "7", "value": 7}, 
                            {"label": "8", "value": 8}, 
                            {"label": "9", "value": 9}, 
                            {"label": "10", "value": 10}, 
                        ], 
                    ),
                    dbc.FormText(
                    "Each of the activities has a score, and as not every project requires all the activities, in this field the minimum score is related to the importance of the activities", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
    ], 
    form = True, 
)

row4 = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Development stage number of employees"), 
                    dbc.Input(
                        type = "number", min = 0, 
                        id = "Etapa_Desarrollo_funcionarios", 
                        placeholder = "[0, inf)", 
                    ), 
                    dbc.FormText(
                    "Number of employees in charge of the develpment", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Analysis stage number of employees"), 
                    dbc.Input(
                        type = "number", min = 0, 
                        id = "Etapa_Analisis de Requerimientos_funcionarios", 
                        placeholder = "[0, inf)", 
                    ), 
                    dbc.FormText(
                    "Number of employees in charge of the requirements analysis stage", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
    ], 
    form = True, 
)

row5 = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Support stage number of employees"), 
                    dbc.Input(
                        type = "number", min = 0, 
                        id = "soporte_funcionarios", 
                        placeholder = "[0, inf)", 
                    ), 
                    dbc.FormText(
                    "Number of employees in charge of the support", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Planned hours"), 
                    dbc.Input(
                        type = "number", min = 0, 
                        id = "Horas planeadas", 
                        placeholder = "[0, inf)", 
                    ), 
                    dbc.FormText(
                    "Expected duration of the project in hours", 
                    color = "secondary", 
                    ), 
                ]
            ), 
            width = 6, 
        ), 
    ], 
    form = True, 
)

prediction = html.Div(
    [
        dbc.Button(
            "Predict", 
            id = "button", 
            color = "primary", 
            className = "mb-3", 
        ), 
        html.Div(id = 'output'), 
    ]
)


"""
layout = html.Div([
     title, row1, row2, row3, row4, row5
])
"""
layout = html.Div([
        html.Div([
                html.Div([
                    html.Div(
                        html.P(
							'Prediction model', 
							#className = 'mb-10 display-4 font-weight-bold text-home-title font-medium'
							className = 'h1'
						)	
                    ),
                    html.Div([
                        html.P(
							'In this section we will make a prediction of the number of hours it may take to develop a new project.', 
							#className = 'mb-10 display-4 font-weight-bold text-home-title font-medium'
							className = 'h6'
						),
						html.P(
							'Note: The sum of Pre-sale, Development, Requirements and Support activities cannot exceed 100%.', 
							#className = 'mb-10 display-4 font-weight-bold text-home-title font-medium'
							className = 'h6'
						)]
                    ), 
                    html.Div([
                            row1, row2, row3, row4, row5, 
                        ], 
                        className = 'mb-10', 
                    ), 
                    prediction, 
                    ], 
                    className = 'col-md-10 p-lg-5 mx-auto my-5', 
                ), 

             ], 
             className = 'position-relative overflow-hidden text-center back-home', 
        )         

    
])


@app.callback(
    Output(component_id = 'output', component_property = 'children'), 
        [Input('button', 'n_clicks')], 
        [State('Numero de Actividades', 'value')], 
        [State('requerimientos', 'value')], 
        [State('Min_Importancia', 'value')], 
        [State('Etapa_Analisis de Requerimientos_funcionarios', 'value')], 
        [State('soporte', 'value')], 
        [State('soporte_funcionarios', 'value')], 
        [State('Etapa_Desarrollo_funcionarios', 'value')], 
        [State('preventa', 'value')], 
        [State('desarrollo', 'value')], 
        [State('Horas planeadas', 'value')], 
)
def update_output_div(clicks, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10):
    
    inputs = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    if clicks is not None:
        
        for i in inputs:
            if i == None:
               return "Please fill in all fields"
               break
        if np.round(i2 + i5 + i8 + i9,2) > 1.00:
            return 'The sum of Development + Pre-sale + Requirements + Support can be max. 100%'
        variables = {
            'Numero de Actividades':[int(i1)], 
            'requerimientos':[i2], 
            'Min_Importancia':[int(i3)], 
            'Etapa_Analisis de Requerimientos_funcionarios':[i4], 
            'soporte':[i5], 
            'soporte_funcionarios':[i6], 
            'Etapa_Desarrollo_funcionarios':[i7], 
            'preventa':[i8], 
            'desarrollo':[i9], 
            'Horas Planeadas':[i10]
        }
        #for x, y in variables.items():
        #    print(x, y)
        Y = scoring(variables, "xgboost_skit.pkl")
        Y = Y[0]
        return 'Number of hours estimated for the development of the project: {:3.2f} - {:3.2f}'.format(Y - 0.1 * Y, Y + 0.1 * Y)
    
"""    
@app.callback(
    dash.dependencies.Output('desarrollo_output', 'children'), 
    [dash.dependencies.Input('desarrollo', 'value')])
def update_output(value):
    return 'You have selected "{}"%'.format(value*100)

@app.callback(
    [dash.dependencies.Output('preventa_output', 'children'), dash.dependencies.Output('desarrollo_output', 'children')], 
    [dash.dependencies.Input('preventa', 'value')])
def update_output(value):
    return 'You have selected "{}"%'.format(value*100)
    
@app.callback(
    dash.dependencies.Output('requerimientos_output', 'children'), 
    [dash.dependencies.Input('requerimientos', 'value')])
def update_output(value):
    return 'You have selected "{}"%'.format(value*100)

@app.callback(
    dash.dependencies.Output('soporte_output', 'children'), 
    [dash.dependencies.Input('soporte', 'value')])
def update_output(value):
    return 'You have selected "{}"%'.format(value*100)
    
    
@app.callback(
    [dash.dependencies.Output('desarrollo_output', 'children'), 
    dash.dependencies.Output('preventa_output', 'children'), 
    dash.dependencies.Output('requerimientos_output', 'children'), 
    dash.dependencies.Output('soporte_output', 'children'), 
    dash.dependencies.Output('desarrollo', 'max'), 
    dash.dependencies.Output('preventa', 'max'), 
    dash.dependencies.Output('requerimientos', 'max'), 
    dash.dependencies.Output('soporte', 'max')], 
    [dash.dependencies.Input('desarrollo', 'value'), 
    dash.dependencies.Input('preventa', 'value'), 
    dash.dependencies.Input('requerimientos', 'value'), 
    dash.dependencies.Input('soporte', 'value')])
def sliders(d, p, r , s):
    ctx = dash.callback_context
    if not ctx.triggered:
        slider_id = 'No clicks yet'
    else:
        slider_id = ctx.triggered[0]['prop_id'].split('.')[0]

    val = 1 - np.round(d + p + r + s, 2)

        
    if slider_id == 'desarrollo':
        return 'You have selected "{}"%'.format(d), 'You have selected "{}"%'.format(p), 'You have selected "{}"%'.format(r), 'You have selected "{}"%'.format(s), val, val, val, val
    if slider_id == 'preventa':
        return 'You have selected "{}"%'.format(d), 'You have selected "{}"%'.format(p), 'You have selected "{}"%'.format(r), 'You have selected "{}"%'.format(s), val, val, val, val
    if slider_id == 'requerimientos':
        return 'You have selected "{}"%'.format(d), 'You have selected "{}"%'.format(p), 'You have selected "{}"%'.format(r), 'You have selected "{}"%'.format(s), val, val, val, val
    if slider_id == 'soporte':
        return 'You have selected "{}"%'.format(d), 'You have selected "{}"%'.format(p), 'You have selected "{}"%'.format(r), 'You have selected "{}"%'.format(s), val, val, val, val    
    else:
        return 'You have selected "{}"%'.format(d), 'You have selected "{}"%'.format(p), 'You have selected "{}"%'.format(r), 'You have selected "{}"%'.format(s), 1, 1, 1, 1
        
      
"""  
@app.callback(
    [dash.dependencies.Output('desarrollo_output', 'children'), 
    dash.dependencies.Output('preventa_output', 'children'), 
    dash.dependencies.Output('requerimientos_output', 'children'), 
    dash.dependencies.Output('soporte_output', 'children')], 
    [dash.dependencies.Input('desarrollo', 'value'), 
    dash.dependencies.Input('preventa', 'value'), 
    dash.dependencies.Input('requerimientos', 'value'), 
    dash.dependencies.Input('soporte', 'value')])
def sliders(d_, p_, r_ , s_):
    d = np.round(d_, 2) 
    p = np.round(p_, 2)
    r = np.round(r_, 2)
    s = np.round(s_, 2)
    
    ctx = dash.callback_context
    if not ctx.triggered:
        slider_id = 'No clicks yet'
    else:
        slider_id = ctx.triggered[0]['prop_id'].split('.')[0]

    sum = np.round(d + p + r + s, 2)
    
    if sum <= 1.00:
        return 'You have selected {:.0%}'.format(d), 'You have selected {:.0%}'.format(p), 'You have selected {:.0%}'.format(r), 'You have selected {:.0%}'.format(s)
        
    if slider_id == 'desarrollo':
        return 'You have selected {:.0%}\t The sum of the inputs is: {:.0%}'.format(d, sum), 'You have selected {:.0%}'.format(p), 'You have selected "{}"'.format(r), 'You have selected "{}"'.format(s)
    if slider_id == 'preventa':
        return 'You have selected {:.0%}'.format(d), ('You have selected {:.0%}\t The sum of the inputs is: {:.0%}'.format(p, sum)), 'You have selected {:.0%}'.format(r), 'You have selected {:.0%}'.format(s)
    if slider_id == 'requerimientos':
        return 'You have selected {:.0%}'.format(d), 'You have selected {:.0%}'.format(p), 'You have selected {:.0%}\t The sum of the inputs is: {:.0%}'.format(r, sum), 'You have selected {:.0%}'.format(s)
    if slider_id == 'soporte':
        return 'You have selected {:.0%}'.format(d), 'You have selected {:.0%}'.format(p), 'You have selected {:.0%}'.format(r), 'You have selected {:.0%}\t The sum of the inputs is: {:.0%}'.format(s, sum)    
    else:
        return 'You have selected {:.0%}'.format(d), 'You have selected {:.0%}'.format(p), 'You have selected {:.0%}'.format(r), 'You have selected {:.0%}'.format(s)
