import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
import os
import numpy as np

def plot_spread(fname, zoom, spread_time):

    ddf = pd.read_csv(fname)
    ddf = ddf[ddf['#time'] == spread_time]
    fig = px.scatter_mapbox(ddf, lon='x', lat='y', color='location_type', zoom=zoom)
        
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    region_map = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return region_map

def plot_map(fname, zoom):

    ddf = pd.read_csv(fname, names=['Type', 'Longitude', 'Latitude', 'Area'])
    fig = px.scatter_mapbox(ddf, lon='Longitude', lat='Latitude', color='Type', zoom=zoom)
        
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    region_map = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return region_map

def plot_demo(fname, region):

    age_dist_df = pd.read_csv(fname)
    fig = px.line(age_dist_df[region], labels={
                     "index": "Age",
                     "value": "Population",
                 },)
    fig.update_layout(showlegend=False)
    demographics = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return demographics

def plot_measures(fname):

    df = pd.read_csv(fname)

    for ii in range(len(df)):
        for kk in list(df.columns):
            if df.loc[ii][kk] == '-':
                if ii == 0:
                    df.loc[ii][kk] = 0
                else:
                    df.loc[ii][kk] = df.loc[ii-1][kk]

    df = df.set_index('date')
    cols = list(df.columns)[4:]
    print(cols, flush=True)


    fig = px.line(df[cols], labels={'date': 'Date', 'value':'Value'})

    mm = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return mm

def plot_results_overall(filename):

    df = pd.read_csv(filename)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.rename(columns={'#time': 'time'})
    df = df.set_index('time')
    
    df = df[['susceptible', 'exposed', 'infectious', 'recovered', 'dead']]
    
    fig = px.line(df, labels={'value': 'Population', 'time':'No. of Days'})

    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig

def plot_results_hospitals(filename):

    df = pd.read_csv(filename)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.rename(columns={'#time': 'time'})
    df = df.set_index('time')
    
    df = df[['num hospitalisations today', 'hospital bed occupancy', 'cum num hospitalisations today']]
    
    fig = px.line(df, labels={'value': 'Population', 'time':'No. of Days'})
    
    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig

def compile_data(borough, observable, scenario, res_dir):

    file_list = os.listdir(res_dir)
    borough_files = [res_dir + x for x in file_list if borough in x.split('-') and scenario in x.split('-') and 'latest.csv' not in x.split('-')]
    df = [pd.read_csv(x) for x in borough_files]
    ll = list((x[observable] for x in df))
    for i in range(len(ll)):
        ll[i].name = 'Trial_' + str(i+1)
    dd = pd.concat(ll, axis=1)

    assert not dd.isnull().values.any()

    dd['mean'] = dd.mean(axis=1)
    dd['std'] = dd.std(axis=1)
    ds = pd.concat([dd['mean'], dd['mean'] + (1.96/np.sqrt(len(ll)))*dd['std'], dd['mean'] - (1.96/np.sqrt(len(ll)))*dd['std']], axis=1)
    ds = ds.rename(columns={0: 'upper', 1: 'lower'})
    ds = ds.reset_index()
    ds = ds.rename(columns={'index': 'time'})

    return ds

def create_traces(ds, obs, label):
    return [
        go.Scatter(
        name=label,
        x=ds['time'],
        y=ds['mean'],
        mode='lines',
        showlegend=True,
        ),

        go.Scatter(
        name='Upper',
        x=ds['time'],
        y=ds['upper'],
        mode='lines',
        showlegend=False,
        line=dict(width=0),
        ),

        go.Scatter(
        name='Lower',
        x=ds['time'],
        y=ds['lower'],
        mode='lines',
        showlegend=False,
        line=dict(width=0),
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty'
        )
    ]

def plot_aggregated_data(borough, observable, scenario, res_dir):

    traces = []
    for sc in scenario:
        for ii in range(len(observable)):
            obs = observable[ii]
            ds = compile_data(borough, obs, sc, res_dir)
            traces.extend(create_traces(ds, obs, label=obs))

    fig = go.Figure(traces)

    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig