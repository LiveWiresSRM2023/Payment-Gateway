from flask import Blueprint, request, jsonify, current_app

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/payment_status', methods=['POST'])
def payment_status():
    data = request.json
    if data['txStatus'] == 'SUCCESS':
        # Fetch the corresponding user data
        db = current_app.config['FIREBASE']
        payments = db.child("payments").order_by_child("orderId").equal_to(data['orderId']).get()
        for payment in payments.each():
            user_data = payment.val()
            user_data.update({
                "paymentStatus": "SUCCESS",
                "transactionId": data['referenceId']
            })
            db.child("successful_payments").push(user_data)
            db.child("payments").child(payment.key()).remove()

    return jsonify({"status": "ok"})
