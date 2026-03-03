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
        self.status = tk.Label(self.window, text = "Ready...", fg = "Black")
        self.window.mainloop()
    def start_thread(self):
        path = filedialog.askopenfilename(filetypes=[("OXPS", "*.oxps")])
        if path:
            self.btn.config(state="disabled")
            self.status.config(text="Converting...", fg="Green")
            thread = th.Thread(target = self.process, args=(path,))
            thread.start()
    def process(self, path):
        success, result = oxpsConverter(path)
        self.window.after(0, lambda: self.finish(success,result))
    def finish(self, success, result):
        self.btn.config(state="normal")
        if success:
            self.status.config(text="File Converted Successfully!", fg="green")
            messagebox.showinfo("Success", f"Saved to: {result}")
        else:
            self.status.config(text="File Converted Unsuccessful", fg="red")
            messagebox.showerror("Error",result)

if __name__ == "__main__":
    window = tk.Tk()
    app = Oxpsapp(window)
   
