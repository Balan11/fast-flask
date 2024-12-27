from flask import Flask,jsonify,request,redirect,url_for,session
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISMYSECRETKEY"

@app.route("/")
def index():
    session.pop("name",None)
    return "<h1>Hello ! World !!</h1>"
@app.route("/home",methods=['POST','GET'],defaults={'name':'default'})
@app.route("/home/<name>",methods=['POST','GET'])
def home(name):
    session['name'] =  name
    return "<h1>hi {} this is your home page  </h1>".format(name)
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
        return '''<form method="POST" action='/theform'>
    <input type="text" name="name">
    <input type="text" name ="location">
    <button type="submit"> save</button>

    </form>
    '''    
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
if __name__ == "__main__":
    app.run()
    