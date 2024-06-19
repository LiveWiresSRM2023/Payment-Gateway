from flask import Blueprint, render_template, current_app
from app.utils.export import export_to_excel

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin():
    db = current_app.config['FIREBASE']
    users = db.child("successful_payments").get().each()
    user_details = [user.val() for user in users]
    return render_template('admin.html', users=user_details)

@admin_bp.route('/export')
def export_data():
    db = current_app.config['FIREBASE']
    users = db.child("successful_payments").get().each()
    user_details = [user.val() for user in users]
    return export_to_excel(user_details)
