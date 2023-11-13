from markupsafe import escape
from flask import Flask, abort, render_template



app = Flask(__name__)
data = "testtekst"

@app.route('/')
@app.route("/index/")
def hello():
    return '<h1>Hello, World!</h1>'

@app.route("/capitalize/<word>/")
def capitalize(word):
    return "<h3>{}<h3>".format(escape(word.capitalize()))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

@app.route("/html/")
def html():
    return render_template("index.html", data=data)