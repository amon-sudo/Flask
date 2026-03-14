from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.permanent_session_lifetime = timedelta(minutes=5)



db = SQLAlchemy(app)
class users(db.model):
    _id =db.Column("id", db.Integer, primary_key=True)
    
    
    
# route.
@app.route("/")
# defining the pages
def home():
    return render_template("index.html" )

@app.route("/login", methods= ["POST", "GET"])

def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nam"]
        session["user"] = user
        flash("Login succesful!!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("already logged!!")
            return redirect(url_for("user"))
            
        return render_template("login.html")


@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("email was saved!!")
           
            
        else:
            
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email)
    else:
        flash("you are not logged in!!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are logged out successful")
    session.pop("user", None)
    session.pop("email", None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)