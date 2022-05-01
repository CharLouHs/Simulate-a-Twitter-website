from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
    
from wtforms.validators import DataRequired, email_validator,Email,EqualTo,ValidationError,Length
from twiter.models import User

class LoginForm(FlaskForm):
    class Meta:
        csrf= False
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remem_me=BooleanField("Remember me")
    submit=SubmitField('Submit')

class RegisterForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email Address",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    password2=PasswordField(
        "Password Repeat",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('please use different username')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('please use different email address')   

class EditProfileForm(FlaskForm):
    about_me=TextAreaField('About me',validators=[Length(min=0,max=120)])
    submit = SubmitField('Save')

class TweetForm(FlaskForm):
    tweet=TextAreaField('Tweet',validators=[DataRequired(),Length(min=1,max=140)])
    submit = SubmitField('Tweet')

