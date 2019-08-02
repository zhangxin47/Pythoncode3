import matplotlib.pyplot as py 
import datetime , csv ,os , math
# a是p1,p2商品免費時基礎需求量 b是價格敏感度, c1, c2成本, n iteration
def findequ(a, b, c1, c2, n):
    p2_ori = 0.0
    p1 = []  #皆為list 去作儲存
    p2 = []  #皆為list 去作儲存
    p1_ori = max((a +b * p2_ori + c1)/2, 0.0) # 首先 p2尚未進入市場，因此 p2 = 0  價格不為負
    p1.append(p1_ori)
    p2_ori = max((a +b* p1_ori + c2)/2 , 0.0) #價格不為負
    p2.append(p2_ori)
    q1 = [] #皆為list 去作儲存
    if (p1_ori > 0.0):
        q1_ori = a - p1[0] + b*p2[0]
        q1.append(q1_ori)
    else:
        q1_ori = 0.0
        q1.append(q1_ori)
    q2 = [] #皆為list 去作儲存
    if (p2_ori > 0.0):
        q2_ori = a - p2[0] + b*p1[0]
        q2.append(q2_ori)
    else:
        q2_ori = 0.0
        q2.append(q2_ori)
    for i in range(0, n-1): # n假如為2  原先ori為第一次iteration 再加上for的 0 共2次
        p1_next = max((a +b * p2[i] + c1)/2, 0.0) # 首先 p2尚未進入市場，因此 p2 = 0  
        p1.append(p1_next)
        p2_next = max((a +b* p1[i+1] + c2)/2 ,0.0)
        p2.append(p2_next)
        if (p1_next > 0.0):
            q1_next = a - p1[i+1] + b*p2[i+1]
            q1.append(q1_next)
        else:
            q1_next = 0.0
            q1.append(q1_next)
        if (p2_next > 0.0):
            q2_next = a - p2[i+1] + b*p1[i+1]
            q2.append(q2_next)
        else:
            q2_next = 0.0
            q2.append(q2_next)
    return p1 , p2, q1, q2
def print_ans(p1, p2, n):
    out_p1 = p1[n-1]
    out_p2 = p2[n-1]
    print("在%d iteration p1價格為: %.2f , p2價格為: %.2f" %(n, out_p1, out_p2))

#利用 map(float, input) 去輸入多個變數並存成 float ，並建立參數設定
while 1:  
    a, b, c1 , c2, n = map(float, input("Please input a b c1 c2 n value:").split(","))
    n = int(n) #把float 換成int
    if ((10 <= a <=10000) and (0 <= b < 1) and (0 < c1 <= a) and (0 < c2 <=a) and (0 <= n <=10)):
        break #符合敘述
    else:
        print("參數設定不正確，請重新輸入")
        continue
p1 , p2 , q1 , q2 = findequ(a, b, c1, c2, n)
print_ans(p1, p2, n)
print(p1)
print(p2)