# app.py
import sys
sys.path.append('src/')
from flask import Flask, render_template,request
import json
from os import listdir
from utils.question import generate_question 
from flask_frozen import Freezer

app = Flask(__name__,template_folder='templates')
freezer = Freezer(app)

@app.route("/",methods=['GET'])
def index():
    csv_list = listdir("src/data")
    
    return render_template("index.html", csv_list=sorted(csv_list,key=len))

@app.route("/exam/<selectFileName>",methods=['GET'])
def exam(selectFileName):
    data = generate_question(selectFileName)
    print(data[1])
    return render_template("exam.html", selectFileName=selectFileName, questionList=data[0], answerList=data[1])

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building website...")
        freezer.freeze()
    else:
        app.run(debug=True)