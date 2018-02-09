# blog.py - controller

# imports
import sqlite3
from flask import Flask, render_template, request, session, flash, redirect, \
    url_for, g

# configuration
DATABASE = "blog.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = ".f\x96\x01\x9d\x94\xf0S\xd0\xfa\xdeZ\xcb\x15L\x07\xdf\x18\xf9r\xd14\x0e"

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=["GET", "POST"])
def login():
    error = None
    status_code = 200
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"] or \
                request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid credentials. Please try again."
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))

    return render_template("login.html", error=error), status_code


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("login"))


@app.route("/main")
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
