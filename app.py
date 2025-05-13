#gemini

from flask import Flask,request,render_template
import google.generativeai as genai

genai.configure(api_key = "AIzaSyABvlD0P6MRi2qNNCJzasbK1l3tVhE70iA")
model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__) #contract in the program to point to you as creator

@app.route("/", methods = ["GET","POST"]) #decorator
def index():
    return(render_template("index1.html")) #first page

@app.route("/gemini", methods = ["GET","POST"]) 
def gemini():
    return(render_template("gemini2.html")) 

@app.route("/gemini_reply", methods = ["GET","POST"]) 
def gemini_reply():
    q = request.form.get("q")
    print(q)
    r = model.generate_content(q)
    return(render_template("gemini_reply3.html",r=r.text)) 

if __name__=="__main__":
    app.run()
