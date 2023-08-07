"""Python Flask: Hello World!"""
from flask import Flask,render_template
# import the Flask class from the flask module

app = Flask(__name__)
# create the application object


# decorator to tell Flask what URL should trigger our function hello
@app.route("/")
# we can write more than one decorator above a function to bind more than one URL to a function
@app.route("/home")
def hello():
    """define the view using a function, which returns a string"""
    return render_template('index.html') # return a string

@app.route("/products")
def product():
    # return render_template('products.html',item_name='Try our new product')
    return render_template('products.html',items=['ajay','praveen','krishna','suraj'])
