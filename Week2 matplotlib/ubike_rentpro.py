import csv, os, datetime 
import matplotlib.pyplot as py 
ubikefile = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\Week2 matplotlib\\ubike.csv"
f = open(ubikefile , "r")

station = {} #ubike 站點資訊
count = {}  # 登記此id 總數 
lat = {}  #緯度
lon = {}  #經度
capacity = {} #總停車格數量
for row in csv.DictReader(f):
    time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
    time = time.hour
    if time == 17 or time == 18:  #只先分析下午五點與六點資訊
        id = int(row["id"])
        if id not in station:
            lat[id] = float(row["latitude"])  #緯度
            lon[id] = float(row["longitude"]) #經度
            capacity[id] = int(row["lot"])  #總停車格數量
            station[id] = int(row["bike"])  #此站點17 & 18時可提供借車數量
            count[id] = 1   #登記此id 總數 
        else:
            station[id] += int(row["bike"])
            capacity[id] += int(row["lot"])
            count[id] += 1
f.close()
id_seq = station.keys()
id_seq = sorted(id_seq)   #30個id
redlat = [] 
redlon = [] 
yellowlat = [] 
yellowlon = [] 
greenlat = [] 
greenlon = [] 
bluelat = [] 
bluelon = [] 
for k in id_seq:  #針對此30個id 作計算
    capacity[k] = float(capacity[k]) / count[k] #總停車格數量 / 紀錄資料數量
    """
    此為 (該id站點 平均可借ubike 數量 / 該id站點平均停車格數量)因此為借車比例 
    比例高代表ubike在此點不熱絡使用，比例低為好事
    """
    station[k] = (float(station[k]) / count[k]) / capacity[k] 
    if station[k] < 0.2:
        redlat.append(lat[k])
        redlon.append(lon[k])
    elif 0.2 <= station[k] < 0.3:
        yellowlat.append(lat[k])
        yellowlon.append(lon[k])
    elif 0.3 <= station[k] < 0.4:
        greenlat.append(lat[k])
        greenlon.append(lon[k])
    else:
        bluelat.append(lat[k])
        bluelon.append(lon[k])

# plotting the data 
py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
py.plot(redlat, redlon, "ro" , label = "<20%")
py.plot(yellowlat, yellowlon, "yo", label = "20%~30%")
py.plot(greenlat, greenlon, "go", label = "30%~40%")
py.plot(bluelat, bluelon, "bo", label = ">=40%  ")
py.axis([25.01,25.05,121.52,121.56])
py.legend(loc = "lower right")
py.show()