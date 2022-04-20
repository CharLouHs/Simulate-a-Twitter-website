from flask_script import Manager

#manage the app or add new command and control the app
from twiter import create_app
app=create_app()
manager = Manager(app)



if __name__ == "__main__":
    manager.run()