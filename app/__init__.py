from flask import Flask
from app.routes.registration import registration_bp
from app.routes.payment import payment_bp
from app.routes.admin import admin_bp
from app.routes.webhook import webhook_bp
from app.utils.firebase import initialize_firebase

def create_app():
    app = Flask(__name__)
    app.register_blueprint(registration_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(webhook_bp)

    # Initialize Firebase
    firebase_config = {
      #get from firebase configuration in your account settings
      }

    initialize_firebase(firebase_config)

    return app
