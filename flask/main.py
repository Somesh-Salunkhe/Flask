# FLASK 

# Import flask
from flask import Flask
from flask import render_template  # Used to redirect to html scripts outside this file


#Create an instance of Flask class, which will serve as the WSGI (Web Server Gateway Interface) application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask tutorial</H1></html>"

@app.route("/index")
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)


"""
1. Use 'debug =True' under app.run() while in development phase to avoid constant need restart server for every change.
"""