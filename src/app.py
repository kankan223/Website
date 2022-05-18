from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("new.html")

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)