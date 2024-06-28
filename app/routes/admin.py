from flask import Blueprint, render_template, send_file
from app.utils.firebase import get_all_payment_details
from app.utils.export import export_to_excel
import io

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/payments', methods=['GET'])
def admin():
    payments = get_all_payment_details()
    return render_template('admin.html', payments=payments)

@admin_bp.route('/admin/download', methods=['GET'])
def download_payments():
    payments = get_all_payment_details()
    output = io.BytesIO()
    export_to_excel(payments, output)
    output.seek(0)
    return send_file(output, attachment_filename="payments.xlsx", as_attachment=True)
