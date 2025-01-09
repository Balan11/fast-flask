from flask import Flask,render_template,redirect,g,url_for

app =Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return render_template('')