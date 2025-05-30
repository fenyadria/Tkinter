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
        npm = [2417053002, 2417051010, 2417051026, 2417050000]
        files = ["ARKAN.jpg", "paspotopeni.jpg", "PASPOTO_Kamila Putri Hasan.jpg", "SAKINA.jpg"]

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
            
        nav_frame = Frame(self, bg="white")
        nav_frame.pack(pady=30)

        btn_kembali = Button(nav_frame, text="Kembali", command=lambda: controller.show_slide("Slide1"))
        btn_kembali.pack(side="left", padx=20)

        btn_lanjut = Button(nav_frame, text="Lanjut", command=lambda: controller.show_slide("Slide3"))
        btn_lanjut.pack(side="left", padx=20)
            lbl_npm = Label(member, text=npm[i], font=("Helvetica", 10, "bold"), bg="white")
            lbl_npm.pack(pady=5)


