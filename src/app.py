from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import Email, InputRequired, Length

local_server = True  


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class website(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.name}"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ['POST', 'GET'])
def loggin():
    user = website.query.filter_by(name=request.form['name']).first()
    if user:
        if website.password == request.form['password']:
             return render_template("login.html")

    return '<h1>Username doesnot exist</h1>'


@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new = website(name=name, email=email, password=password)
        
        try:
            db.session.add(new)
            db.session.commit()
            return redirect('/')

        except:
            return "There was a problem creating an account"
            #return redirect("/sign_up")
    else:
        #data = website.query.order_by(date)
        return render_template("sign_up.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")



@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)
