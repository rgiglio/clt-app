from datetime import date

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable

from utils import mk_empty_datatable


number_of_balls = dcc.Input(
    id='number-of-balls',
    type='number',
    placeholder='Number of balls',
    min=2, max=100, step=1, value=33,
    style={"margin-left": "15px"}
)
number_of_samples = dcc.Input(
    id='number-of-samples',
    type='number',
    placeholder='Number of samples',
    min=1, max=10**6, step=1, value=1,
)
sample_size = dcc.Input(
    id='sample-size',
    type='number',
    placeholder='N',
    min=2, max=10**6, step=1, value=5,
    style={"margin-left": "15px"}
)
reset_button = dbc.Button('Reset', id='reset', n_clicks=0)
addup_button = dbc.Button('Add 1 sample', id='addup', n_clicks=0, block=True)
addup1000_button = dbc.Button('Add 1000 samples', id='addup1000', n_clicks=0, block=True)

clt_output = dcc.Graph(id='clt-output')
