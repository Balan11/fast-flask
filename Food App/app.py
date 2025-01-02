from flask import Flask,jsonify,request,redirect,url_for,session,render_template,g
import sqlite3
app = Flask(__name__,template_folder='template')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISMYSECRETKEY"

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template('home.html')
    else:
      return render_template('home.html')
@app.route("/addfood",methods=['GET','POST'])
def addfood():
    if request.method=='GET':
        return render_template('add_food.html')
    else:
        return render_template('add_food.html')
@app.route("/day",methods=['GET','POST'])
def day():
    if request.method=="GET":
        return render_template('day.html')
    else:
         return render_template('day.html')
if __name__ == "__main__":
    app.run()
    