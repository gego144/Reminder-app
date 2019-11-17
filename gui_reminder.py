import tkinter as tk

HEIGHT = 125
WIDTH = 600

the_text_holder = []
the_date_holder = []


def get_text(entry):
  the_text_holder.append(entry)


def get_date(entry):
    the_date_holder.append(entry)
    

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()


frame = tk.Frame(root, bg= "#696969")
frame.place(relwidth = 1, relheight = 1)


label = tk.Label(frame,text= "Reminder", bg = "#696969", font = ("arial", 12))
label.place(relx = 0.05, rely = 0.01)

label = tk.Label(frame,text= "Enter reminder:", bg = "#21558c", font = ("arial", 12))
label.place(relx = 0.05, rely = 0.19)

label = tk.Label(frame,text= "Enter time:", bg = "#21558c", font = ("arial", 12))
label.place(relx = 0.05, rely = 0.37)


reminder_entry = tk.Entry(frame, bg="white")
reminder_entry.place(relx=0.3, rely=0.19, relwidth=0.6)

time_entry = tk.Entry(frame, bg="white")
time_entry.place(relx=0.3, rely=0.37, relwidth=0.6)


button = tk.Button(frame, text="Set text", bg="#8b0000", command=lambda: get_text(reminder_entry.get()))
button.place(relx=0.91, rely=0.15)

button = tk.Button(frame, text="Set time", bg="#8b0000", command=lambda: get_date(time_entry.get()))
button.place(relx=0.91, rely=0.37)

root.mainloop()

