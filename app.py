import os

from dash import Dash
from dash_bootstrap_components.themes import FLATLY as theme
from dash.dependencies import Input, Output
import dash_html_components as html

from callbacks import register_callbacks
from layout import layout


app = Dash(__name__, external_stylesheets=[theme])
app.config.suppress_callback_exceptions = True
app.title = 'CLT app'
server = app.server
app.layout = layout
register_callbacks(app)


if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    debug = os.getenv('DEBUG') == 'true'
    app.run_server(host='0.0.0.0', port=port, debug=debug)
