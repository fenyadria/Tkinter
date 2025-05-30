class Slide2(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
    
        self.controller = controller
        self.configure(bg="white")
        
        title = Label(self, text="DISUSUN OLEH", font=("Segoa UI", 50, "bold"), fg="black", bg="white")
        title.pack(pady=20)
        
        team_frame = Frame(self, bg="white")
        team_frame.pack(pady=20)

