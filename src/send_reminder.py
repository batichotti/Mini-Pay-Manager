import pywhatkit as kit
from datetime import datetime, timedelta
from time import sleep
import webbrowser
import time

def send_payment_reminder(payments: list, method: str='pywhatkit'):
    if method == 'pywhatkit':
        open_whatsapp_web()
    
    for payment in payments:
        message = payment['message']
        phone = payment['phone']
        if len(phone) <= 11:
            phone = "+55" + phone

        if message:
            if method == 'pywhatkit':
                send_with_pywhatkit(phone, message)
            elif method == 'selenium':
                send_with_selenium(phone, message)
            elif method == 'wa_link':
                send_with_wa_link(phone, message)
            elif method == 'print':
                print_message(phone, message)

def open_whatsapp_web():
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(15)

def send_with_pywhatkit(phone, message):
    kit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)

def send_with_selenium(phone, message):
    pass

def send_with_wa_link(phone, message):
    pass

def print_message(phone, message):
    print(f"Phone: {phone}")
    print(f"Message: {message}")

if __name__ == "__main__":
    payments = [
        {
            'client_name': 'John Doe',
            'client_phone': '44998385898',
            'amount': '100.00',
            'due_date': '2024-12-29'
        },
        {
            'client_name': 'Jane Smith',
            'client_phone': '44998385898',
            'amount': '100.00',
            'due_date': '2025-01-04'
        },
        {
            'client_name': 'Alice Johnson',
            'client_phone': '44998385898',
            'amount': '100.00',
            'due_date': '2025-01-05'
        }
    ]
    send_payment_reminder(payments)
