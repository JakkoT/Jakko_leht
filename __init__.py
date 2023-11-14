
from markupsafe import escape
from flask import Flask, abort, render_template



app = Flask(__name__)

@app.route("/")
def test():
	return render_template("index.html")
