from . import db
from .models import Post, User
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
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

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

@routes.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id =id).first()

    if not post:
        flash('Post does not exist.', category='error')
    elif current_user.id != post.author:
        flash("You don't have the permission to delkete this post.", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully.', category='success')

    return redirect(url_for('routes.home'))

@routes.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user with that username exists.", category='error')
        return redirect(url_for('routes.home'))

    posts = user.posts

    return render_template('posts.html', user=current_user, posts=posts, username=username)