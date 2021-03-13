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
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=10,
        style_header={
            'font-family': 'Rubik, sans-serif;',
            'font-style': 'normal',
            'font-weight': 'bold',
            'font-size': '16px;',
            'line-height': '22px;',
            'display': 'flex;',
            'align-items': 'center;',
            'letter-spacing': '0.15px;',
            'margin': '1px 9px;',
            'backgroundColor': 'white',
            'fontWeight': 'bold',
            'textAlign': 'left'
        },
        style_cell={
            'font-family': 'Roboto Mono, sans-serif;',
            'font-style': 'normal',
            'font-weight': 'normal',
            'font-size': '14px;',
            'line-height': '22px;',
            'display': 'flex;',
            'align-items': 'center;',
            'letter-spacing': '0.15px;',
            'backgroundColor': '#262421;',
            'margin': '1px 9px;',
            'flex': 'none;',
            'order': '0;',
            'textAlign': 'center'
        },
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['ESPECIALIDADE_INTERNACAO']
        ]
    )