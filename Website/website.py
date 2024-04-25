from flask import Flask, redirect, url_for, render_template, request
import plotly.express as px
from MapCreator import getMap

app = Flask(__name__)
app.secret_key = "AsdsjahdHkNFhade134vksln"

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

@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        lt = float(request.form["lt"])
        ln = float(request.form["ln"])
        print(lt)
        print(ln)
        fig = getMap()
        fig.update_layout(mapbox=dict(center=dict(lat=lt, lon=-ln), zoom=8))
        div = fig.to_html(full_html=False)
        return render_template("searchResult.html", div_placeholder=div)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=False)