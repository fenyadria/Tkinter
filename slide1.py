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
        resized = self.original_image.resize((event.width, event.height), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized)

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.center_x = event.width // 2
        self.center_y = event.height // 3
        if not self.floating_text1 and not self.floating_text2:
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

            self.floating_text1_outline_ids, self.floating_text1 = garis_pinggir_teks(
            self.canvas, self.center_x, self.center_y - 60,
            "WELCOME",
            ("Old English Text MT", 120, "bold"),
            fill="#5B2C2C",
            outline_color="white",
            outline_width=2
    )

            self.floating_text2_outline_ids, self.floating_text2 = garis_pinggir_teks(
            self.canvas, self.center_x, self.center_y + 60,
            "Project Kelompok 9",
            ("Magneto", 50, "bold"),
            fill="#5B2C2C",
            outline_color="white",
            outline_width=2
    )

            self.tombol_lanjut_id = self.canvas.create_window(
                self.center_x, self.center_y + 100,  # Tetap
                window=self.tombol_lanjut
            )
            self.tombol_ke_slide3_id = self.canvas.create_window(
                self.center_x, self.center_y + 160,
                window=self.tombol_ke_slide3
            )

            self.animate_floating_text()
        else:
            self.canvas.coords(self.floating_text1, self.center_x, self.center_y - 60 + self.float_offset)
            self.canvas.coords(self.floating_text2, self.center_x, self.center_y + 60 + self.float_offset)
            self.canvas.coords(self.tombol_lanjut_id, self.center_x, self.center_y + 100)
            self.canvas.coords(self.tombol_ke_slide3_id, self.center_x, self.center_y + 160)

    def animate_floating_text(self):
        self.float_offset += self.float_direction
        if abs(self.float_offset) > 20:
          self.float_direction *= -1

        ox = [ -2, -2, -2, 0, 0, 2, 2, 2 ]
        oy = [ -2, 0, 2, -2, 2, -2, 0, 2 ]
        for i, outline_id in enumerate(self.floating_text1_outline_ids):
          self.canvas.coords(outline_id, self.center_x + ox[i], self.center_y - 60 + oy[i] + self.float_offset)
        self.canvas.coords(self.floating_text1, self.center_x, self.center_y - 60 + self.float_offset)
        for i, outline_id in enumerate(self.floating_text2_outline_ids):
          self.canvas.coords(outline_id, self.center_x + ox[i], self.center_y + 20 + oy[i] + self.float_offset)
        self.canvas.coords(self.floating_text2, self.center_x, self.center_y + 20 + self.float_offset)

        self.after(50, self.animate_floating_text)

          

