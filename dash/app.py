# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly 
import plotly.graph_objs as go 

#this function allows to use a different port
def run_server(self,
               port = 8050,
               debug = True,
               threaded = True,
               **flask_run_options):
    self.server.run(port = port, debug = debug, **flask_run_options)

#print table
def generate_table(dataframe, max_rows = 10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

#get projects from db
def get_proy(proyectos):
    r = []
    for p in proyectos:
        r. append({'label': p, 'value': str(p)})
    return r
    
    
#Load datasets
original = pd.read_hdf('data.h5', 'original')
new_variables = pd.read_hdf('data.h5', 'new_variables')
univariado = pd.read_hdf('data.h5', 'univariado')

# Read style of internet (css file)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# Init my app dash and define my style CSS
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)#, suppress_callback_exceptions=True)
#change default port
#Layouts

layout_titulo = html.Div(
    className='row',
    children = 
    [
        html.H2(children = "TITULO"),   
    ],style={'text-align': 'center'}
)  

layout_actividades_proyectos = html.Div(
    className='row',
    children = [
        html.Div(
            className="four columns",
            children = [
            html.Label('Proyectos'),
            dcc.Dropdown(
                id='proy_selector',
                options = get_proy(original.Proyecto.sort_values().unique()),
                multi=True, value = original.Proyecto.sort_values().unique()[12]
            ),
            
        ]),
        html.Div(
            className="eight columns",
            children = [
            #html.Label('grafica'),#generate_table(original)
            dcc.Graph(id='actividades_por_proyecto')                    
        ])
    ]
)
  
#app layout  
app.layout = html.Div(
    children = [layout_titulo, layout_actividades_proyectos    
    ]
)


#callbacks
@app.callback(
    Output('actividades_por_proyecto', 'figure'),
    [Input('proy_selector', 'value')])
def update_graph_scatter(proyectos):
    print(proyectos)
    if isinstance(proyectos, str):
        proyectos = [proyectos]
    fig = go.Figure()
    for p in proyectos:
        aux = original[original['Proyecto'] == p]
        aux['Fecha'] = pd.to_datetime(aux['Fecha'], errors='coerce')
        aux = aux.groupby([aux["Fecha"].dt.year, aux["Fecha"].dt.month])["Actividad"].count().to_frame()#.plot(kind="bar", title  = t)
        aux.index.set_names(["Año", "Mes"], inplace=True)
        aux.reset_index(inplace = True)
        aux['Periodo'] = pd.to_datetime(aux[['Año','Mes']].astype(str).agg('-'.join, axis = 1))
        #fig = px.bar(aux, x = 'Periodo', y = 'Actividad')
        X = aux.Periodo
        Y = aux.Actividad

        fig.add_trace( 
            go.Scatter( 
            x=list(X), 
            y=list(Y), 
            name=p, 
            mode= 'lines+markers'
            )
        )
    """
    # css para tema oscuro
    fig.update_layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Actividad en los proyectos', 'font': {'color': 'white'}, 'x': 0.5}
    )
    """
    fig.update_layout(title={'text': 'Actividad en los proyectos', 'font': {'color': 'black', 'size': 25}, 'x': 0.5})
    return fig#{'data': [data], 'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)} 
  
if __name__ == '__main__':
    app.run_server(debug = True, port = 8057)