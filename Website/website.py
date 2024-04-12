from flask import Flask, redirect, url_for, render_template
import plotly.express as px
from MapCreator import getMap

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=False)