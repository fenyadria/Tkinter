from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class Slide3(Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    
    self.controller = controller
    self.configure(bg="white")

    topframe = Frame(self, background="black", height="80")
    topframe.pack(fill="x", side="top") 

    Label(topframe, text="Ao", fg='blue', bg='black', font=('Arial', 16, 'bold')).grid(row=1, column=0, padx=5, pady=5)
    self.ao_name = Entry(topframe, width=15)
    self.ao_name.insert(0, "input")
    self.ao_name.grid(row=1, column=1, padx=10)

    Label(topframe, text="Divisi :", fg='white', bg='black', font=('Arial', 16)).grid(row=1, column=3)
    self.divisi_entry = Entry(topframe, width=15)
    self.divisi_entry.insert(0, "input")
    self.divisi_entry.grid(row=1, column=4, padx=10)

    Label(topframe, text="Aka", fg='red', bg='black', font=('Arial', 16, 'bold')).grid(row=1, column=6)
    self.aka_name = Entry(topframe, width=15)
    self.aka_name.insert(0, "input")
    self.aka_name.grid(row=1, column=7, padx=10)

    Button(topframe, text="Close", bg='darkred', fg='white', font=('Arial', 12, 'bold'),
    command=self.winfo_toplevel().quit).grid(row=0, column=10, rowspan=2, padx=10)

    subframe4 = Frame(self, height="70", bg="white")
    subframe4.pack(fill="x", side="bottom")

    subframe = Frame(self, background="blue")
    subframe.pack(expand = True, fill = "both", side="left")
 
    subframe2 = Frame(self, background="red")
    subframe2.pack(expand=True, fill="both", side="left")
    
    btn_kembali = Button(subframe3, text="Kembali",
                         command=lambda: controller.show_slide("Slide1"),
                         font=("Algerian", 15, "bold"),
                         bg="#5B2C2C", fg="white",
                         activebackground="#0059b3", activeforeground="white",
                         padx=0, pady=0, borderwidth=0, relief="flat")
    btn_kembali.pack(side="right", padx=30, pady=20)


