from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()
from twiter.route import index, login


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Flask/main/twiter.db'
    #app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/flask'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
   
    db.init_app(app)
    
    migrate.init_app(app,db)
    app.config['SECRET_KEY'] = '123'
    app.add_url_rule('/index','index',index)
    app.add_url_rule('/login','login',login,methods=['GET','POST'])
    return app


    