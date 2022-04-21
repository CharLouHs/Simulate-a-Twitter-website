from flask import Flask
from twiter.route import index, login


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123'
    app.add_url_rule('/index','index',index)
    app.add_url_rule('/login','login',login,methods=['GET','POST'])
    return app


    