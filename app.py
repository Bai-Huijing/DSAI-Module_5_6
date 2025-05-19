#gemini

from flask import Flask,request,render_template
import google.generativeai as genai
import os
import sqlite3
import datetime

#Configure Gemini
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key = gemini_api_key)

#Configure Gemini Model
model = genai.GenerativeModel("gemini-2.0-flash")

#Configure Flask - contract in the program to point to you as creator
app = Flask(__name__)


first_time = 1

#Flask
@app.route("/", methods = ["GET","POST"]) #decorator
def index():
    return(render_template("index1.html")) #first page

@app.route("/main", methods = ["GET","POST"]) 
def main():
    global first_time
    if first_time ==1:
        q = request.form.get("q")
        print(q)
        t = datetime.datetime.now()
        conn =sqlite3.connect('user.db')
        cursor =conn.cursor()
        cursor.execute("insert into users(name, timestamp) values(?,?)",(q, t))
        conn.commit()
        cursor.close()
        conn.close()
    return(render_template("main.html")) 

#Gemini
@app.route("/gemini", methods = ["GET","POST"]) 
def gemini():
    return(render_template("gemini2.html")) 

@app.route("/gemini_reply", methods = ["GET","POST"]) 
def gemini_reply():
    q = request.form.get("q")
    print(q)
    r = model.generate_content(q)
    return(render_template("gemini_reply3.html",r=r.text)) 

@app.route("/user_log", methods = ["GET","POST"]) 
def user_log():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("select * from users")
    r = ""
    for row in cursor:
        print(row)
        r = r+str(row)
    cursor.close()
    conn.close()
    return(render_template("user_log.html", r=r)) 

@app.route("/delete_log", methods = ["GET","POST"]) 
def delete_log():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("delete from users")
    conn.commit()
    cursor.close()
    conn.close()
    return(render_template("delete_log.html")) 

if __name__=="__main__":
    app.run()
