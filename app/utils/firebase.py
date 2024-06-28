import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase(firebase_config):
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'create realtime database in firebase and copy and paste the link'
    })

def get_all_users():
    ref = db.reference('users')
    return ref.get()

def add_user(user_data):
    ref = db.reference('users')
    ref.push(user_data)

def store_payment_details(payment_data):
    ref = db.reference('payments')
    ref.push(payment_data)

def get_all_payment_details():
    ref = db.reference('payments')
    return ref.get()
