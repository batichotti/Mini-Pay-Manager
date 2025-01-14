import pywhatkit as kit
from time import sleep
import webbrowser
import time


def send_payment_reminder(payment:dict, method:str='pywhatkit')->None:
    if method == 'pywhatkit':
        open_whatsapp_web()
    
    phone = payment['phone']
    message = payment['message']

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
    time.sleep(60)

def send_with_pywhatkit(phone, message):
    kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)

def send_with_selenium(phone, message):
    pass

def send_with_wa_link(phone, message):
    pass

def print_message(phone, message):
    print("\n")
    print(f"Phone: {str(phone)}")
    print(f"Message: {message}")

if __name__ == "__main__":
    payments ={
            'phone': '0000000000',
            'message': 'A message'
        }
    send_payment_reminder(payments)
