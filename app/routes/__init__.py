from flask import Blueprint

# Import blueprints from individual route modules
from .registration import registration_bp
from .payment import payment_bp
from .admin import admin_bp
from .webhook import webhook_bp

def register_blueprints(app):
    """
    Function to register all blueprints with the Flask app
    """
    app.register_blueprint(registration_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(webhook_bp)
