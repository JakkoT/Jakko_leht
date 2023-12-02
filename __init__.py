
from markupsafe import escape
from flask import Flask, abort, render_template, send_file, url_for, redirect



app = Flask(__name__)

@app.route("/")
def test():
	return render_template("index.html")

@app.route('/download')
def download_file():
    file_path = 'files/test.txt'  
    return send_file(file_path, as_attachment=True)

@app.route('/raspberry')
def raspberry():
    return render_template('raspberry.html')

@app.route('/PiPDF')
def raspberryPiPDF():
    return render_template('downloadPiPDF.html')

@app.route('/PiPic')
def piPic():
    return render_template('piPic.html')

@app.route('/downloadCV')
def download_CV():
    file_path = 'files/CV.txt'  
    return send_file(file_path, as_attachment=True)

@app.route('/kontakt')
def kontakt():
     return render_template('kontakt.html')