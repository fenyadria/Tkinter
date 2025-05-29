from tkinter import Tk, Frame
from slide1 import Slide1
from slide2 import Slide2

class AplikasiTkinter:
  def __init__(self, root):
    self.root = root
    self.root.title("Kelompok 9")
    self.root.geometry("600x400")
    self.root.resizable(True, True)

    self.container = Frame(self.root)
    self.container.pack(expand=True, fill="both")
    self.slides = {}

if __name__ == "__main__":
  root = Tk()
  app = AplikasiTkinter(root)
  root.mainloop()
