import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table import DataTable


def mk_card(title, obj):
    return dbc.Card(
        dbc.CardBody([
            html.H4(title),
            html.Div([obj])
        ])
    )


def mk_empty_datatable(table_id):
    return DataTable(
        id=table_id,
        style_as_list_view=True,
        editable=False,
        style_header={
            'font-family': 'Rubik, sans-serif;',
            'font-style': 'normal',
            'font-weight': 'bold',
            'font-size': '16px;',
            'line-height': '22px;',
            'display': 'flex;',
            'letter-spacing': '0.15px;',
            'margin': '1px 9px;',
            'backgroundColor': 'white',
            'fontWeight': 'bold',
        },
        style_cell={
            'font-family': 'Roboto Mono, sans-serif;',
            'font-style': 'normal',
            'font-weight': 'normal',
            'font-size': '14px;',
            'line-height': '22px;',
            'display': 'flex;',
            'letter-spacing': '0.15px;',
            'backgroundColor': '#262421;',
            'margin': '1px 9px;',
            'flex': 'none;',
            'order': '0;',
        },
    )