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
