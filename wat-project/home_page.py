from flask import render_template,jsonify
from Setting import OpenInit
openInit = OpenInit()
app = openInit.app()

@app.route("/")
def home_page():
    return render_template("Index.html")