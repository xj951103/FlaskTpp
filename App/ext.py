from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache


db = SQLAlchemy()
migrate = Migrate()

cache = Cache(
    config={

    }
)

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
