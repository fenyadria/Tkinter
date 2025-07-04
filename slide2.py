from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class Slide2(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
    
        self.controller = controller
        self.configure(bg="white")

        title = Label(self, text="DISUSUN OLEH", font=("Segoa UI", 50, "bold"), fg="black", bg="white")
        title.pack(pady=20)

        team_frame = Frame(self, bg="white")
        team_frame.pack(pady=20)

        self.images = []
        nama = ["Arkhan Al Hakim", "Feny Adria Marshela", "Kamila Putri Hasan", "Sakinah"]
        npm = [2417053002, 2417051010, 2417051026, 2417051024]
        files = ["fotoarkhan.png", "fotofeny.png", "fotokamila.png", "fotosakinah.png"]

        for i in range(4):
            member = Frame(team_frame, bg="white")
            member.pack(side="left", padx=15)

            try:
                img = Image.open(files[i]).resize((200, 300))
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)

                lbl_img = Label(member, image=photo, bg="white")
                lbl_img.pack()

            except Exception as e:
                print(f"Failed to load {files[i]}: {e}")
                lbl_img = Label(member, text="(No image)", bg="white")
                lbl_img.pack()

            lbl_name = Label(member, text=nama[i], font=("Helvetica", 12, "bold"), bg="white")
            lbl_name.pack(pady=5)
            
            lbl_npm = Label(member, text=npm[i], font=("Helvetica", 10, "bold"), bg="white")
            lbl_npm.pack(pady=5)

        nav_frame = Frame(self, bg="white")
        nav_frame.pack(pady=30)

        btn_kembali = Button(nav_frame, text="Kembali",
                             command=lambda: controller.show_slide("Slide1"),
                             font=("Algerian", 15, "bold"),
                             bg="#5B2C2C", fg="white",
                             activebackground="#0059b3", activeforeground="white",
                             padx=20, pady=10, borderwidth=0, relief="flat")
        btn_kembali.pack(side="left", padx=20)

        btn_lanjut = Button(nav_frame, text="Project UAS",
                            command=lambda: controller.show_slide("Slide3"),
                            font=("Algerian", 15, "bold"),
                            bg="#5B2C2C", fg="white",
                            activebackground="#0059b3", activeforeground="white",
                            padx=20, pady=10, borderwidth=0, relief="flat")
        btn_lanjut.pack(side="left", padx=20)

        btn_kembali.bind("<Enter>", lambda e: btn_kembali.config(bg="#090909"))
        btn_kembali.bind("<Leave>", lambda e: btn_kembali.config(bg="#5B2C2C"))

        btn_lanjut.bind("<Enter>", lambda e: btn_lanjut.config(bg="#02080e"))
        btn_lanjut.bind("<Leave>", lambda e: btn_lanjut.config(bg="#5B2C2C"))

