# import plotly.express as px
# import pandas as pd
# from Database.DatabaseConnector import *
#
#
# def getMap():
#     df: pd.DataFrame = setUpData()
#     return createMap(df)
#
#
# def setUpData() -> pd.DataFrame:
#     print("Getting data")
#
#     fetcher = DatabaseConnector()
#     data = fetcher.getData()
#     # Just some placeholder data for now
#     # data: dict = {
#     # "idnr": [1, 2, 3],
#     # "lon": [12.45, 12.48, 12.43],
#     # "lat": [41.88, 41.89, 41.8]
#     # }
#     return pd.DataFrame(data)
#
# def createMap(df : pd.DataFrame) -> px.scatter_mapbox:
#     print("Creating map")
#     fig = px.scatter_mapbox(df,
#                         lon = df['lon'],
#                         lat = df['lat'],
#                         text = df['address'],
#                         zoom = 10,
#                         width = 1200,
#                         height = 900,
#                         title = 'Water Fountain Map')
#     fig.update_layout(mapbox_style="open-street-map")
#     fig.update_layout(margin={"r":0,"t":50, "l":0, "b":10})
#
#     return fig
#
# if __name__ == "__main__":
#     fig = getMap()
#     fig.show()

import pandas as pd
import plotly.graph_objects as go
from Database.DatabaseConnector import *


def getMap():
    df: pd.DataFrame = setUpData()
    return createMap(df)


def setUpData() -> pd.DataFrame:
    print("Getting data")

    fetcher = DatabaseConnector()
    data = fetcher.getData()
    # Just some placeholder data for now
    # data: dict = {
    # "idnr": [1, 2, 3],
    # "lon": [12.45, 12.48, 12.43],
    # "lat": [41.88, 41.89, 41.8]
    # }
    return pd.DataFrame(data)

def createMap(df : pd.DataFrame) -> go.Figure:
    print("Creating map")
    fig = go.Figure(go.Scattermapbox(
        lon=df['lon'],
        lat=df['lat'],
        mode='markers',
        marker=dict(
            size=10,
            color='blue'),
        text=df['address'],

    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lon=df['lon'].mean(), lat=df['lat'].mean()),
            zoom=10
        ),
        width=1200,
        height=900,
        title='Water Fountain Map',
        margin={"r": 0, "t": 50, "l": 0, "b": 10}
    )



    return fig

if __name__ == "__main__":
    fig = getMap()
    fig.show()