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

@app.route("/students")
def student():
    # return render_template('products.html',item_name='Try our new product')
    itemvalues=[
        {'name':'Siva','educ':'10th std','age':'15','address':'chathrapatti'},
        {'name':'Ram','educ':'1st yr college','age':'18','address':'Kovilpatti'},
        {'name':'Sakthi','educ':'12th std','age':'17','address':'vadugapatti'},
        {'name':'Saravanan','educ':'8th grade','age':'13','address':'New York'}
    ]
    return render_template('student.html',items=itemvalues)
