from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    class Meta:
        csrf= False
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remem_me=BooleanField("Remember me")
    submit=SubmitField('Submit')