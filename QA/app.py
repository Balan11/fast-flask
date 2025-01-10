from flask import Flask,render_template,redirect,g,url_for

app =Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("login.html")
@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/ask")
def ask():
    return render_template("ask.html")
@app.route("/answer")
def question():
    return render_template("answer.html")