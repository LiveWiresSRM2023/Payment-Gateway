import requests

class CashfreeAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = 'https://api.cashfree.com'

    def get_access_token(self):
        url = f"{self.base_url}/v2/auth/token"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()['token']
        else:
            return None

    def initiate_payment(self, order_id, amount, customer_name, customer_email):
        access_token = self.get_access_token()
        if not access_token:
            return False, "Failed to get access token from Cashfree"

        url = f"{self.base_url}/v2/payments"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        data = {
            'orderId': order_id,
            'orderAmount': str(amount),
            'customerName': customer_name,
            'customerPhone': '',  # Optional
            'customerEmail': customer_email,
            'returnUrl': 'http://your-website.com/payment/success',  # Replace with your actual return URL
            'notifyUrl': 'http://your-website.com/webhook',  # Replace with your actual webhook URL
            'paymentModes': 'upi'  # Adjust as per your requirement
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.json()
