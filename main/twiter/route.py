from flask import Flask, render_template,redirect, url_for,request
from twiter.forms import LoginForm
from flask_login import login_user,current_user, logout_user,login_required
from twiter.models import User,Tweet
from twiter import db

@login_required
def index():
    name={'username':current_user.username}
    posts=[
        {'author':{'name':'Mary'},'body':27}
        

    ]
    return render_template('index.html',posts=posts)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
   
    if form.validate_on_submit():
    #    msg=('username={},password={},remem_me={}'.format (
    #        form.username.data,
     #       form.password.data,
    #        form.remem_me.data
    #    ))
    #    print(msg)
        u=User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u,remember=form.remem_me.data)
        next_page=request.args.get('next')
        if next_page:
            return redirect(next_page)
        
        return redirect(url_for('index'))
    else:
        print(form.errors)
    
    return render_template('login.html',title='Login',form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))