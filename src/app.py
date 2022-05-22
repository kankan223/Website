from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import Model, SQLAlchemy
#import sqlalchemy as sa
#from sqlalchemy.ext.declarative import declared_attr, has_inherited_table
from datetime import datetime
import json
import os


#class IdModel(Model):
#    @declared_attr
#   def id(cls):
#       for base in cls.__mro__[1:-1]:
#           if getattr(base, '__table__', None) is not None:
#               type = sa.ForeignKey(base.id)
#               break
#       else:
#           type = sa.Integer

#       return sa.Column(type, primary_key=True)

#db = SQLAlchemy(model_class=IdModel)

#class User(db.Model):
#   name = db.Column(db.String)

#class Employee(User):
#   title = db.Column(db.String)

#with open('./templates/config.json', 'r') as c:
    #params = json.load(c)["params"]

local_server = True#params['local_serer']    


app = Flask(__name__)
#if(local_server):
 #   app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
#else:
 #   app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class website(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

    



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login",  methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("index.html")
    else:
        return render_template("login.html")

@app.route("/sign_up", methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new = website(name=name, email=email, password=password)


        try:
            db.session.add(new)
            db.session.commit
            return redirect("/")
        except:
            return "There was a problem creating an account"
            return redirect("/sign_up")
    else:
        return render_template("sign_up.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/login_val", methods=['POST', 'GET'])
def login_val():
    email=request.form.get('email')
    username=request.form.get('username')
    password=request.form.get('password')
    return redirect("/")


@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)