from flask import Blueprint, render_template, request, redirect, current_app
import requests

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        payload = {
            "orderId": "order{}".format(hash(email)),
            "orderAmount": "100",
            "orderCurrency": "INR",
            "customerName": name,
            "customerPhone": phone,
            "customerEmail": email
        }
        headers = {
            "Content-Type": "application/json",
            "x-client-id": "YOUR_CLIENT_ID",
            "x-client-secret": "YOUR_CLIENT_SECRET"
        }
        response = requests.post('https://test.cashfree.com/api/v2/cftoken/order', json=payload, headers=headers)
        payment_link = response.json().get('paymentLink')

        # Store payment details temporarily
        db = current_app.config['FIREBASE']
        db.child("payments").push(payload)

        return redirect(payment_link)
    return render_template('payment.html')
