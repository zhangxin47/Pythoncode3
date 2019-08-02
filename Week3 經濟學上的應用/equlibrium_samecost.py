import csv , datetime 
import matplotlib.pyplot as py
def findequ(a , c, n):
    # the first time
    q1 = []
    q2 = []
    q1_original = (a - c) / 2 #此時沒有q2進來市場
    q1.append(q1_original)
    q2_original = (a - q1_original - c)/2 
    q2.append(q2_original)

    for i in range(0, n+1):
        q1_next = (a - q2[i] - c) /2
        q1.append(q1_next)
        q2_next = (a - q1[i+1]-c) /2
        q2.append(q2_next)
    return q1, q2
def printans(q1, q2, n):
    for i in range(0, n+1):
        print("第 %d 次iteration結果為:(%.4f , %.4f , %d)" % (i+1,q1[i],q2[i], i+1) )
def ploteq(q1, q2, a, c, n):
        ub1 = (a - c) /2 *2.5
        ub2 = (a - c) /2* 2.5
        ub = max(ub1,ub2)
        #axes 把圖給畫大
        py.plot([0,0],[ub,-1], "k--")
        py.plot([ub,-1],[0,0], "k--")
        #best response
        py.plot([0,0], [ub, a-c], "g")
        py.plot([0,(a-c)/2],[a-c,0], "g")
        py.plot([ub, a-c],[0,0],"r")
        py.plot([a-c,0],[0, (a-c)/2],"r")
        for i in range(n):
                q1cur = q1[i]
                q2cur = q2[i]
                q1next = q1[i+1]
                q2next = q2[i+1]
                
                py.plot([q1cur, q1next], [q2cur, q2cur],"g" ,linewidth = 2.0)
                py.plot([q1next, q1next], [q2next, q2cur],"r" , linewidth = 2.0)
        q1equ = (a - c)/3
        q2equ = (a - c)/3
        py.plot([q1equ], [q2equ], "ob")
        py.plot([q1[0]],[q2[0]], "ob")

        #axes 補充
        py.axis([-1 , ub, -1, ub])
        py.xlabel = "Q of product1"
        py.ylabel = "q of product2"
        py.show()

a = 10.0 #市場想買的人所能帶給的收益
c = 2.0  #成本
n = 10 #作10次
q1, q2 = findequ(a , c , n)  #想作10次iteration
printans(q1,q2,n)
ploteq(q1, q2, a , c, n)
