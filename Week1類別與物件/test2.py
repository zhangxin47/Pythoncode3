# def f1(a):
#     print(a)
# f1(3)
# d = dict()
# array = ['I','I','I','Y','X']
# for i in array:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

# midterm_sort_file = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\midterm2_sort.csv"
# midterm_sort2 = open(midterm_sort_file, "r", newline = "")
# midterm_sort_dict = csv.DictReader(midterm_sort2 , delimiter = "," )
# Dict_midterm2 = dict()
# problem_list = []
# Dict1 = dict()
# Dict2 = dict()
# status_list_header = ['Accepted', 'Compile Error', 'Runtime Error', 
# 'Time Limit Exceed', 'Wrong Answer']
# set_ori = [0,0,0,0,0]
# for i,j in zip(status_list_header,set_ori):
#     Dict1[i]=j
#     Dict2[i]=j
# def count(pp):
#     for arow in pp:
#         Dict_midterm2[arow ['Problem']] = arow ['Status']
#         problem_list.append (arow['Problem'])
#         if arow['Problem'] == '1':
#             if (arow ['Status'] not in Dict1):
#                 Dict1[arow['Status']] = 1
#             else:
#                 Dict1[arow['Status']] += 1
# def count2(pp):
#     for arow in pp:
#         Dict_midterm2[arow ['Problem']] = arow ['Status']
#         problem_list.append (arow['Problem'])
#         if arow['Problem'] == '2':
#             if (arow ['Status'] not in Dict2):
#                 Dict2[arow['Status']] = 1
#             else:
#                 Dict2[arow['Status']] += 1
# count2(midterm_sort_dict)
# count(midterm_sort_dict)

# print(problem_list , len(problem_list))
# print(Dict1)
# print(Dict2)
# # count_status(Dict_midterm2,problem_list)

import csv, datetime , csvsorter
midterm2path = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\Week1類別與物件\\midterm2.csv"
stuIDpath = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\Week1類別與物件\\stuID.csv"
stuID_test = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\Week1類別與物件\\stuIDtest.csv"
def findsubcnt(filepath):
    fh = open(filepath , "r",)
    csvfile = csv.DictReader(fh)

    stuDict = dict()  #建立一個dict 去紀錄學生繳交次數

    for arow in csvfile:
        sid = int(arow['StudentID']) #存成StudentID 數字
        if sid not in stuDict:
            stuDict[sid] = 1
        else:
            stuDict[sid] += 1
    fh.close
    return stuDict
#練習 把dict 作 輸出csv
def write_ans(stuIDpath , studentDict):
    fh2 = open(stuIDpath, "w", encoding = "utf-8", newline = "")
    headers = ['StudentID', 'Freq']
    csvfile_w = csv.DictWriter(fh2 , fieldnames = headers)
    csvfile_w.writeheader()
    for key in studentDict.keys():
        csvfile_w.writerow({headers[0] : int(key) , headers[1]: studentDict[key]})
    fh2.close()
def sorted_dict(studentDict , sortedcol):
    new_dict = dict()
    new_dict = sorted(studentDict.items() , key = lambda x:x[sortedcol])
    return new_dict
import collections
studentDict = findsubcnt(midterm2path) #建立一個dict 去紀錄學生繳交次數
print(studentDict)
Sort_studentDict = sorted_dict(studentDict, 1) #繳交次數排序
Sort_studentDict = collections.OrderedDict(Sort_studentDict) #轉成字典
write_ans(stuIDpath , Sort_studentDict)
print(Sort_studentDict)
# import matplotlib.pyplot as py
# seq = range (0, len(studentDict))
# width = 0.35
# py.xlim(0,max(studentDict.keys())) #設定xlim
# py.ylim(0,max(studentDict.values())) #設定ylim
# py.bar(sorted(studentDict.keys()) , studentDict.values(), width)
# # py.show()
# string = "我是愛你的"
# string = string[:-1]
# print(string)