class Slide2(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
    
        self.controller = controller
        self.configure(bg="white")
