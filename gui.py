import tkinter as tk
from convertFunction import oxpsConverter
from tkinter import filedialog, messagebox
import threading as th
class Oxpsapp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x250")
        self.window.title("OXPS to PDF Converter")

        self.label = tk.Label(self.window, text ="Microsoft One Note To PDF File Converter", font=('Arial', 12))
        self.label.pack(padx=20, pady=20)
        self.btn = tk.Button(window, text = "Select File", command= self.start_thread, pady=10,padx=20)
        self.btn.pack(pady=20)
        self.status_var = tk.StringVar(value= "Ready...")
        self.status_label = tk.Label(self.window, textvariable=self.status_var, fg = "black", font=('Arial', 8))
        self.status_label.pack(pady=20)
        self.window.mainloop()
    def start_thread(self):
        path = filedialog.askopenfilename(filetypes=[("OXPS", "*.oxps")])
        if path:
            self.btn.config(state="disabled")
            self.status_var.set("Converting...")
            thread = th.Thread(target = self.process, args=(path,))
            thread.start()
    def process(self, path):
        success, result = oxpsConverter(path)
        self.window.after(0, lambda: self.finish(success,result))
    def finish(self, success, result):
        self.btn.config(state="normal")
        if success:
            self.status_var.set("File Converted Successfully!")
            messagebox.showinfo("Success", f"Saved to: {result}")
        else:
            self.status_var.set("File Convertion Unsuccessful")
            messagebox.showerror("Error",result)

if __name__ == "__main__":
    window = tk.Tk()
    app = Oxpsapp(window)
   
