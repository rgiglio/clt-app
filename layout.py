import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import components as cp
from utils import mk_card


layout = html.Div([
    html.Br(),
    html.H1('Sampling Distribution Demonstration'),
    html.Br(),
    html.H3('Instructions'),
    html.Br(),
    dcc.Markdown('This simulation illustrates the concept of a **sampling distribution**.'),
    html.Br(),
    dcc.Markdown('Depicted on the top graph is the population from which we are going to sample.'),
    html.Br(),
    dcc.Markdown(f'There are `U` different values in the population: the integers from 0 to `U` (inclusive).'),
    html.Br(),
    dbc.Row([
        html.Label(['U'], style={"margin-left": "15px", 'font-weight': 'bold', "text-align": "center"}), cp.number_of_balls,
    ]),
    html.Br(),
    dcc.Markdown('You can think of the population as consisting of having an extremely large number of balls with 0\'s, an extremely large number with 1\'s, etc. on them.'),
    html.Br(),
    dcc.Markdown('The height of the distribution shows the relative number of balls of each number.'),
    html.Br(),
    dbc.Row([
        html.Label(['Population distribution'], style={"margin-left": "15px", 'font-weight': 'bold', "text-align": "center"}), cp.distribution,
    ]),
    html.Br(),
    dcc.Markdown(f'If you push the `add 1 sample` buton below, `K` balls are selected and are plotted on the second graph. The mean of this sample of `K` is then computed and plotted on the third graph.'),
    html.Br(),
    dbc.Row([
        html.Label(['K'], style={"margin-left": "15px", 'font-weight': 'bold', "text-align": "center"}), cp.sample_size,
    ]),
    html.Br(),
    dcc.Markdown('If you push the `add 1 sample` button again, another sample of `K` will be taken, and again plotted on the second graph. The mean will be computed and plotted on the third graph.'),
    html.Br(),
    dcc.Markdown('This third graph is labeled "Distribution of Sample Means, N = `K`" because each value plotted is a sample mean based on a sample of `K`. At this point, you should have two means plotted in this graph.'),
    html.Br(),
    dcc.Markdown('The mean is depicted graphically on the distributions themselves by solid vertical bars below the X-axis. Dashed lines extends one standard deviation in length in both directions.'), 
    dcc.Markdown('The values of both the mean and the standard deviation are given to the top of the graph. Notice that the numeric form of a property matches its graphical form.'),
    html.Br(),
    dcc.Markdown('The sampling distribution of a statistic is the relative frequency distribution of that statistic that is approached as the number of samples (not the sample size!) approaches infinity.'),
    dcc.Markdown('To approximate a sampling distribution, click the `add 1000 sample` button several times. The bottom graph is then a relative frequency distribution of the thousands of means. It is not truly a sampling distribution because it is based on a finite number of samples. Nonetheless, it is a very good approximation.'),
    html.Br(),
    dbc.Col(cp.reset_button),
    html.Br(),
    dbc.Col(cp.addup_button),
    html.Br(),
    dbc.Col(cp.addup1000_button),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.Spinner(cp.table_output)),
    ]),
    dbc.Row([
        dbc.Col(dbc.Spinner(cp.clt_output)),
    ]),
    html.Br(),
], className='container')