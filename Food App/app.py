from flask import Flask,jsonify,request,redirect,url_for,session,render_template,g
import sqlite3
app = Flask(__name__,template_folder='template')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISMYSECRETKEY"
# ---------------------- db session start ----------------
def connect_db():
    sql=sqlite3.connect("foodappDb.db")
    sql.row_factory = sqlite3.Row
    return sql
def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

def close_db():
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
#------------------------------- db session close
@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template('home.html')
    else:
      return render_template('home.html')
@app.route("/addfood",methods=['GET','POST'])
def addfood():
    if request.method=='GET':
        db=get_db()
        curr=db.execute("select name,protein,carbohydrate,calories,fat from food")
        result = curr.fetchall()
        print(result)
        return render_template('add_food.html',result=result)
    if request.method=="POST":
        db=get_db()
        db.execute("insert into food(name,protein,carbohydrate,calories,fat)values(?,?,?,?,?)",[request.form['food-name'],request.form['protein'],request.form['carbohydrates'],request.form['fat'],request.form['fat']])
        db.commit()
        return render_template('add_food.html')
@app.route("/day",methods=['GET','POST'])
def day():
    if request.method=="GET":
        return render_template('day.html')

@app.route("/newday",method=['POST'])
def newday():
    if request.method=="POST":
        print(request.form['new_day'])
        return redirect('day')

if __name__ == "__main__":
    app.run()
    