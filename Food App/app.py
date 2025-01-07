from flask import Flask,jsonify,request,redirect,url_for,session,render_template,g
import sqlite3,datetime
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
        db=get_db()
        cur=db.execute("select id,entry_date from log_date")
        results= cur.fetchall()
        finalresult=[]
        for i in results:
            if i['entry_date']!='':
                d={}
                d['id'] =i['id']
                d['entry_date'] = datetime.datetime.strptime(i['entry_date'],"%Y-%m-%d").strftime("%B %d,%Y")
                finalresult.append(d)
        return render_template('home.html',results=finalresult)
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
@app.route("/newday",methods=['POST'])
def newday():
    
    if request.method=="POST":
        print("inside")
        db = get_db()
        db.execute("insert into log_date (entry_date)values(?)",[request.form['new_day']])
        db.commit()
        return redirect('day')
@app.route("/view/<date>",methods=['GET','POST'])
def view(date):
    mydate = datetime.datetime.strptime(date,"%Y%m%d").strftime("%Y-%m-%d")
    db = get_db()
    cur =db.execute("select id,entry_date from  log_date where entry_date=?",[mydate])
    food_day = db.execute("select food.name,food.protein,food.carbohydrate,food.calories,food.fat from log_date join food_date on food_date.log_date_id = log_date.id join food on food.id = food_date.food_id")
    all_food=food_day.fetchall()
    result = cur.fetchone()
    if request.method =="POST":
        db.execute("insert into food_date(food_id,log_date_id)values(?,?)",[request.form['foodselect'],result['id']])
        db.commit()
        return f"<h1>request {request.form['foodselect']} </h1>"
    food=db.execute("select id,name,protein,carbohydrate,calories,fat from food")
    myfood = food.fetchall()
    mydate= datetime.datetime.strptime(result['entry_date'],'%Y-%m-%d').strftime("%B %d,%Y")  
    return render_template('day.html',result=mydate,myfood=myfood,date=date,food_day=all_food)

if __name__ == "__main__":
    app.run()
    