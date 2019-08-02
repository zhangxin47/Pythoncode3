import matplotlib.pyplot as py
import csv , datetime
# py.subplot(111)
# x = range(1 , 6)
# y = [4, 2, 5 , 1, 6]
# py.yticks(range(1,8))
# py.plot(x , y , 'or-' , label = 'y = x + 2')
# py.legend()
# py.show()
midtermfile = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\midterm2.csv" #原始檔案位置
def findSubTime(midtermfile):
    fh = open(midtermfile, "r")
    csvfile = csv.DictReader(fh)

    subtime = []
    for row in csvfile:
        dt = datetime.datetime.strptime(row['SubmissionTime'], "%H:%M:%S").time()
        sub = (dt.hour - 9) * 3600 + (dt.minute - 20) *60 + dt.second
        subtime.append(sub)
    fh.close()
    return subtime
subtime = findSubTime(midtermfile)

py.hist(subtime, bins = range(0, 12000, 1000), color = "gray", edgecolor = "black")
n , bins , patches = py.hist(subtime, bins = range(0, 12000, 1000))
py.xlim(0,11000)
py.ylim(0,120)
py.title("Hist of submission time")
py.xlabel("submission time")
py.ylabel("freq")
# print(n) #frequency 每個endpoint內的個數
# print(bins) #endpoint histogram的切點
py.show()