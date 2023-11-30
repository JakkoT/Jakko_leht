
from markupsafe import escape
from flask import Flask, abort, render_template



app = Flask(__name__)

@app.route("/")
def test():
	return render_template("index.html")

@app.route('/download')
def download_file():
    file_path = 'files/test.txt'  # Replace with the actual path to your file
    return send_file(file_path, as_attachment=True)

@app.route('/')
def index():
    return render_template('download.html')
