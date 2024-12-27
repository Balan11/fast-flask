from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello ! World !!</h1>"
@app.route("/home",methods=['POST','GET'],defaults={'name':'default'})
@app.route("/home/<name>",methods=['POST','GET'])
def home(name):
    return "<h1>hi {} this is your home page  </h1>".format(name)
@app.route("/json")
def json():
    return jsonify({'key':'value',
                    'key2':[1,2,2],
                    'key3':"wait",
                    })
    
@app.route("/query")
def query():
    name = request.args.get('name')
    location = request.args.get("location")
    return "<h1>Hi {} and you coming from {} .You Are the Query page!</h1>".format(name,location)

@app.route("/theform",methods=['GET',"POST"])
def theform():
    return '''<form method="POST" action='/process'>
<input type="text" name="name">
<input type="text" name ="location">
<button type="submit"> save</button>

</form>
'''
@app.route("/process",methods=["POST"])
def process():
    name = request.form['name']
    location = request.form['location']
    return "<h1> Hello {} are you from {} . ok enjoy".format(name,location)
if __name__ == "__main__":
    app.run(debug=True)
    