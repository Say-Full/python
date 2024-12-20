import datetime

# mulai = datetime.datetime(2023, 5, 15, 8, 23, 22)
# selesai = datetime.datetime(2023, 5, 15, 8, 23, 32)

# print(selesai - mulai)


# Total durasi 
durasi1 = datetime.datetime.strptime("2:17:32", "%H:%M:%S")
dt1 = datetime.timedelta(hours=durasi1.hour, minutes=durasi1.minute, seconds=durasi1.second)

durasi2 = datetime.datetime.strptime("0:1:2", "%H:%M:%S")
dt2 = datetime.timedelta(hours=durasi2.hour, minutes=durasi2.minute, seconds=durasi2.second)

durasi3 = datetime.datetime.strptime("0:0:4", "%H:%M:%S")
dt3 = datetime.timedelta(hours=durasi3.hour, minutes=durasi3.minute, seconds=durasi3.second)

durasi4 = datetime.datetime.strptime("0:0:7", "%H:%M:%S")
dt4 = datetime.timedelta(hours=durasi4.hour, minutes=durasi4.minute, seconds=durasi4.second)

durasi5 = datetime.datetime.strptime("0:0:10", "%H:%M:%S")
dt5 = datetime.timedelta(hours=durasi5.hour, minutes=durasi5.minute, seconds=durasi5.second)

total_durasi = dt1 + dt2 + dt3 + dt4 + dt5
print(str(total_durasi))