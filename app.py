from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,Abhay Singh Tomar !</p>"

@app.route("/about")
def about():
    return "<p>I'm Btech Student , pursuing from PSIT Kanpur Looking Forward to Explore New technologies and Much more!</p>"

if __name__ =="__main__":
    app.run(debug=True,port=8000)