import datetime , csv
midterm2path = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\midterm2.csv"
def findpro(datapath):
    fh = open(midterm2path, "r")
    csvfile = csv.DictReader(fh)

    statusDict = dict()
    for arow in csvfile:  #要把status 抓進 dict 去作計算
        status = arow ['Status']
        if status not in statusDict:
            statusDict[status] = 1
        else:
            statusDict[status] += 1
    fh.close() #養成關檔習慣
    return statusDict

statusDict = findpro(midterm2path)
# print(statusDict)   #測試是否成功
import matplotlib.pyplot as py
keys = list(statusDict.keys())  #存放key 要成為list
values = list(statusDict.values()) #存放values 要成為list
patches , texts , autotexts = py.pie(values, labels = keys, autopct = "%1.1f%%")
# py.show()
print(autotexts[2])