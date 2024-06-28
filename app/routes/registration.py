from flask import Blueprint, render_template, request, redirect, url_for
import uuid
from app.utils.firebase import add_user

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'order_id': str(uuid.uuid4()),  # Generate a unique order_id
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone')
        }
        # Store user_data in Firebase or another database
        add_user(user_data)
        return redirect(url_for('payment.payment', **user_data))

    return render_template('register.html')
