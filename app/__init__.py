from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap


#import os

#os.environ['FLASK_APP'] = 'microblog.py'   ##


app = Flask(__name__)             # создаём объект приложения как экземпляр класса Flask
app.config.from_object(Config)    # применение конфигурации из класса Config
db = SQLAlchemy(app)              # объект db, представляющий базу данных
migrate = Migrate(app, db)
login = LoginManager(app)         # Flask-Login initialization
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)


from app import routes, models, errors
