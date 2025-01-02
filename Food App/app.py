from flask import Flask,jsonify,request,redirect,url_for,session,render_template,g
import sqlite3
app = Flask(__name__,template_folder='template')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISMYSECRETKEY"

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/addfood")
def addfood():
    return render_template('add_food.html')
@app.route("/day")
def day():
    return render_template('day.html')
if __name__ == "__main__":
    app.run()
    