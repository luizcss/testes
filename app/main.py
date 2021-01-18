from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app= Flask(__name__)
@app.route('/')
def index():
  books =[]
  return render_template("home.html",lstbooks=books)