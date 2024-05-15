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
    # Starting session, dark mode is off by default
    print(session)
    if "theme" not in session:
        session.permanent = True
        session["theme"] = "off"
    if "center" not in session:
        session["center"] = list()

    # Creating the map with open-street-map style and view of whole world
    fig = getMap()

    #Update Map depending on input
    if request.method == "POST":
        print(request.form)

        search = request.form.get("search")
        theme = request.form.get("Dark Mode")


         # If search is made, try to get latitude & longitude of that location and update center of map
        if search is not None:
            print(search)
            try:
                lt, ln = search_helper(search)
                coordinates = session["center"]
                # Remove old search
                coordinates.clear()
                coordinates.extend([lt, ln])
            except:
                flash("Try again!")
        # If checkbox checked change theme
        elif theme is not None:
            session["theme"] = theme
        else:
            session["theme"] = "off"
       
    print(session)
    # Check if dark mode is on and then update map to be dark 
    if session["theme"] == "on":
        print("Dark mode on")
        fig.update_layout(mapbox={'style':'carto-darkmatter'}, template="plotly_dark")

    if session["center"]:
        lt = session["center"][0]
        ln = session["center"][1]
        fig.update_layout(mapbox=dict(center=dict(lat=lt, lon=ln), zoom=8))
    
    # Finally render the map
    div = fig.to_html(full_html=False)
    return render_template("index.html", div_placeholder=div, theme=session["theme"])

    
@app.route("/about")
def about():
    return render_template("about.html", theme=session["theme"])

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
