
# Utiliza Bootstrap para Hoja de Estilos
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from   dash.dependencies import Input, Output

from importlib import import_module
import warnings

# Connect to main app.py file
from app import app
from app import server

# El llamado de estos modulos tiene que estar DESPUES de que se crea el app.Dash
from apps import home_page_Home_Skit_Consulting, panorama_general, grafica, model, administration

SKING_CONSULTING_LOGO = "/assets/img/skit-consulting-logo.png"

# Barra de Navegacion en Bootstrap
navbar_children = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active=True, href="/")),
        dbc.NavItem(dbc.NavLink("Administration", href="/Administration", disabled=False)),        
        dbc.NavItem(dbc.NavLink("Project Information", href="/Project_Information")),
        dbc.NavItem(dbc.NavLink("Data Exploration", href="/Data_Exploration")),
        dbc.NavItem(dbc.NavLink("Model", href="/Model")),
        
        #, disabled=True
		html.Div([  
			html.A(
				html.Div([
					html.Img(src=SKING_CONSULTING_LOGO, height="50px"),],
					className='rounded float-right',
				),
				href="/",
			),
		]),
	
	],
    pills=True,
)

navbar = dbc.Navbar(
    navbar_children, 
    id='navbar',
    sticky="top",
    className = 'navbar navbar-dark shadow'

)
#Titulo
layout_titulo = html.Div(id="Titulo",
    className = "h3",
    children = 
    [
        html.H2(children = "DS4 - SKING CONSULTING LTDA - GRUPO 70"),   
    ],style = {"text-align": "center"}
)  

#Pie de Pagina
footer = html.Footer(
    [
        html.Div(
            [
                html.Div(
                    [
                        'Copyright © 2020, Licensed under the MIT License.'
                    ],
                    className='copyright'
                )
            ],
            className = 'container py-4'
        )
    ],
    style = {'background-color': '#343a40', 'color': '#aaaaaa'}
)


# define page layout
app.layout = html.Div(
    [
        html.Div(id='blank-output'), # only for the name in the tab
        dcc.Location(id="url", refresh=False),
        navbar,
        # Column for user controls (SIDE BAR) 
        dcc.Loading(  
            id="loading-1",
            type="circle",
            fullscreen=True,
            children=[
                html.Div(
                   
                    id="content",
                                      
                    
                ), 
                
            ],
        ),
        footer
    ]
)


# create callback for modifying page layout
@app.callback(
    Output("content", "children"),
    [Input("url", "pathname")])
def display_page(pathname):    
    if pathname == "/":        
        return home_page_Home_Skit_Consulting.layout  
    if pathname == "/Administration":
        return administration.layout  
    if pathname == "/Project_Information":        
        return panorama_general.layout    
    if pathname == "/Data_Exploration":
        return grafica.layout  
    if pathname == "/Model":
        return model.layout
    else:
        return "404 Page Error! Pelase choose a Link"

    # if not recognised, return home page
    #return home_page_Home_Skit_Consulting.layout


#app run server ----------------------------------------------------------------------------------------------------   
if __name__ == '__main__':
    app.run_server(debug=False, host = '0.0.0.0', port = '8080')
    #app.run_server(debug=True)
   