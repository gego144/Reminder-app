import tkinter as tk

root = tk.Tk()
root.title("Reminder")

HEIGHT = 125
WIDTH = 600

the_text_holder = []
the_date_holder = []
hours = []
minutes = []
seconds = []

# Getting the text the user wants to be reminded of
def get_text(entry):
    global the_text
    the_text_holder.append(entry)
    the_text= ''.join(the_text_holder)
    return the_text

# Getting when the user wants to be reminded 
def how_long_sleep(the_hour, the_minute, the_second):
    global sleep_for
    sleep_for = (3600000 * the_hour) +  (60000 * the_minute) + (1000 * the_second)
    return sleep_for

# The pop up of the reminder
def open_window():
    top = tk.Toplevel(root)
    top.title("Your reminder")
    canvas1 = tk.Canvas(top, height=HEIGHT, width=WIDTH)
    canvas1.pack()
    frame1 = tk.Frame(top, bg="#696969")
    frame1.place(relwidth=1, relheight=1)
    label0 = tk.Label(top, text="Don't forget!!!", bg="#8b0000", font=("arial", 12))
    label0.place(relx=0.05, rely=0.01)
    label1 = tk.Label(top, text= the_text, bg="#21558c", font=("arial", 12))
    label1.place(relx=0.05, rely=0.19)

# Making sure the user is inputing the correct time format and putting the program to sleep for as long as they requested if it is correct
def date_limit(entry):
    if len(entry) != 6 or entry.isdigit() == False:
        error_label = tk.Label(frame, text="Please make sure you are putting in a number with 6 digits", bg="#696969", font=("arial", 12))
        error_label.place(relx=0.05, rely=0.72)
    else:
        time_seperated = list(entry)
        # putting it into a list to make divide the values into their respective parts
        for i in time_seperated[0:2]:
            hours.append(i)

        for i in time_seperated[2:4]:
            minutes.append(i)

        for i in time_seperated[4:]:
            seconds.append(i)

        # turning the values into integers
        hours_in_string = ''.join(hours)
        hours_in_int = int(hours_in_string)

        minutes_in_string = ''.join(minutes)
        minutes_in_int = int(minutes_in_string)

        seconds_in_string = ''.join(seconds)
        seconds_in_int = int(seconds_in_string)
        the_date_holder.append(entry)

        how_long_sleep(hours_in_int, minutes_in_int, seconds_in_int)
        root.after(sleep_for,open_window)
        root.withdraw()
        root.after(sleep_for, root.deiconify)

# Building the gui itself
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="#696969")
frame.place(relwidth=1, relheight=1)


label = tk.Label(frame, text="Reminder", bg="#696969", font=("arial", 12))
label.place(relx=0.05, rely=0.01)

label = tk.Label(frame, text="Enter reminder:", bg="#21558c", font=("arial", 12))
label.place(relx=0.05, rely=0.19)

label = tk.Label(frame, text="Enter time in format:", bg="#21558c", font=("arial", 12))
label.place(relx=0.05, rely=0.37)

label = tk.Label(frame, text="Format: hours/minutes/seconds, 00/00/00, without the /", bg="#21558c", font=("arial", 12))
label.place(relx=0.05, rely=0.54)


reminder_entry = tk.Entry(frame, bg="white")
reminder_entry.place(relx=0.3, rely=0.19, relwidth=0.6)

time_entry = tk.Entry(frame, bg="white")
time_entry.place(relx=0.3, rely=0.37, relwidth=0.6)


button = tk.Button(frame, text="Set text", bg="#8b0000", command=lambda: get_text(reminder_entry.get()))
button.place(relx=0.91, rely=0.15)

button = tk.Button(frame, text="Set time", bg="#8b0000", command=lambda: date_limit(time_entry.get()))
button.place(relx=0.91, rely=0.37)


root.mainloop()
