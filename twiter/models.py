from twiter import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))

    def __repr__(self) :
        return 'id={}, username={}, email={},password_hash={}'.format(
            self.id,self.username,self.email,self.password_hash
        )
