import plotly.express as px
import pandas as pd
from Database.DatabaseConnector import *



def getMap():
    df: pd.DataFrame = setUpData()
    return createMap(df)


def setUpData() -> pd.DataFrame:
    print("Getting data")

    fetcher = DatabaseConnector()
    data = fetcher.getData()
    return pd.DataFrame(data)

def createMap(df : pd.DataFrame) -> px.scatter_mapbox:
    print("Creating map")
    fig = px.scatter_mapbox(df, 
                        lon = df['lon'],
                        lat = df['lat'],
                        zoom = 1,
                        width = 800,
                        height = 600,
                        mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":50, "l":0, "b":10})
    return fig

    

if __name__ == "__main__":
    fig = getMap()
    fig.show()