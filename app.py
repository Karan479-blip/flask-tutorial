from flask import Flask 
app=Flask(__name__)


@app.route("/")
def welcome():
    return "hello world"


app.route("/home")
def home():
    return "this is home pagerun"

#from controller import product_controller,user_controller
from controller import *