from flask import Flask, render_template, request, flash
import plotly.express as px
from MapCreator import getMap
from geopy.geocoders import Nominatim
from functools import partial

app = Flask(__name__)
app.secret_key = "jenvjjvbhsavhcegHCJfgVFGcvajcfk"
geolocator = Nominatim(user_agent="my_app_name")

@app.route("/",  methods=["POST", "GET"])
def index():
    geocode = partial(geolocator.geocode, language="es")
    if request.method == "POST":
        search = request.form["search"]
        print(search)
        try:
            if "," in search:
                l = search.split(",")
                lt = float(l[0])
                ln = float(l[1])
            else:
                lt = geocode(search).latitude
                ln = geocode(search).longitude
            fig = getMap()
            fig.update_layout(mapbox=dict(center=dict(lat=lt, lon=ln), zoom=8))
            div = fig.to_html(full_html=False)
            return render_template("index.html", div_placeholder=div)
        except:
            flash("Try again!")
            fig = getMap()
            div = fig.to_html(full_html=False)
            return render_template("index.html", div_placeholder=div)
    else:
        fig = getMap()
        div = fig.to_html(full_html=False)
        return render_template("index.html", div_placeholder=div)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=False)