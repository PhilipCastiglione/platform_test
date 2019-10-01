import os

class Config(object):
    DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DEFAULT_DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
