class Slide1(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.original_image = Image.open("Tyler The Creator.jpg")
        self.canvas = Canvas(self, width=1300, height=650, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Configure>", self.resize_background)

        self.tombol_lanjut = Button(self, text="Perkenalan Kelompok",
                                    command=lambda: controller.show_slide("Slide2"),
                                    font=("Algerian", 15, "bold"),
                                    bg="#5B2C2C", fg="white",
                                    activebackground="#0059b3", activeforeground="white",
                                    padx=20, pady=10, borderwidth=0, relief="flat")
        self.tombol_ke_slide3 = Button(self, text="Project UAS",
                                       command=lambda: controller.show_slide("Slide3"),
                                       font=("Algerian", 15, "bold"),
                                       bg="#5B2C2C", fg="white",
                                       activebackground="#0059b3", activeforeground="white",
                                       padx=20, pady=10, borderwidth=0, relief="flat")

        self.tombol_lanjut.bind("<Enter>", lambda e: self.tombol_lanjut.config(bg="#090909"))
        self.tombol_lanjut.bind("<Leave>", lambda e: self.tombol_lanjut.config(bg="#5B2C2C"))

        self.tombol_ke_slide3.bind("<Enter>", lambda e: self.tombol_ke_slide3.config(bg="#02080e"))
        self.tombol_ke_slide3.bind("<Leave>", lambda e: self.tombol_ke_slide3.config(bg="#5B2C2C"))

        self.tombol_lanjut_id = None
        self.tombol_ke_slide3_id = None

        self.floating_text1 = None
        self.floating_text2 = None
        self.float_offset = 0
        self.float_direction = 1    

    def resize_background(self, event):
