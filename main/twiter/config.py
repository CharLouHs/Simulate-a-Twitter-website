import os
config_path=os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL",'sqlite:///'+os.path.join(config_path,'twiter.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='abc123'
    TWEET_PER_PAGE=2


