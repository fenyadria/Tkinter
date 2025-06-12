from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class Slide3(Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    
    self.controller = controller
    self.configure(bg="white")

    subframe3 = Frame(self, background="black", height="80")
    subframe3.pack(fill="x", side="top") 

    subframe4 = Frame(self, height="70", bg=self['bg'])
    subframe4.pack(fill="x", side="bottom")

    subframe = Frame(self, background="blue")
    subframe.pack(expand = True, fill = "both", side="left")
 
    subframe2 = Frame(self, background="red")
    subframe2.pack(expand=True, fill="both", side="left")
    
    btn_kembali = Button(subframe3, text="Kembali",
                         command=lambda: controller.show_slide("Slide1"),
                         font=("Algerian", 15, "bold"),
                         bg="#5B2C2C", fg="white",
                         activebackground="#0059b3", activeforeground="white"
                         padx=0, pady=0, borderwidth=0, relief="flat")
    btn_kembali.pack(side="right", padx=30, pady=20)


