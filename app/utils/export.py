import openpyxl
from flask import send_file

def export_to_excel(users):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Registrations'
    sheet.append(['Name', 'Email', 'Phone', 'Order ID', 'Transaction ID', 'Payment Status'])

    for user in users:
        sheet.append([
            user['name'], 
            user['email'], 
            user['phone'], 
            user['orderId'], 
            user['transactionId'], 
            user['paymentStatus']
        ])

    file_path = 'registrations.xlsx'
    workbook.save(file_path)
    return send_file(file_path, as_attachment=True)
