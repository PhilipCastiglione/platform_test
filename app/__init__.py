import os
from dotenv import load_dotenv
from flask import Flask
from app.config import Config, TestConfig
from app.clients import RedisClient
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from rq import Queue

load_dotenv()

app = Flask(__name__)

if os.environ.get('TESTING'):
    app.config.from_object(TestConfig)
else:
    app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

redis = RedisClient()

battle_queue = Queue(connection=redis.connection)

from app import routes, models
