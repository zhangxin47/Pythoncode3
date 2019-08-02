# 看是否為閏年 ， 定義為global function 因為不是只有Date class可呼叫
def isleap(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

def strToDate(birth):
    d = Date()
    year , month, day = birth.split("/")
    d.year = int(year)
    d.month = int(month)
    d.day = int(day)
    return d

def printbirth(namebirth):  #把Dict 丟入 副程式做輸出
    for i in namebirth.keys():
        Dateobject = namebirth[i] #把每一個姓名對到其Dateobject
        print(i,"was born at", Dateobject.tostr())

class Date:   #Date 是一個class 內含isvaliddate這個operation
    def isvaliddate(self): # instance function ， birth 已是date object 含 year month day 
        if (1 <= self.year <= 3000) and (1 <= self.month <= 12):
            daysin_month = [31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30 ,31]
            if isleap(self.year) == True:
                daysin_month[1] = 29
            if 1<= self.day <= daysin_month[self.month-1]:
                return True
        return False
    def tostr(self): # instance function ，把數值轉為字串輸出
        return str(self.year) + "/" + str(self.month) + "/" + str(self.day)
    def isleap(self): 
        return isleap(self.year)  #放進global function

# 作一個名字與生日的Dict
namebirth = dict()
while True:
    name = str(input("input your name:"))
    if name == "":  #如果名字為空字串代表結束
        break
    
    birth = str(input("input your birth date:"))
    if birth == "":  #如果生日為空字串代表結束
        break
    birth = strToDate(birth) #把字串轉為 class
    # namebirth [name] = birth
    if birth.isvaliddate() == True:  #因birth已是classes 因此可呼叫instance function
        if name not in namebirth.keys():
            namebirth [name] = birth
        else:
            print("你已重複輸入，資料紀錄會覆蓋哦!")
            namebirth [name] = birth
            # namebirth [name].append(birth)
    else:
        print("日期格式錯誤!")
printbirth(namebirth) #丟入 namebirth Dict