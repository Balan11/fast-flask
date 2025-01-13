from flask import Flask,render_template,redirect,g,url_for,request,session
from werkzeug.security import check_password_hash,generate_password_hash
from database import get_db,connect_db,close_db
import os
from migratedb import conn
from emailconfig import *

app =Flask(__name__,template_folder='template')
mail = Mail(app)
mail.init_app(app)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] =os.urandom(24)

def get_current_user():
    user=None
    if 'user' in session:
        user = session['user']  
    return user

@app.route("/")
def index():
    user=None

    if 'user' in session :
        user= session['user']
    return render_template('index.html',user=user)

@app.route("/register",methods=['GET',"POST"])
def register():
    if request.method=="POST":
        db=get_db()
        hashed_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256') #method='pbkdf2:sha256'
        db.execute("insert into user (name,password,expert,admin) values(?,?,?,?)",[request.form['username'],hashed_password,0,0])
        db.commit()
        return f"<h1> UserName {request.form['username']}  created !</h1>"
    if request.method=="GET":
        return render_template("register.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":
        print(request.form['username'],request.form['password'])
        db=get_db()
        correntUser=db.execute("select id,name,password from user where name=?",[request.form['username']])
        username = correntUser.fetchone()
        print(username['password'])
        if check_password_hash(username['password'],request.form['password']):
            session['user']=username['name']
            return """<h1>oh My god !! login successfully ! 
            <form method="POST" action="/logout">
            <button type="submit">Logout</button>
            </form>
        </h1>"""
        else: 
            return "<h1>oh My god !! you faild to  login ! Try again </h1>"
            
    return render_template("login.html")

@app.route("/logout",methods=['POST'])
def logout():
    session.pop("user",None)
    return redirect("/")
@app.route("/question")
def question():
    return render_template("question.html")
@app.route("/ask")
def ask():
    return render_template("ask.html")
@app.route("/answer")
def answer():
    return render_template("answer.html")

if __name__ == "__main__":
    app.run()