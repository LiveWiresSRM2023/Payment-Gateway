from flask import Blueprint, render_template, request, redirect, current_app

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        data = {"name": name, "email": email, "phone": phone}
        db = current_app.config['FIREBASE']
        db.child("registrations").push(data)
        return redirect('/payment?name={}&email={}&phone={}'.format(name, email, phone))
    return render_template('register.html')
