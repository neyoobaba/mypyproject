from flask import Flask, render_template, url_for
app = Flask(__name__)
# print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def my_homep():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def my_works():
    return render_template('works.html')

@app.route('/contact.html')
def my_contact():
    return render_template('contact.html')

@app.route('/work.html')
def my_work():
    return render_template('work.html')

@app.route('/components.html')
def my_components():
    return render_template('components.html')