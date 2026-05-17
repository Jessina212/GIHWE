import os

import sqlite3
from flask import Flask, render_template, request, session, redirect
from cs50 import SQL
from helpers import login_required
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required, apology


# confirgure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    # for getting a quote at random from the database, the fetchone().funtion just return it as one value rather than a. set returned by db. execute
    quote = db.execute("SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1")
    quote = quote[0]["quote"] if quote else None

    # initialising the variable
    task = None

    if request.method == "POST":
        # getting the user input, checking itt. and if not none, tthen using. hte input. to. fnid a task from. t he database that matches the time enetered by the user
        try:
            minutes = int(request.form.get("time"))
        except (TypeError, ValueError):
            minutes = None
        if minutes is not None:
            task = db.execute(
                "SELECT description FROM tasks WHERE max_time >= ? ORDER BY RANDOM() LIMIT 1", minutes)
            task = task[0]["description"] if task else None
    rows = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    name = rows[0]["username"]
    return render_template("index.html", quote=quote, task=task, name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("Password and Confirmation do not match")

        hashed_password = generate_password_hash(password,  method='pbkdf2:sha256')

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", name, hashed_password)
        except ValueError:
            return apology("Username already exists")

        return redirect("/")

    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)

# the database was filled with hundreds of quotes and tasks using ChatGPT's help.
