import time

hours = []
minutes = []
seconds = []


print("Hour/minute/second")
hour = input("Please input it in the format hour/minute/second ")


while hour.isdigit() == False:
    hour = input("Please input it in the format hour/minute/second ")
else:
    time_seperated = list(hour)



for i in time_seperated[0:2]:
    hours.append(i)

for i in time_seperated[2:4]:
    minutes.append(i)

for i in time_seperated[4:]:
    seconds.append(i)


hours_in_string = ''.join(hours)
hours_in_int = int(hours_in_string)

minutes_in_string = ''.join(minutes)
minutes_in_int = int(minutes_in_string)

seconds_in_string = ''.join(seconds)
seconds_in_int = int(seconds_in_string)


def how_long_sleep(the_hour, the_minute, the_second):
    sleep_for = (3600 * the_hour) +  (60 * the_minute) + (the_second)
    time.sleep(sleep_for)
    print("Your reminder!")

how_long_sleep(hours_in_int, minutes_in_int, seconds_in_int)
