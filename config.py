from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config:
    # This db will be used for saving input from users and logging acess to web server.
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:#INSERT_PASSWORD_HERE#@127.0.0.1:3306/mydb'
    print('db configured')