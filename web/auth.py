import re
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash


auth = Blueprint("auth", __name__)

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Emial does not exists.', category='error')

    return render_template("login.html", hide_nav=True)

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email already exists.', category='error')
        elif username_exists:
            flash('Username is taken.', category='error')
        elif password != confirm_password:
            flash('Password do not match.', category='error')
        elif len(username) < 3:
            flash('Username is too short.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        elif not email or not re.match(EMAIL_REGEX, email):
            flash('Email is invalid.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, ))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!')
            return redirect(url_for('routes.home'))

    return render_template("signup.html", hide_nav=True)

@auth.route("/forgot")
def forgot():
    return render_template("forgot.html", hide_nav=True) 

@auth.route("/logout")
@login_required
def logout():
    logout_user(current_user)
    return redirect(url_for("routes.base"))