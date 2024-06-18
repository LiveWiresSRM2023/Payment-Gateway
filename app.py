from flask import Flask, render_template, request, redirect, jsonify
import pyrebase
import requests
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import firebase_admin
from firebase_admin import credentials


app = Flask(__name__)

Config = {
  'apiKey': "AIzaSyCGb4XZaWONndWTmQZTQjeJCDj0-ch4mHk",
  'authDomain': "payment-gateway-f5576.firebaseapp.com",
  'databaseURL': "https://payment-gateway-f5576-default-rtdb.firebaseio.com",
  'projectId': "payment-gateway-f5576",
  'storageBucket': "payment-gateway-f5576.appspot.com",
  'messagingSenderId': "461167654954",
  'appId': "1:461167654954:web:d930df69629fea58f1eb53",
  'measurementId': "G-KN2JBDFSGQ"
};

#Initialize Firebase

firebase = pyrebase.initialize_app(Config)
db = firebase.database()

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        data = {"name": name, "email": email, "phone": phone}
        db.child("registrations").push(data)
        return redirect('/payment')
    return render_template('register.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        payload = {
            "orderId": "order0001",
            "orderAmount": "100",
            "orderCurrency": "INR",
            "customerName": "John Doe",
            "customerPhone": "9876543210",
            "customerEmail": "john@example.com"
        }
        headers = {
            "Content-Type": "application/json",
            "x-client-id": "YOUR_CLIENT_ID",
            "x-client-secret": "YOUR_CLIENT_SECRET"
        }
        response = requests.post('https://test.cashfree.com/api/v2/cftoken/order', json=payload, headers=headers)
        return redirect(response.json()['paymentLink'])
    return render_template('payment.html')



















if __name__ == '__main__':
    app.run(debug=True)
