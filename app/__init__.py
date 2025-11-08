from flask import Flask
from dotenv import load_dotenv
from app.routes import main

import os

def create_app():
  load_dotenv()
  templates_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))

  app = Flask(__name__, template_folder=templates_path)

  app.secret_key = os.getenv("SECRET_KEY", "SuPeRsecret")

  app.register_blueprint(main)

  return app


