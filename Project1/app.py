from flask import Flask,jsonify,request,redirect,url_for,session,render_template,g
import sqlite3
app = Flask(__name__,template_folder='template')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISMYSECRETKEY"
DATABASE_PATH = 'database.db'

def connect_db():
    sql=sqlite3.connect(DATABASE_PATH)
    sql.row_factory = sqlite3.Row
    return sql
def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


@app.route("/")
def index():
    session.pop("name",None)
    return "<h1>Hello ! World !!</h1>"
@app.route("/home",methods=['POST','GET'],defaults={'name':'default'})
@app.route("/home/<name>",methods=['POST','GET'])
def home(name):
    session['name'] =  name
    return render_template("home.html",name=name)
@app.route("/json")
def json():
    name='nothing'
    if 'name' in session:
    # mylist=[1,2,3,4,5]
        name=session['name']    
    return jsonify({'key':'value',
                    'key2':[1,2,2],
                    'key3':"wait",
                    'name':name
                    })
    
@app.route("/query")
def query():
    name = request.args.get('name')
    location = request.args.get("location")
    return "<h1>Hi {} and you coming from {} .You Are the Query page!</h1>".format(name,location)

@app.route("/theform",methods=['GET','POST'])
def theform():
    if request.method=="GET":
        return render_template('forms.html')
    else:
        print("else")
        name = request.form['name']
        return redirect(url_for("home",name=name))
           
@app.route("/process",methods=["POST"])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1> Hello {} are you from {} . ok enjoy".format(name,location)

@app.route("/processjson",methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    
    return jsonify({'result':"sucess",
                    'name':name,
                    'location':location,
                    'randomlist':randomlist[1]})

# db work
@app.route("/viewresults")
def viewresults():
    db  = get_db()
    print(db)
    cur=db.execute("select id,name,location  from user ")

    results = cur.fetchall()
    return "<h1>Id {} name{} location {}</h1>".format(results[0]['id'],results[0]['name'],results[0]['location'])
if __name__ == "__main__":
    app.run()
    