from flaskapp import app,db
from flaskapp.models import User
from flask import render_template,request,flash,redirect
from flaskapp.forms import SignUpForm,LoginForm
from flask_bcrypt import Bcrypt

bcypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET', 'POST'])
def sign_up():
    form=SignUpForm()
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        passwd=bcypt.generate_password_hash(password)
        new_user=User(name=name,email=email,password=passwd)
        db.session.add(new_user)
        db.session.commit()
        flash('New User Added Successfully,You can Now log in')
        return redirect('/signup')
    return render_template('sign.html',form=form)

@app.route('/login')
def login_user():
    form=LoginForm()
    return render_template('login.html',form=form)