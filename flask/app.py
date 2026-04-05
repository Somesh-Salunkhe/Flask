# FLASK 

# Import flask
from flask import Flask


#Create an instance of Flask class, which will serve as the WSGI (Web Server Gateway Interface) application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask tutorial"

@app.route("/index")
def welcome_index():
    return "Welcome to the index page."


if __name__ == "__main__":
    app.run(debug=True)


"""
1. Use 'debug =True' under app.run() while in development phase to avoid constant need restart server for every change.
"""