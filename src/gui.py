import tkinter as tk
from tkinter import filedialog
import pandas as pd
from send_reminder import send_payment_reminder
import config_gui as cfg

def load_excel_file()->None:
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)

def send_charges()->None:

    print("Sending charges...")

root = tk.Tk()
root.title(cfg.WINDOW_TITLE)
root.configure(bg=cfg.BG_COLOR)
root.geometry(cfg.WINDOW_SIZE)
root.resizable(cfg.WINDOW_RESIZABLE, cfg.WINDOW_RESIZABLE)

frame = tk.Frame(root, bg=cfg.BG_COLOR)
frame.pack(pady=cfg.PADY)

load_button = tk.Button(frame, text="Carregar Tabela Excel", command=load_excel_file, bg=cfg.BTN_COLOR, fg=cfg.BTN_TEXT_COLOR)
load_button.pack(pady=cfg.PADY)

send_button = tk.Button(frame, text="Enviar Cobranças", command=send_charges, bg=cfg.BTN_COLOR, fg=cfg.BTN_TEXT_COLOR)
send_button.pack(pady=cfg.PADY)

root.mainloop()
