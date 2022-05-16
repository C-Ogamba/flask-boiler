from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()


def createapp(config_class=Config):
    """factory function"""

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app,db)

    """registering blueprints"""
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.errors import errors as error_bp
    app.register_blueprint(error_bp)
    

    return app