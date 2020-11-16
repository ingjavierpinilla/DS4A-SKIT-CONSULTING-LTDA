import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd
import numpy as np
import json


# Section layout --------------------
layout = html.Div([
        html.Div([
                html.Div([
                    html.Div(
                        html.P(
							'Estimation Modelling of Project Development for Skit Consulting LTDA', 
							#className='mb-10 display-4 font-weight-bold text-home-title font-medium'
							className='h1'
						)	
                    ),
                    html.Div([
                        html.P(
							'Company Introduction',
							className='h2'),
						html.P(
                            'Skit Consulting is a software company with 15 years of experience in the market. Its main clients are companies in the financial sector, to whom it offers products for bank reconciliation, operational risk, payment button and IT consulting services, flexible plant and software factory.', 
                            className='lead font-weight-normal text-dark font-home-m text-justify'
                        ),
						html.P(
							'Business Problem',
							className='h2'),
						html.P(
                            'The company has a repository of historical information, which allows it to evaluate the time invested in each of the projects developed. This data is also used for basic historical analysis, but not for the identification of trends or prospective analysis. It is expected that this information will be used to make estimates of different types of projects, identifying which resources and time (cash and calendar) we require for their development.', 
                            className='lead font-weight-normal text-dark font-home-m text-justify'
                        ),
						html.P(
							'Specific Problem',
							className='h2'),
						html.P(
                            'It is necessary to identify trends or prospective analysis in order to make estimates of projects of various kinds, in which the resources and time needed for their development are identified. This, in order to improve the productivity, performance and quality of our projects, with their respective effect on economic performance, in addition to identifying what made the difference in successful projects to replicate these practices in the future.', 
                            className='lead font-weight-normal text-dark font-home-m text-justify'
                        ),
						html.P(
                            """
                            Data Exploration 
                            """, 
                            className='lead font-weight-normal text-dark font-home-m'
                        ),
                        ],
                        className='mb-10',
                    ),
                    html.Div([
                        html.A('Start Here', className='btn btn-outline-secondary text-dark font-home-m', href="/Proyect_Information"),
                    ]),
                    ],
                    className='col-md-10 p-lg-5 mx-auto my-5',
                ),

             ],
             className = 'position-relative overflow-hidden text-center back-home',
        )         

    
])
