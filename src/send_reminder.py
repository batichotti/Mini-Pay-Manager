import pywhatkit as kit
from time import sleep
import webbrowser
import time

def send_payment_reminder(payment: dict, method: str = 'pywhatkit') -> None:
    """
    Send a payment reminder using the specified method.

    Args:
        payment (dict): A dictionary containing the phone number and message.
        method (str): The method to use for sending the reminder ('pywhatkit', 'selenium', 'wa_link', or 'print').
    """
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
    """
    Open WhatsApp Web in the default web browser.
    """
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(60)

def send_with_pywhatkit(phone, message):
    """
    Send a WhatsApp message using pywhatkit.

    Args:
        phone (str): The phone number to send the message to.
        message (str): The message to send.
    """
    kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)

def send_with_selenium(phone, message):
    """
    Send a WhatsApp message using Selenium.

    Args:
        phone (str): The phone number to send the message to.
        message (str): The message to send.
    """
    pass

def send_with_wa_link(phone, message):
    """
    Send a WhatsApp message using a wa.me link.

    Args:
        phone (str): The phone number to send the message to.
        message (str): The message to send.
    """
    pass

def print_message(phone, message):
    """
    Print the message to the console.

    Args:
        phone (str): The phone number to send the message to.
        message (str): The message to send.
    """
    print("\n")
    print(f"Phone: {str(phone)}")
    print(f"Message: {message}")

if __name__ == "__main__":
    payments = {
        'phone': '0000000000',
        'message': 'A message'
    }
    send_payment_reminder(payments)
