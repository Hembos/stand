from flask import Flask, render_template, request, redirect, send_file
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect('database.db') 
connect.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, email TEXT, city TEXT, country TEXT, phone TEXT)') 

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email'] 
        city = request.form['city'] 
        country = request.form['country'] 
        phone = request.form['phone']
        
        with sqlite3.connect("database.db") as users: 
            cursor = users.cursor() 
            cursor.execute("INSERT INTO Users \
            (name,email,city,country,phone) VALUES (?,?,?,?,?)", 
                            (name, email, city, country, phone)) 
            users.commit() 
        
        return redirect(f"/profile/{name}")
    else:
        return render_template("signup.html")

@app.route("/profile/<username>")
def profile(username: str):
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor() 
    cursor.execute(f"SELECT * FROM Users WHERE name='{username}'") 
  
    data = cursor.fetchone() 
    return render_template("profile.html", data=data) 

@app.route("/download", methods=['GET'])
def file():
    filename = request.args.get('file')
    return send_file(f"static/{filename}") 

if __name__=='__main__':
  app.run(debug=True)