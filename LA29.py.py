import tkinter as tk

your_name = "Badict Santiago"
your_section = "BSIT 2B"
root = tk.Tk()
root.title("OOP LA29")
text_disp = tk.Label(root, text=f"OOP 29 {your_name} {your_section}")
text_disp.grid(row=0, column=0, padx=100, pady=100)
root.mainloop()