from gui import PaymentManagerApp
import tkinter as tk


def main():
    root = tk.Tk()
    app = PaymentManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
