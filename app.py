# api cannoy appear in cloud

from flask import Flask #网页创建包
from flask import render_template,request
import textblob
import google.generativeai as genai
import os
#api='AIzaSyC3PgQn6g619clqC5CZd_CymqrGq7O2iC0'
api=os.getenv("makersuite")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask("__name__")#

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name=request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q =request.form.get("q") # "q"是front end(html), q=的是backend(python)
    r=textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r))

@app.route("/genAI",methods=["GET","POST"])
def GenAI():
    return(render_template("genAI.html"))

@app.route("/genAI_result",methods=["GET","POST"])
def genAI_result():
    q =request.form.get("q")
    r=model.generate_content(q)
    r=r.candidates[0].content.parts[0].text
    return(render_template("genAI_result.html",r=r))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))
    
if __name__ == "__main__": ## __is for system to use
    app.run()
