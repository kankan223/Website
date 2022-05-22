from flask import Flask, render_template, request, redirect, flash, Blueprint
from flask_sqlalchemy import Model, SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash
import json
import os
from flask_login import login_user, login_required, logout_user, current_user


local_server = True  #params['local_serer']    


app = Flask(__name__)
#if(local_server):
 #   app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
#else:
 #   app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class website(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        #return '<Name %r>' % self.sno
        return f"{self.sno} - {self.name}"

auth =  Blueprint('auth', __name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def loggin():
    return render_template("login.html")


#@auth.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        name = request.form.get('name')
#        email = request.form.get('email')
#        password = request.form.get('password')

#        website = website.query.filter_by(name=name).first()
#        website = website.query.filter_by(email=email).first()
#        if website:
#            if check_password_hash(website.password, password):
#                flash('Logged in seccuessfully!', category='success')
#                login_user(website, remember=True)
#                return redirect('/')
#            else:
#                flash('Incorrect password, try again', category='error')
#        else:
#            #flash('Email does not exist', category='error')

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