from flask import Flask, render_template, request, flash, redirect, url_for, session
import plotly.express as px
from MapCreator import getMap
from geopy.geocoders import Nominatim
from functools import partial
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "jenvjjvbhsavhcegHCJfgVFGcvajcfk"
app.permanent_session_lifetime = timedelta(minutes=5)
geolocator = Nominatim(user_agent="my_app_name")

@app.route("/",  methods=["POST", "GET"])
def index():
<<<<<<< Updated upstream
    
    if request.method == "POST":
        search = request.form["search"]
        print(search)
        try:
            lt, ln = search_helper(search)
=======
    geocode = partial(geolocator.geocode, language="es")

    if "theme" not in session:
        session.permanent = True
        session["theme"] = "off"

    
    if request.method == "POST":
        if "Dark Mode" in request.form:
            if session["theme"] == "on":
                session["theme"] = "off"
                print(session["theme"])
            else:
                session["theme"] = request.form["Dark Mode"]

>>>>>>> Stashed changes
            fig = getMap()
            if session["theme"] == "on":
                fig.update_layout(mapbox={'style':'carto-darkmatter'})

            div = fig.to_html(full_html=False)
            return render_template("index.html", div_placeholder=div, theme=session["theme"])
        
        elif "search" in request.form:
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
                if "theme" in session and session["theme"] == "on":
                    fig.update_layout(mapbox={'style':'carto-darkmatter'})
    
                div = fig.to_html(full_html=False)
                return render_template("index.html", div_placeholder=div, theme=session["theme"])
            except:
                flash("Try again!")
                fig = getMap()
                if "theme" in session and session["theme"] == "on":
                    fig.update_layout(mapbox={'style':'carto-darkmatter'})
                div = fig.to_html(full_html=False)
                return render_template("index.html", div_placeholder=div, theme=session["theme"])
        else:
            fig = getMap()
            if "theme" in session and session["theme"] == "on":
                fig.update_layout(mapbox={'style':'carto-darkmatter'})
            div = fig.to_html(full_html=False)
            return render_template("index.html", div_placeholder=div, theme=session["theme"])

    else:
        fig = getMap()
        if "theme" in session and session["theme"] == "on":
            fig.update_layout(mapbox={'style':'carto-darkmatter'})
        div = fig.to_html(full_html=False)
        return render_template("index.html", div_placeholder=div, theme=session["theme"])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return redirect(url_for("index"))


def search_helper(search):
    geocode = partial(geolocator.geocode, language="es")
    if "," in search:
        l = search.split(",")
        lt = float(l[0])
        ln = float(l[1])
    else:
        lt = geocode(search).latitude
        ln = geocode(search).longitude
    return lt, ln


if __name__ == "__main__":
    app.run(debug=True)
