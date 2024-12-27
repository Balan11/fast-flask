from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello ! World !!</h1>"
@app.route("/home")
def home():
    return "<h1>home page</h1>"
@app.route("/json")
def json():
    return jsonify({'key':'value',
                    'key2':[1,2,2],
                    'key3':"wait",
                    })
if __name__ == "__main__":
    app.run(debug=True)
    