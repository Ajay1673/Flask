"""Python Flask: Hello World!"""
from flask import Flask,render_template
from sqlalchemy import create_engine
# import the Flask class from the flask module
engine = create_engine("mysql+pymysql://root:ajayKrishna03@localhost:3306/college")
app = Flask(__name__) # create the application object

# decorator to tell Flask what URL should trigger our function home()
# we can write more than one decorator above a function to bind more than one URL to a function
@app.route("/home")
def home():
    """define the view using a function, which returns a string"""
    return render_template('home.html') # return a string

@app.route("/students")
def student():
    # return render_template('products.html',item_name='Try our new product')
    itemvalues=[
        {'name':'Siva','email':'2015060@nec.edu.in','phone':'9600235322','mark1':'80','mark2':'82','cgpa':'8.2'},
        {'name':'Ram','email':'2015058@nec.edu.in','phone':'9687645632','mark1':'70','mark2':'74','cgpa':'7.5'},
        {'name':'Sakthi','email':'2015063@nec.edu.in','phone':'9623646212','mark1':'75','mark2':'87','cgpa':'9'},
        {'name':'Saravanan','email':'2015062@nec.edu.in','phone':'9609876570','mark1':'85','mark2':'88','cgpa':'8.5'}
    ]
    return render_template('student.html',items=itemvalues)
