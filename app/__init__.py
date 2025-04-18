from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)


    from app.routes import router
    app.register_blueprint(router)


    return app