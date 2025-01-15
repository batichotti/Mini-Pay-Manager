from datetime import datetime, timedelta

def create_message(name: str, due_date: datetime, next_due_date: datetime | bool) -> str:
    """
    Creates a payment reminder message based on the due date and next due date.

    Args:
        name (str): The name of the person.
        due_date (datetime): The due date of the payment.
        next_due_date (datetime | bool): The next due date of the payment or False if there is no next due date.

    Returns:
        str: The payment reminder message.
    """
    today = datetime.today()
    message = ""
    first_name = name.split()[0]

    # Caso 1: Boleto prestes a vencer (10 dias antes do vencimento ou no vencimento)
    if due_date - timedelta(days=10) <= today <= due_date or today.replace(hour=0, minute=0, second=0, microsecond=0) == due_date:
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        due_date_str = "*HOJE*" if today == due_date else due_date.strftime('%d/%m/%Y')
        message = (
            f"Olá {first_name},\n"
            f"Passando para lembrar de seu boleto que irá vencer na data de {due_date_str}.\n"
            "Pague até o vencimento e não perca o desconto!\n"
            "Studio R Formaturas"
        )
    
    # Caso 2: Boleto vencido há até 20 dias
    elif due_date < today <= due_date + timedelta(days=20):
        message = (
            f"Olá {first_name},\n"
            f"Consta um boleto em seu nome vencido em {due_date.strftime('%d/%m/%Y')}.\n"
            "Procure pagar em dia e evite juros e multas desnecessários.\n"
            "Studio R Formaturas"
        )
    
    # Caso 3: Boleto vencido há mais de 31 dias (sem outros boletos vencidos)
    elif due_date + timedelta(days=31) < today and (not isinstance(next_due_date, datetime) or today <= next_due_date):
        message = (
            f"Olá {first_name},\n"
            "Consta vencido o último boleto de sua compra.\n"
            "Informamos que após o 30° dia o seu nome será incluído automaticamente no SERASA/SPC.\n"
            "Evite transtornos!!!\n"
            "Entre em contato para regularização ou renegociação amigável.\n"
            "Studio R Formaturas"
        )
    
    # Caso 4: Mais de um boleto vencido (ou seja, próximo boleto também está vencido)
    elif isinstance(next_due_date, datetime) and today > next_due_date:
        message = (
            f"Olá {first_name},\n"
            "Constam vários boletos vencidos provenientes de sua compra.\n"
            "Informamos que seu contrato está em movimento para ajuizamento, o que elevará significativamente os valores a pagar com juros, multa e honorários advocatícios.\n"
            "Informamos também que seu nome foi incluído no SERASA/SPC nesta data.\n"
            "Entre em contato urgente para regularização ou renegociação amigável.\n"
            "Studio R Formaturas"
        )
    
    # Caso 5: Boleto vencido entre 21 e 31 dias (sem outros atrasos)
    elif due_date + timedelta(days=20) < today <= due_date + timedelta(days=31):
        message = (
            f"Olá {first_name},\n"
            "Em poucos dias vencerá mais um boleto de sua compra.\n"
            "Informamos que após duas parcelas vencidas seu nome é incluído automaticamente no SCP/SERASA.\n"
            "Efetue o pagamento ou entre em contato para regularização ou renegociação amigável.\n"
            "Evite transtornos!\n"
            "Studio R Formaturas"
        )

    return message