import pyrebase

def initialize_firebase(config):
    firebase = pyrebase.initialize_app(config)
    return firebase.database()
