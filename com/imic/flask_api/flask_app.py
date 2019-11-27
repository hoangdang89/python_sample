from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return "Home page"

@app.route("/hello")
def hello_world():
    return "hello world!"

@app.route("/login", methods = ['POST'])
def login():
    userName = request.form['userName']
    print('userName: ', userName)
    return "userName: " + userName

@app.route("/user/<userName>")
def user(userName):
    return "Hello: " + userName

@app.route("/post/<int:postId>")
def post(postId):
    return "Some article, id: " + str(postId)

serve(app, host="localhost", port="8080")
