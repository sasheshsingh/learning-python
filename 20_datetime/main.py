import datetime

date = datetime.date(2025, 10, 10)

print(date)

today = datetime.date.today()

print(today)

time = datetime.time(10, 30,0)

print(time)

now = datetime.datetime.now()

print(now)

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)

current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
