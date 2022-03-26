import pandas as pd
import plotly.express as px

df = pd.read_csv('calarasi_data_combined.csv', names=['type', 'lon', 'lat', 'area'])

print(df)

fig = px.scatter_mapbox(df, lon='lon', lat='lat', color='type', zoom=10)
fig.update_layout(mapbox_style='open-street-map')
fig.show()