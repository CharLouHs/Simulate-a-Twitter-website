from flask import Flask, render_template,redirect, url_for,request,abort,current_app
from twiter.forms import EditProfileForm
from twiter.forms import LoginForm,RegisterForm,TweetForm
from flask_login import login_user,current_user, logout_user,login_required
from twiter.models import User,Tweet
from twiter import db

@login_required
def index():
    form=TweetForm()
    if form.validate_on_submit():
        t = Tweet(body=form.tweet.data,author=current_user)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    page_num=int(request.args.get('page') or 1)
    tweets=current_user.own_and_followed_tweets().paginate(page=page_num, per_page=current_app.config['TWEET_PER_PAGE'], error_out=False)
   
    next_url=url_for('index',page=tweets.next_num) if tweets.has_next else None
    
    prev_url = url_for('index',page=tweets.prev_num) if tweets.has_prev else None
    return render_template('index.html',tweets=tweets.items,form=form,
            next_url=next_url,prev_url=prev_url)

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

def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title="Registration",form=form)

@login_required
def user(username):
    u=User.query.filter_by(username=username).first()
    if u is None:
        abort(404)
    tweets=u.tweets.order_by(Tweet.create_time.desc())
    if request.method=='POST':
        if request.form['request_button'] == "Follow":
            current_user.follow(u)
            db.session.commit()
            print("click follow")
        else:
            current_user.unfollow(u)
            db.session.commit()
            print("click unfollow")

    page_num=int(request.args.get('page') or 1)
    tweets=current_user.own_and_followed_tweets().paginate(page=page_num, per_page=current_app.config['TWEET_PER_PAGE'], error_out=False)
   
    next_url=url_for('profile',page=tweets.next_num,username=username) if tweets.has_next else None
    
    prev_url = url_for('profile',page=tweets.prev_num,username=username) if tweets.has_prev else None
    return render_template('user.html',title='Profile',tweets=tweets.items,user=u,next_url=next_url,prev_url=prev_url)

def pageNotFound(e):
    return render_template('404.html',title='404'),404

def edit_profile():
    form=EditProfileForm()
    if request.method == 'GET':
        form.about_me.data=current_user.about_me
    if form.validate_on_submit():
        current_user.about_me=form.about_me.data
        db.session.commit()
        return redirect(url_for('profile',username=current_user.username))
    return render_template('edit_profile.html',form=form)