from flask import Flask, redirect, url_for, render_template, request, flash
import plotly.express as px
from MapCreator import getMap
from CityToCoordinates import city2Coordinates
from geopy.geocoders import Nominatim
from functools import partial

app = Flask(__name__)
app.secret_key = "AsdsjahdHkNFhade134vksln"
geolocator = Nominatim(user_agent="my_app_name")

@app.route("/")
def index():
    fig = getMap()
    div = fig.to_html(full_html=False)
    return render_template("index.html", div_placeholder=div)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/search")
def search():
    return render_template("search.html")


def searchWithCityHelper(city):
    geocode = partial(geolocator.geocode, language="es")
    if request.method == "POST":
        print(city)
        try:
            # coordinates = city2Coordinates(city, "Website/static/worldcities.csv")
            # lt = coordinates[0]
            # ln = coordinates[1]
            # print(ln)
            # print(lt)
            lt = geocode(city).latitude
            ln = geocode(city).longitude
            fig = getMap()
            fig.update_layout(mapbox=dict(center=dict(lat=lt, lon=ln), zoom=8))
            div = fig.to_html(full_html=False)
            return render_template("searchResult.html", div_placeholder=div)
        except:
            flash("Try again!")
            return render_template("searchWithCity.html")
    else:
        return render_template("searchWithCity.html")


@app.route("/searchWithCoordinates", methods=["POST", "GET"])
def searchWithCoordinates(lt, ln):
    if request.method == "POST":
        try:
            print(lt)
            print(ln)
            fig = getMap()
            fig.update_layout(mapbox=dict(center=dict(lat=lt, lon=ln), zoom=8))
            div = fig.to_html(full_html=False)
            return render_template("searchResult.html", div_placeholder=div)
        except:
            flash("Try again!")
            return render_template("searchWithCoordinates.html")
    else:
        return render_template("searchWithCoordinates.html")

@app.route("/searchWithCity", methods=["POST", "GET"])
def searchWithCity():
    if request.method == "POST":
        s = request.form["cty"]
        if "," in s:
            l = s.split(",")
            lt = float(l[0])
            ln = float(l[1])
            return searchWithCoordinates(lt, ln)
        else:
            return searchWithCityHelper(s)
    else:
        return render_template("searchWithCity.html")
    

if __name__ == "__main__":
    app.run(debug=False)
