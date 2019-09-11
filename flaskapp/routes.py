from flaskapp import app
from flask import render_template
from flaskapp.forms import SignUpForm,LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def sign_up():
    form=SignUpForm()
    return render_template('sign.html',form=form)

@app.route('/login')
def login_user():
    form=LoginForm()
    return render_template('login.html',form=form)