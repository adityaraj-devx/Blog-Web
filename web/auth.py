from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html", hide_nav=True)

@auth.route("/signup")
def signup():
    return render_template("signup.html", hide_nav=True)

@auth.route("/forgot")
def forgot():
    return render_template("forgot.html", hide_nav=True) 

@auth.route("/logout")
def logout():
    return redirect(url_for("routes.base"))