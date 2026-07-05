from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
@routes.route("/base")
def base():
    return render_template("base.html")

@routes.route("home")
def home():
    return render_template("home.html")