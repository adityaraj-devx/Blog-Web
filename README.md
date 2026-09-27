# NovaHub

A full-stack blogging platform built with Flask. Users can sign up, write posts, comment, and like posts from other members.

**Live site:** https://novahub-int1.onrender.com

## Features

- User authentication (sign up, login, logout, forgot password)
- Create, view, and delete posts
- Comment on posts, with delete permissions for the comment author or post owner
- Like/unlike posts
- Per-user profile pages showing all posts by that user
- Responsive, custom-designed UI (no CSS framework — hand-built design system)

## Tech Stack

- **Backend:** Flask, organized with Blueprints (`routes`, `auth`)
- **Database:** SQLite via SQLAlchemy (Flask-SQLAlchemy)
- **Auth:** Flask-Login, with passwords hashed via Werkzeug
- **Templates:** Jinja2
- **Frontend:** Custom CSS, Bootstrap 5's JS bundle (dropdowns/collapse only — no Bootstrap CSS), Font Awesome icons
- **Server:** Gunicorn (production), Flask's built-in dev server (local)
- **Hosting:** Render

## Project Structure

```
.
├── main.py                # App entry point
├── requirements.txt
├── .env                    # Local environment variables (not committed)
├── instance/
│   └── database.db         # SQLite database (auto-created, not committed)
└── web/
    ├── __init__.py          # App factory, DB init
    ├── auth.py              # Auth routes (login/signup/forgot/logout)
    ├── models.py            # SQLAlchemy models: User, Post, Comment, Like
    ├── routes.py            # Main app routes (posts, comments, likes)
    ├── static/
    │   ├── styles.css
    │   └── script.js
    └── templates/
        ├── layout.html
        ├── base.html
        ├── home.html
        ├── post_container.html
        ├── posts.html
        ├── create_post.html
        ├── login.html
        ├── signup.html
        └── forgot.html
```

## Local Setup

**1. Clone the repo and install dependencies**

```bash
git clone <your-repo-url>
cd <project-folder>
pip install -r requirements.txt
```

*(Optional: use a virtual environment first with `python -m venv venv` then `venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux.)*

**2. Set up environment variables**

Create a `.env` file in the project root:

```
SECRET_KEY=your-random-secret-key
```

Generate a strong value with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**3. Run the app**

```bash
python main.py
```

Visit `http://127.0.0.1:5000`. The SQLite database is created automatically in `instance/database.db` on first run.

## Deployment (Render)

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn main:app`
- **Environment Variables:** `SECRET_KEY` must be set in Render's Environment tab (a local `.env` file is not deployed).
- **Database persistence:** Render's filesystem is ephemeral by default. Either attach a persistent disk mounted at the `instance/` folder, or switch to a managed database (e.g. Postgres) for production use.

## Known Limitations

- SQLite is not ideal for concurrent production traffic — fine for a demo, but a managed database is recommended for real use.
- No password reset tokens/email verification — the "Forgot Password" flow currently updates the password directly rather than sending a reset link.

## License

This project is for personal/portfolio use.