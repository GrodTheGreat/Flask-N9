from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(import_name=__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app=app)

    from views import register_routes  # The import is here to prevent circular imports
    register_routes(app=app, db=db)

    migrate = Migrate(app=app, db=db)

    return app