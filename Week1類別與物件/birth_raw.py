# 看是否為閏年
def isleap(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

def isvaliddate(birth):
    year , month, day = birth.split("/")
    year = int(year)
    month = int(month)
    day = int(day)
    if (1 <=year <= 3000) and (1 <= month <= 12):
        daysin_month = [31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30 ,31]
        if isleap(year) == True:
            daysin_month[1] = 29
        if 1<= day <= daysin_month[month-1]:
            return True
    return False

# 作一個名字與生日的Dict
namebirth = dict()
while True:
    name = str(input("input your name:"))
    if name == "":  #如果名字為空字串代表結束
        break
    
    birth = str(input("input your birth date:"))
    if birth == "":  #如果生日為空字串代表結束
        break
    # namebirth [name] = birth
    if isvaliddate(birth) == True:
        if name not in namebirth.keys():
            namebirth [name] = [birth]
        else:
            namebirth [name].append(str(birth))
    else:
        print("日期格式錯誤!")
print(namebirth)