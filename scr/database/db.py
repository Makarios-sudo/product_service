from flask_mongoengine import MongoEngine

from pymongo import monitoring

from scr.utility.log import CommandLogger

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)


monitoring.register(CommandLogger())

