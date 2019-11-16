
import time

hours = []
minutes = []
seconds = []

the_text = input("What would you like to be reminded of? ")

#opening txt file to write reminder in
try:
    reminder_file = open("reminder.txt", "w")
    reminder_file.write(the_text)
    reminder_file.close()

except IOError:
    print("The file is not found, please find the correct one and rerun the program.")


#opening txt file to read it later on
reminder_file1 = open("reminder.txt", "r")



#getting when the user wants to be notified
print("Please use this format, Hour/minute/second, without the, / ,limit 6 numbers")
hour = input("When would you like to be reminded?")


#checking to see if input is a number and making sure its only 6 values
while hour.isdigit() == False and len(hour) == 6:
    hour = input("Please input it in the format hour/minute/second ")
else:
    time_seperated = list(hour)


# putting it into a list to make divide the values into their respective parts
for i in time_seperated[0:2]:
    hours.append(i)

for i in time_seperated[2:4]:
    minutes.append(i)

for i in time_seperated[4:]:
    seconds.append(i)

#turning the values into integers
hours_in_string = ''.join(hours)
hours_in_int = int(hours_in_string)

minutes_in_string = ''.join(minutes)
minutes_in_int = int(minutes_in_string)

seconds_in_string = ''.join(seconds)
seconds_in_int = int(seconds_in_string)

# putting the function to sleep for how ever long the user requested
def how_long_sleep(the_hour, the_minute, the_second):
    sleep_for = (3600 * the_hour) +  (60 * the_minute) + (the_second)
    time.sleep(sleep_for)
    print(reminder_file1.read())
    reminder_file1.close()

#calling the reminder when the user requested
how_long_sleep(hours_in_int, minutes_in_int, seconds_in_int)
