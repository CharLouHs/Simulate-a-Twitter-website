from flask import Flask, render_template,redirect, url_for
from twiter.forms import LoginForm


def index():
    name={'username':'root'}
    posts=[
        {'author':{'name':'Mary'},'body':27}
        

    ]
    return render_template('index.html',name=name,posts=posts)

def login():
    form=LoginForm(WTF_CSRF_ENABLED = False)
   
    if form.validate_on_submit():
        msg=('username={},password={},remem_me={}'.format (
            form.username.data,
            form.password.data,
            form.remem_me.data
        ))
        print(msg)
        return redirect(url_for('index'))
    else:
        print(form.errors)
    
    return render_template('login.html',title='Login',form=form)
