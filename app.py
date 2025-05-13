#gemini

from flask import Flask,request,render_template

app = Flask(__name__) #contract in the program to point to you as creator

@app.route("/", methods = ["GET","POST"]) #decorator
def index():
    return(render_template("index.html")) #first page

if __name__=="__main__":
    app.run()
