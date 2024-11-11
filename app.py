from flask import Flask #网页创建包
from flask import render_template,request

app = Flask("__name__")#

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__": ## __is for system to use
    app.run()