from flask import Flask #import the Flask class from the flask module

app = Flask(__name__) #create the application object

@app.route("/") #decorator to tell Flask what URL should trigger our function hello 
def hello(): #define the view using a function, which returns a string
    return '<div>Welcome to Python Flask<p>My first Page</p></div>' #return a string
    
        


