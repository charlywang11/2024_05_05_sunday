from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>我的第一個網站</h1>"