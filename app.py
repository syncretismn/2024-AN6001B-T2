from flask import Flask #网页创建包
from flask import render_template,request

app = Flask("__name__")#

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name=request.form.get("q")
    return(render_template("main.html"))

if __name__ == "__main__": ## __is for system to use
    app.run()