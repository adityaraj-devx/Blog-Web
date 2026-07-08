from flask import Blueprint, render_template
from flask_login import login_required, current_user

routes = Blueprint("routes", __name__)

@routes.route("/")
@routes.route("/base")
def base():
    return render_template("base.html")

@routes.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.username)