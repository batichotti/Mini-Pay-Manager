# Mini-Payment-Manager

## Overview
Mini-Pay-Manager is a Python application designed to help manage and send payment reminders via WhatsApp. It uses a GUI built with Tkinter to load payment data from an Excel file and send reminders using various methods.

## Features
- Load payment data from an Excel file.
- Generate payment reminder messages based on due dates.
- Send reminders via WhatsApp using different methods (`pywhatkit`, `selenium`, `wa_link`, or print to console).

## Requirements
- Python 3.x
- Required Python packages:
  - `pywhatkit`
  - `tkinter`
  - `pandas`
  - `openpyxl`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Mini-Pay-Manager.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Mini-Pay-Manager/src
    ```
3. Install the required packages:
    ```sh
    pip install pywhatkit pandas openpyxl
    ```

## Usage
1. Run the application:
    ```sh
    python gui.py
    ```
2. Use the GUI to load an Excel file containing payment data.
3. Click "Enviar Cobranças" to send payment reminders.

## File Descriptions
### `gui.py`
This file contains the main GUI application built with Tkinter. It allows users to load an Excel file and send payment reminders.

### `payment_to_message.py`
This file contains the `create_message` function, which generates payment reminder messages based on due dates.

### `send_reminder.py`
This file contains functions to send payment reminders using different methods (`pywhatkit`, `selenium`, `wa_link`, or print to console).

### `config_gui.py`
This file contains configuration settings for the GUI, such as padding, colors, window size, and fonts.

## Example Excel File Format
The Excel file should contain the following columns:
- `Nome`: The name of the person.
- `Telefone`: The phone number of the person.
- `Valor`: The amount due.
- `Vencimento`: The due date of the payment (format: `dd/mm/yyyy`).

## License
This project is licensed under the MIT License.

