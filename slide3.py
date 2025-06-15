from tkinter import Frame, Button, Label, Tk, StringVar, messagebox
import os, csv, datetime
from PIL import Image, ImageTk

class Slide3(Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller
    self.configure(bg="white")

    self.time_left = 60
    self.running = False
    self.stopwatch_visible = True

    self.subframe3 = Frame(self, background="black", height=100, width=1550)
    self.subframe3.place(x=0, y=0)

    Label(self.subframe3, text="Ao", fg='blue', bg='black', font=('Arial', 16, 'bold')).place(x=30, y=30)
    self.ao_name = Entry(self.subframe3, width=15)
    self.ao_name.place(x=70, y=35)

    Label(self.subframe3, text="Divisi :", fg='white', bg='black', font=('Arial', 16)).place(x=700, y=30)
    self.divisi_entry = Entry(self.subframe3, width=15)
    self.divisi_entry.place(x=775, y=35)

    Label(self.subframe3, text="Aka", fg='red', bg='black', font=('Arial', 16, 'bold')).place(x=1250, y=30)
    self.aka_name = Entry(self.subframe3, width=15)
    self.aka_name.place(x=1300, y=35)

    Button(self.subframe3, text="Kembali", bg='darkred', fg='white',
    font=('Arial', 12, 'bold'), command=lambda: controller.show_slide("Slide1")).place(x=1450, y=25)

    self.subframe4 = Frame(self, bg="white", height=70, width=1550)
    self.subframe4.place(x=0, y=730)

    Button(self.subframe4, text='Start', font=('Arial', 14, 'bold'),
           bg='limegreen', fg='white', command=self.start_timer).place(x=30, y=15)
    Button(self.subframe4, text='Show/Hide Stopwatch', font=('Arial', 12),
            bg='lightgreen', command=self.toggle_stopwatch).place(x=600, y=18)

    Button(self.subframe4, text='Done', font=('Arial', 14, 'bold'),
            bg='lightgreen', command=self.done).place(x=800, y=15)
    Button(self.subframe4, text='Reset', font=('Arial', 14, 'bold'),
            bg='red', fg='white', command=self.reset).place(x=1450, y=12)
    Button(self.subframe4, text='Shikakku', font=('Arial', 12),
            bg='navy', fg='white', command=self.shikakku_blue).place(x=300, y=15)
    Button(self.subframe4, text='Kikken', font=('Arial', 12),
            bg='darkblue', fg='white', command=self.kikken_blue).place(x=400, y=15)
    Button(self.subframe4, text='Shikakku', font=('Arial', 12),
            bg='darkred', fg='white', command=self.shikakku_red).place(x=1100, y=15)
    Button(self.subframe4, text='Kikken', font=('Arial', 12),
            bg='firebrick', fg='white', command=self.kikken_red).place(x=1200, y=15)

    self.subframe = Frame(self, background="blue", height=650, width=775)
    self.subframe.place(x=0, y=80)

    self.blue_score = StringVar(value="0")
    Label(self.subframe, textvariable=self.blue_score, font=("Digital-7", 150),
          bg="blue", fg="white").place(x=160, y=100)

    Button(self.subframe, text="+1", command=self.increment_blue,
           font=("Arial", 20), width=3).place(x=150, y=450)
    Button(self.subframe, text="-1", command=self.decrement_blue,
           font=("Arial", 20), width=3).place(x=250, y=450)

    self.ao_timer_label = Label(self.subframe, text="1:00", font=("Digital-7", 70),
                                bg="blue", fg="white")
    self.ao_timer_label.place(x=500, y=425)
    
    self.subframe2 = Frame(self, background="red", height=650, width=775)
    self.subframe2.place(x=775, y=80)

    self.red_score = StringVar(value="0")
    Label(self.subframe2, textvariable=self.red_score, font=("Digital-7", 150),
          bg="red", fg="white").place(x=150, y=100)

    Button(self.subframe2, text="+1", command=self.increment_red,
           font=("Arial", 20), width=3).place(x=125, y=450)
    Button(self.subframe2, text="-1", command=self.decrement_red,
            font=("Arial", 20), width=3).place(x=225, y=450)

    self.aka_timer_label = Label(self.subframe2, text="1:00", font=("Digital-7", 70),
                                 bg="red", fg="white")
    self.aka_timer_label.place(x=490, y=425)
    
    self.gambar1 = ImageTk.PhotoImage(Image.open("blueflag.jpg").resize((250, 250)))
    self.gambar2 = ImageTk.PhotoImage(Image.open("redflag.jpg").resize((250, 250)))

    Label(self.subframe, image=self.gambar1, bg="blue").place(x=480, y=80)
    Label(self.subframe2, image=self.gambar2, bg="red").place(x=460, y=80)

    def countdown(self, count):
      if count >= 0 and self.running:
        mins, secs = divmod(count, 60)
        time_format = f"{mins}:{secs:02d}"
        self.ao_timer_label.config(text=time_format)
        self.aka_timer_label.config(text=time_format)
        self.time_left = count
        self.after(1000, self.countdown, count - 1)
      elif count < 0:
        self.running = False
        self.done()

    def start_timer(self):
      if not self.ao_name.get().strip() or not self.aka_name.get().strip() or not self.divisi_entry.get().strip():
            messagebox.showwarning("Peringatan", "Harap isi nama Tim Ao, Tim Aka, dan Divisi terlebih dahulu!")
            return
      if not self.running:
            self.running = True
            self.countdown(self.time_left)

    def toggle_stopwatch(self):
        self.stopwatch_visible = not self.stopwatch_visible
        if self.stopwatch_visible:
            self.ao_timer_label.place(x=500, y=425)
            self.aka_timer_label.place(x=490, y=425)
        else:
            self.ao_timer_label.place_forget()
            self.aka_timer_label.place_forget()

    def save_to_csv(self):
        with open('skor.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([
                now,
                self.ao_name.get(),
                self.aka_name.get(),
                self.divisi_entry.get(),
                self.blue_score.get(),
                self.red_score.get()
            ])

    def done(self):
        self.save_to_csv()
        messagebox.showinfo("Done", "Pertandingan selesai!")

    def reset(self):
        self.blue_score.set("0")
        self.red_score.set("0")
        self.time_left = 60
        self.running = False
        self.ao_timer_label.config(text="1:00")
        self.aka_timer_label.config(text="1:00")

    
    def shikakku_blue(self):
        ao = self.ao_name.get()
        messagebox.showinfo("Diskualifikasi", f"Pertandingan selesai, tim {ao} didiskualifikasi!")

    def kikken_blue(self):
        aka = self.aka_name.get()
        messagebox.showinfo("Menang WO", f"Pertandingan selesai, dimenangkan oleh tim {aka}!")

    def shikakku_red(self):
        aka = self.aka_name.get()
        messagebox.showinfo("Diskualifikasi", f"Pertandingan selesai, tim {aka} didiskualifikasi!")

    def kikken_red(self):
        ao = self.ao_name.get()
        messagebox.showinfo("Menang WO", f"Pertandingan selesai, dimenangkan oleh tim {ao}!")

    
    def increment_blue(self):
        score = int(self.blue_score.get()) + 1
        self.blue_score.set(str(score))

    def decrement_blue(self):
        score = int(self.blue_score.get()) - 1
        self.blue_score.set(str(score))

    def increment_red(self):
        score = int(self.red_score.get()) + 1
        self.red_score.set(str(score))

    def decrement_red(self):
        score = int(self.red_score.get()) - 1
        self.red_score.set(str(score))
