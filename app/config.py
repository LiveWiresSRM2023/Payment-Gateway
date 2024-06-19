import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    FIREBASE_CONFIG = {
        "apiKey": os.environ.get('FIREBASE_API_KEY'),
        "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN'),
        "databaseURL": os.environ.get('FIREBASE_DATABASE_URL'),
        "storageBucket": os.environ.get('FIREBASE_STORAGE_BUCKET')
    }
    CASHFREE_CLIENT_ID = os.environ.get('CASHFREE_CLIENT_ID')
    CASHFREE_CLIENT_SECRET = os.environ.get('CASHFREE_CLIENT_SECRET')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
