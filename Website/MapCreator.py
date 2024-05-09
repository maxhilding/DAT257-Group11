import pandas as pd
import plotly.graph_objects as go
from Database.DatabaseConnector import *


def getMap():
    a, b = setUpData()
    return createMap(a, b)

def setUpData() -> (pd.DataFrame, pd.DataFrame):
    print("Getting data")
    fetcher = DatabaseConnector()
    data = fetcher.getData()
    df = pd.DataFrame(data)
    m = df['working'] == True
    a, b = df[m], df[~m]
    print(a)
    print(b)
    return a,b

def createMap(a : pd.DataFrame, b: pd.DataFrame) -> go.Figure:
    print("Creating map")
    fig = go.Figure(go.Scattermapbox(
        lon=a['lon'],
        lat=a['lat'],
        mode="markers",
        marker={'size':10, 'color':'blue'},
        text=a['address'],
        name='Working'
    ))

    fig.add_trace(go.Scattermapbox(
        lon=b['lon'],
        lat=b['lat'],
        mode="markers",
        marker={'size':10, 'color':'red'},
        text=b['address'],
        name='Not working'
    ))


    fig.update_layout(
        mapbox={'style':'open-street-map', 'zoom':1},
        width=1100,
        height=600,
        margin={"r": 0, "t": 50, "l": 0, "b": 10}
    )
    
    return fig
    

if __name__ == "__main__":
    fig = getMap()
    fig.show()