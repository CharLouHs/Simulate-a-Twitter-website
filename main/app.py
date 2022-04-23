""" from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name={'username':'root'}
    posts=[
        {'author':{'name':'Mary'},'body':27}
        

    ]
    return render_template('index.html',name=name,posts=posts)

@app.route("/test")
def test():
    return "<p>test ! </p>"

if __name__=="__main__":
    app.run() """