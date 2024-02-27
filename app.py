from flask import Flask, render_template, request, redirect, url_for
from mongodb import *
# from database import load_products_from_db

app = Flask(__name__)

address = "98 lovell street, worcester, MA 01609"

# @app.route("/")
# def hello():
#   products = load_products_from_db()
#   return render_template("home.html", products=products, contact=address)


@app.route("/home.html")
def home():
  return render_template("home.html", contact=address)


@app.route("/login.html")
def login():
  return render_template("login.html")


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']

    # Check if user already exists
    existing_user = collection.find_one(
        {"$or": [{
            "username": username
        }, {
            "email": email
        }]})
    if existing_user:
      return render_template(
          'login.html')  # Assuming you have a login.html template

    # Proceed with sign-up process if user doesn't exist
    password = request.form['password']
    # Insert user data into the database
    collection.insert_one({
        "username": username,
        "email": email,
        "password": password
    })
    return redirect(url_for(
        'login'))  # Redirect to the login page after successful sign-up
  return render_template('signup.html')


@app.route("/products.html")
def products():
  return render_template("products.html")


@app.route("/contact.html")
def contact():
  return render_template("contact.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
