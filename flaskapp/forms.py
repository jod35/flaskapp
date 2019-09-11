from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo


class SignUpForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired(),Length(max=50)])
    email=StringField("Email",validators=[DataRequired(),Length(max=50)])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo('confirm')])
    confirm=PasswordField("Confirm Password",validators=[DataRequired()])
    
    submit=SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email=StringField("Email")
    password=PasswordField("Password")
    submit=SubmitField("Log In")

