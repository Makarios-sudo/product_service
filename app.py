from flask import Flask
from scr.database.db import initialize_db
from scr.urls.routes import initialize_routes
from flask_restful import Api




app = Flask(__name__)


# database configuration
app.config["MONGODB_SETTINGS"] = MONGO_URI= {
    "db": "product-Service-db",
    "host": "localhost",
    "port": 27017
}

api = Api(app, )

initialize_db(app)
initialize_routes(api)








app.run()