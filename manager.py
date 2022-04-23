from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from twiter.models import User

#manage the app or add new command and control the app
from twiter import create_app
app=create_app()
manager = Manager(app)
manager.add_command('db',MigrateCommand)



if __name__ == "__main__":
    
    manager.run()