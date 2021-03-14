from scipy import stats
import pandas as pd
import numpy as np


sample_means = []


def reset():
    global sample_means
    sample_means = []


def prepare(data_series, number_of_balls):
    return (
        pd.merge(
            pd.Series(np.zeros(number_of_balls,), name='data'),
            data_series.round().value_counts().rename('data'),
            how='left',
            left_index=True,
            right_index=True
        )
        .fillna(0)
        .assign(data=lambda x: x.sum(axis=1))
        ['data']
    )


def plot(dist, population, number_of_balls, n_samples, sample_size):
    population = pd.Series(population)
    pop_mean = population.mean()
    pop_std = population.std()
    global sample_means
    for _ in range(n_samples):
        sample = pd.Series(dist.rvs(sample_size))
        sample_mean = sample.mean()
        sample_std = sample.std()
        sample_means.append(sample_mean)
    num_samples_so_far = len(sample_means)
    if num_samples_so_far > 0:
        mean_sample_mean = sum(sample_means) / num_samples_so_far
        std_sample_mean = pd.Series(sample_means).std()
    else:
        mean_sample_mean = np.nan
        std_sample_mean = np.nan
    if n_samples == 0:
        sample = pd.Series([np.nan])
        sample_mean = np.nan
        sample_std = np.nan
        mean_sample_mean = np.nan
        std_sample_mean = np.nan
    figure = {
        'data': [
            {
                'y': prepare(population, number_of_balls),
                'type': 'bar',
                'name': 'Population'
            },
            {
                'y': prepare(sample, number_of_balls),
                'type': 'bar',
                'xaxis': 'x2',
                'yaxis': 'y2',
                'name': f'Sample (size {sample_size})',
                'marker': {'color': 'red'}
            },
            {
                'x': pd.Series(sample_means),
                'type': 'histogram',
                'xaxis': 'x3',
                'yaxis': 'y3',
                'name': 'Sample Means',
                'marker': {'color': 'green'},
                'nbinsx': number_of_balls
            }
        ],
        'layout': {
            'margin': {'l': 100, 'r': 100, 't': 100, 'b': 100},
            'width': 1200,
            'height': 800,
            'yaxis': {
                'anchor': 'x',
                'domain': [0.8, 1.0]
            },
            'yaxis2': {
                'anchor': 'x2',
                'domain': [0.45, 0.75]
            },
            'yaxis3': {
                'anchor': 'x3',
                'domain': [0.0, 0.4]
            },
            'bargap': 0.30,
            'xaxis': {
                'anchor': 'y',
                'domain': [0.0, 1.0],
                'tickmode': 'linear',
                'tick0': 0,
                'dtick': 1,
                'range': [-0.5, number_of_balls-0.5]
            },
            'xaxis2': {
                'anchor': 'y2',
                'domain': [0.0 ,1.0],
                'tickmode': 'linear',
                'tick0': 0,
                'dtick': 1,
                'range': [-0.5, number_of_balls-0.5]
            },
            'xaxis3': {
                'anchor': 'y3',
                'domain': [0.0 ,1.0],
                'tickmode': 'linear',
                'tick0': 0,
                'dtick': 1,
                'range': [-0.5, number_of_balls-0.5]
            },
            'title': {
                'text': f'Number of samples: {num_samples_so_far}',
            },
            'shapes': [
                {
                    'type': 'line',
                    'yref': 'paper', 'y0': 0.8, 'y1': 1,
                    'xref': 'x', 'x0': pop_mean, 'x1': pop_mean,
                    'line': {'color': 'black', 'width': 4, 'dash': 'dash'},
                },
                {
                    'type': 'line',
                    'yref': 'paper', 'y0': 0.45, 'y1': 0.75,
                    'xref': 'x', 'x0': sample_mean, 'x1': sample_mean,
                    'line': {'color': 'black', 'width': 4, 'dash': 'dash'},
                } if sample_mean == sample_mean else {},
                {
                    'type': 'line',
                    'yref': 'paper', 'y0': 0, 'y1': 0.4,
                    'xref': 'x', 'x0': mean_sample_mean, 'x1': mean_sample_mean,
                    'line': {'color': 'black', 'width': 4, 'dash': 'dash'},
                } if mean_sample_mean == mean_sample_mean else {},
                {
                    'type': 'line',
                    'yref': 'paper', 'y0': 0, 'y1': 0.4,
                    'xref': 'x', 'x0': mean_sample_mean - std_sample_mean, 'x1': mean_sample_mean - std_sample_mean,
                    'line': {'color': 'black', 'width': 4, 'dash': 'dash'},
                } if std_sample_mean == std_sample_mean else {},
                {
                    'type': 'line',
                    'yref': 'paper', 'y0': 0, 'y1': 0.4,
                    'xref': 'x', 'x0': mean_sample_mean + std_sample_mean, 'x1': mean_sample_mean + std_sample_mean,
                    'line': {'color': 'black', 'width': 4, 'dash': 'dash'},
                } if std_sample_mean == std_sample_mean else {},
            ]
        }
    }
    df = pd.DataFrame(
        [
            ['Population', pop_mean, pop_std],
            ['Sample', sample_mean, sample_std],
            ['Sample Means', mean_sample_mean, std_sample_mean]
        ],
        columns=['index', 'Mean', 'Standard Deviation']
    ).set_index('index').applymap(lambda x: f'{x:.2f}').reset_index()
    columns = [{"name": i, "id": i} for i in df.columns]
    data = df.to_dict('records')
    return figure, columns, data


def update_figure(distribution, number_of_balls, number_of_samples, sample_size):
    if distribution == 'uniform': 
        dist = stats.randint(0, number_of_balls)
    elif distribution == 'normal low variance': 
        dist = stats.norm(number_of_balls/2, number_of_balls/10)
    elif distribution == 'normal high variance': 
        dist = stats.norm(number_of_balls/2, number_of_balls/5)
    else:
        raise NotImplementedError
    population = dist.rvs(10**7)
    return plot(dist, population, number_of_balls, number_of_samples, sample_size)
