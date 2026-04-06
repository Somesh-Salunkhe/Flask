### Jinja2 template engine for Flask

'''
This script demonstrates three different concepts:
1. Building dynamic URLs
2. Variable rule
3. Jinja2 Template Engine
'''

# FLASK 

# Import flask
from flask import Flask
from flask import render_template  # Used to redirect to html scripts outside this file
from flask import request # Used to capture request GET or POST
from flask import redirect # Used to redirect to other urls
from flask import url_for # Used to generate dynamic urls for the application

#Create an instance of Flask class, which will serve as the WSGI (Web Server Gateway Interface) application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask tutorial</H1></html>"

@app.route("/index", methods=['GET'])
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

# Variable rule

@app.route('/success/<int:score>')
def success(score):
    #return f'Your score is {score}'
    return "Your score is " + str(score) # We have to typecast score to string to concatenate it with other string

"""
Jinja2 Template Engine has several ways to generate dynamic content in HTML templates.
1. {{ }}: Used to print the value of a variable or expression in the template.
2. {% %}: Used for control structures like loops and conditionals.
3. {# #}: Used for comments in the template, which will not be rendered in the final output.
"""

# Using Jinja2 Template Engine to generate dynamic content in HTML templates

#  {{ }} Method
@app.route('/result/<int:score>')
def result(score):
    result = ''
    if score >= 50:
        result = "You have passed"
    else:
        result = "You have failed"

    return render_template('result.html', result = result) # We can pass variables to html script as well, here we are passing result variable to result.html script

# {% %} Method
@app.route('/result_2/<int:score>')
def result_2(score):
    result = ''
    if score >= 50:
        result = "You have passed"
    else:
        result = "You have failed"
    
    exp = {"score": score, "result": result} # Dictonary to store variables to pass to html script

    return render_template('result2.html', result = exp) # We can pass variables to html script as well, here we are passing result variable to result.html script

# {% %} If Method
@app.route('/result_3/<int:score>')
def result_3(score):
    return render_template('result3.html', score = score) # We can pass variables to html script as well, here we are passing result variable to result.html script


'''
Building Dynamic URLs: Flask allows us to create dynamic URLs by using variable rules in the route. 
'''
# Get score
@app.route('/submit2', methods = ['POST','GET'])
def submit2():
    total_score = 0
    if request.method == 'POST':
        score1 = float(request.form['science'])
        score2 = float(request.form['maths'])
        score3 = float(request.form['c'])
        score4 = float(request.form['datascience'])
        total_score = (score1 + score2 + score3 + score4)/4
        return redirect(url_for('result_2', score = total_score)) # We can redirect to other urls as well, here we are redirecting to result_2 url and passing score variable to it
    return render_template('getscore.html')
  


if __name__ == "__main__":
    app.run(debug=True)


"""
1. Use 'debug =True' under app.run() while in development phase to avoid constant need restart server for every change.
"""