from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method=="GET":
        return "you didnt fill the form out"
    else:
        userData=dict(request.form)
        sentence=userData["sentence"]
        sentence= model.count(sentence)
        characters = sentence
        sentence= model.nums(sentence)
        return render_template("result.html", sentence = sentence, characters = characters)
        