from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

class OpenInit:
    def app(self):
        app = Flask(__name__)
        return app
    def models(self):
        DB = self.app()
        DB.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Wjx20210601@120.79.136.233:3306/MySQL"
        Bootstrap(DB)
        db = SQLAlchemy(DB)
        return db