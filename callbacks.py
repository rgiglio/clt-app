from dash import callback_context
from dash.dependencies import Input, Output, State
from dash_table import FormatTemplate
from dash_table.Format import Format
import dash

import backend as be


def register_callbacks(app):
    
    @app.callback(
        [Output('clt-output', 'figure'),
         Output('table-output', 'columns'),
         Output('table-output', 'data'),
         Output('session', 'data')],
        [Input('distribution', 'value'),
         Input('number-of-balls', 'value'),
         Input('sample-size', 'value'),
         Input('reset', 'n_clicks'),
         Input('addup', 'n_clicks'),
         Input('addup1000', 'n_clicks')],
        [State('session', 'data')],
    )
    def update_figure(distribution, number_of_balls, sample_size, n_clicks_reset,
                      n_clicks_addup, n_clicks_addup1000, session_data):
        if dash.callback_context.triggered[0]['prop_id'] == 'addup.n_clicks':
            return be.update_figure(distribution, number_of_balls, 1, sample_size, session_data)
        if dash.callback_context.triggered[0]['prop_id'] == 'addup1000.n_clicks':
            return be.update_figure(distribution, number_of_balls, 1000, sample_size, session_data)
        return be.update_figure(distribution, number_of_balls, 0, sample_size, session_data)
