from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app(config_object='app.config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize components
    from app.utils.logger import setup_logging
    setup_logging(app)

    # Register blueprints
    from app.api import main_blueprint
    app.register_blueprint(main_blueprint)


    return app