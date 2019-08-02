import matplotlib.pyplot as py
import csv, datetime
import numpy as np
# open the file
ubikefile = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\Week2 matplotlib\\ubike.csv"
f = open(ubikefile, "r")
bike = {}   #dict 去存取幾點有幾輛bike
capacity = {}  #dict 去存取幾點有多少停車格
count = {}  #dict 去存取幾點有多少資料量  31天
# lot - bike - empty = 故障數
# processing the data
for row in csv.DictReader(f):
    if row["station"] == "Roosevelt & Xinsheng S. Intersection":
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if hour not in bike:
            bike[hour] = int(row["bike"])
            capacity[hour] = int(row["lot"])
            count[hour] = 1
        else:
            bike[hour] += int(row["bike"])
            capacity[hour] += int(row["lot"]) 
            count[hour] += 1 
        print(row)
f.close()

# preparing for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []  # 0~23點 平均有多少bike數量可以借
lot = []  # 0~23點 平均有多少停車格 
for k in time_seq:
    avg.append(float(bike[k]) / count[k])   #一天有24個時點 因此有24筆資料 ,count 有31天的資料量
    lot.append(float(capacity[k]) / count[k])
    
# plotting the data in avg and lot

py.plot(time_seq, lot, label = "Capacity") #lot 紀錄的是此站點的Capacity
py.plot(time_seq, avg, label = "Average") #avg 紀錄平均此站點可借出bike數
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
py.ylim(0, max(lot)+30)
py.xticks(time_seq)
py.legend(loc = "upper right")
py.show()