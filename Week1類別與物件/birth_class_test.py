# 看是否為閏年 ， 定義為global function 因為不是只有Date class可呼叫
def isleap(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

# def strToDate(birth):
#     d = Date()
#     year , month, day = birth.split("/")
#     d.year = int(year)
#     d.month = int(month)
#     d.day = int(day)
#     return d

def printbirth(namebirth):  #把Dict 丟入 副程式做輸出
    for i in namebirth.keys():
        Dateobject = namebirth[i] #把每一個姓名對到其Dateobject
        print(i,"was born at", Dateobject.tostr())

class Date:   #Date 是一個class 內含isvaliddate這個operation
    doubledigit = False
    @staticmethod #說明接下來為 staticmethod
    def setdoubledigit(dd):
        Date.doubledigit = dd
    def __init__(self, year, month, day):  # constructor , 初始class 會執行的動作
        self.year = year
        self.month = month
        self.day = day
    def isvaliddate(self): # instance function ， birth 已是date object 含 year month day 
        if (1 <= self.year <= 3000) and (1 <= self.month <= 12):
            daysin_month = [31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30 ,31]
            if isleap(self.year) == True:
                daysin_month[1] = 29
            if 1<= self.day <= daysin_month[self.month-1]:
                return True
        return False
    def tostr(self): # instance function ，把數值轉為字串輸出
        if Date.doubledigit == False:
            return str(self.year) + "/" + str(self.month) + "/" + str(self.day)
        else:
            datestr = str(self.year) + "/"
            if self.month < 10:
                datestr += "0" + str(self.month) + "/"
            else:
                datestr += str(self.month) + "/"
            if self.day < 10:
                datestr += "0" + str(self.day) + "/"
            else: 
                datestr += str(self.day) 
            return datestr
    def __str__(self): # constructor , 作為print tostr 的 operations
        return self.tostr()
    def isleap(self): 
        return isleap(self.year)  #放進global function
    def islater(self, day2):
        if self.year > day2.year:
            return True
        elif self.year == day2.year:
            if self.month > day2.month:
                return True
            elif self.day > day2.day:
                return True
        return False
# test constructor
d = Date(2018, 5, 25)
print(d.year)
Date.setdoubledigit(True)
d2 = Date(2019, 3, 28)
print(d2)