
from markupsafe import escape
from flask import Flask, abort, render_template, send_file, url_for, redirect



app = Flask(__name__)

@app.route("/")
def test():
	return render_template("index.html")

@app.route('/download')
def download_file():
    file_path = 'files/test.txt'  # Replace with the actual path to your file
    return send_file(file_path, as_attachment=True)

@app.route('/raspberry')
def raspberry():
    return render_template('raspberry.html')

@app.route('/PiPDF')
def raspberryPiPDF():
    return render_template('downloadPiPDF.html')
