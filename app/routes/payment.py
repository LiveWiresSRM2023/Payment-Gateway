from flask import Blueprint, render_template, request, redirect, url_for

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        amount = request.form.get('amount')
        customer_name = request.form.get('customer_name')
        customer_email = request.form.get('customer_email')
        
        # Process payment logic here

        return redirect(url_for('payment.success'))  # Replace with actual success route

    return render_template('payment.html')
