import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from payment_to_message import create_message
from send_reminder import send_payment_reminder
import config_gui as cfg
from datetime import datetime
#pip install openpyxl

class PaymentManagerApp:
    def __init__(self, root):
        self.root = root
        self.df = None
        self.file_path_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        self.root.title(cfg.WINDOW_TITLE)
        self.root.configure(bg=cfg.BG_COLOR)
        self.root.geometry(cfg.WINDOW_SIZE)
        self.root.resizable(cfg.WINDOW_RESIZABLE, cfg.WINDOW_RESIZABLE)

        frame = tk.Frame(self.root, bg=cfg.BG_COLOR)
        frame.pack(pady=cfg.PADY)

        self.file_path_entry = tk.Entry(frame, textvariable=self.file_path_var, bg=cfg.BG_COLOR, fg=cfg.TEXT_INPUT_COLOR, font=cfg.FONT_INPUT, state='readonly', width=50)
        self.file_path_entry.pack(pady=cfg.PADY)

        load_button = tk.Button(frame, text="Carregar Tabela Excel", command=self.load_excel_file, bg=cfg.BTN_COLOR, fg=cfg.BTN_TEXT_COLOR, font=cfg.FONT)
        load_button.pack(pady=cfg.PADY)

        send_button = tk.Button(frame, text="Enviar Cobranças", command=self.send_charges, bg=cfg.BTN_COLOR, fg=cfg.BTN_TEXT_COLOR, font=cfg.FONT)
        send_button.pack(pady=cfg.PADY)

    def focus_on_end(self, event):
        self.file_path_entry.icursor(tk.END)

    def load_excel_file(self) -> None:
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            try:
                self.df = pd.read_excel(file_path)
                messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
                self.file_path_var.set(file_path)
                self.file_path_entry.icursor(tk.END)
                self.file_path_entry.xview_moveto(1)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")

    def send_charges(self) -> None:
        if self.df is not None:
            self.df['Vencimento'] = pd.to_datetime(self.df['Vencimento'], format='%d/%m/%Y')
            self.df = self.df.sort_values(by='Vencimento')
            grouped = self.df.groupby('Nome')
            for name, group in grouped:
                for index, row in group.iterrows():
                    next_due_date = group.iloc[index + 1]['Vencimento'] if index + 1 < len(group) else False
                    message: str = create_message(name=name, amount=float(row['Valor']), due_date=row['Vencimento'], next_due_date=next_due_date)
                    payment: dict = {'phone': row['Telefone'], 'message': message}
                    send_payment_reminder(payment, method='print')
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo carregado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentManagerApp(root)
    root.mainloop()
