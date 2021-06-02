from flask import render_template,Blueprint,jsonify

index = Blueprint("index",__name__)

@index.route("/index")
def index():
    return render_template("Index.html")