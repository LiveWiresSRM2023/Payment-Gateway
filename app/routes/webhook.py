from flask import Blueprint, request, jsonify
from app.utils.firebase import store_payment_details
from app.utils.email import send_ticket_email

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    order_id = data.get('order_id')
    order_amount = data.get('order_amount')
    customer_details = data.get('customer_details')
    status = data.get('status')

    if not all([order_id, order_amount, customer_details, status]):
        return jsonify({"error": "Missing required parameters"}), 400

    # Store payment details in Firebase
    payment_details = {
        "order_amount": order_amount,
        "customer_details": customer_details,
        "status": status
    }
    store_payment_details(order_id, payment_details)
    
    # Send ticket email
    customer_email = customer_details.get('customer_email')
    subject = "Your Payment Ticket"
    body = f"Dear {customer_details.get('customer_name')},\n\nYour payment was successful. Here are your details:\nOrder ID: {order_id}\nOrder Amount: {order_amount}\n\nThank you for your purchase!"
    email_sent = send_ticket_email(customer_email, subject, body)
    
    if not email_sent:
        return jsonify({'status': 'success', 'message': 'Payment details stored, but failed to send email.'})

    return jsonify({'status': 'success', 'message': 'Payment details stored and email sent.'})
