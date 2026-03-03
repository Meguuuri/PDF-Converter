import tkinter as tk

window = tk.Tk()

window.geometry("500x500")
window.title("OXPS to PDF Converter")

label = tk.Label(window, text ="Microsoft One Note To PDF File Converter", font=('Arial', 12))
label.pack(padx=20, pady=20)

window.mainloop()

