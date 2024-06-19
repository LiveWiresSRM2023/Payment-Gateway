from flask import Flask
from app.utils.firebase import initialize_firebase
from app.config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize Firebase
    app.config['FIREBASE'] = initialize_firebase(app.config['FIREBASE_CONFIG'])

    # Import and register Blueprints
    from app.routes.registration import registration_bp
    from app.routes.payment import payment_bp
    from app.routes.admin import admin_bp
    from app.routes.webhook import webhook_bp

    app.register_blueprint(registration_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(webhook_bp)

    return app
