from . import db
from .models import Post
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request

routes = Blueprint("routes", __name__)

@routes.route("/")
def base():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    return render_template("base.html")

@routes.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.username)

@routes.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash("Post can't be empty.", category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Blog posted.", category='success')
            return redirect(url_for('routes.home'))

    return render_template('create_post.html', user=current_user)