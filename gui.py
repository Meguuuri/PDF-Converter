import tkinter as tk
from main import oxpsConverter
class Oxpsapp:
    def __init__(self, window):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("OXPS to PDF Converter")

        self.label = tk.Label(self.window, text ="Microsoft One Note To PDF File Converter", font=('Arial', 12))
        self.label.pack(padx=20, pady=20)
        self.window.mainloop()

