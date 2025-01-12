from datetime import datetime, timedelta

def create_message(name: str, due_date: datetime, amount: float, next_due_date: datetime | bool) -> str:
    today = datetime.today()
    due_date = datetime.combine(due_date, datetime.min.time())
    message = ""

    if today == due_date - timedelta(days=5):
        message = f"Olá {name}, seu pagamento de {amount} vence em 5 dias."
    elif today == due_date:
        message = f"Olá {name}, seu pagamento de {amount} vence hoje."
    elif due_date < today <= due_date + timedelta(days=10):
        message = f"Olá {name}, seu pagamento de {amount} está atrasado há {(today - due_date).days} dias."
    elif due_date + timedelta(days=10) < today <= due_date + timedelta(days=25):
        message = f"Olá {name}, seu pagamento de {amount} está atrasado há {(today - due_date).days} dias. Por favor, regularize sua situação."
    elif due_date + timedelta(days=25) < today <= due_date + timedelta(days=30):
        message = f"Olá {name}, seu pagamento de {amount} está muito atrasado. Por favor, entre em contato conosco."
    elif today > due_date + timedelta(days=30):
        message = f"Olá {name}, seu pagamento de {amount} está extremamente atrasado. Ação imediata é necessária."
    if next_due_date and today > next_due_date:
        message += f"\nOlá {name}, este é o seu segundo boleto vencido. Por favor, regularize sua situação imediatamente."

    return message
