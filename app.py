from flask import Flask, render_template

app = Flask(__name__)

address = "98 lovell street, worcester, MA 01609"


@app.route("/")
def hello():
  return render_template("home.html", contact=address)


@app.route("/login")
def login():
  return render_template("login.html")


@app.route("/signup.html")
def signup():
  return render_template("signup.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
