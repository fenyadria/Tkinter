class Slide3(Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller
    self.configure(bg="white")
    
    btn_kembali = Button(subframe3, text="Kembali",
                         command=lambda: controller.show_slide("Slide1"),
                         font=("Algerian", 15, "bold"),
                         bg="#5B2C2C", fg="white",
                         activebackground="#0059b3", activeforeground="white"
                         padx=10, pady=10, borderwidth=0, relief="flat")
    btn_kembali.pack(side="right", pady = 10)


