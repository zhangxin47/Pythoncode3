import tkinter as tk
import tkinter.font as tkFont
import math, os
import matplotlib.pyplot as pyplot
from PIL import ImageTk 

class Plotter(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) #將tk.Frame 基本類別產生，才能作gird&
        self.grid()
        self.creatwidget()
    def creatwidget(self):
        f1 = tkFont.Font(size = 16 , family = "Courier New")
        self.labx = tk.Label(self, text = "X:", height = 1, width = 3,\
            font = f1)
        self.laby = tk.Label(self, text = "Y:", height = 1, width = 3, \
            font = f1)
        self.txtx = tk.Text(self, height = 1, width = 40 , font = f1)
        self.txty = tk.Text(self, height = 1, width = 40 , font = f1)
        self.btnload = tk.Button(self, text = "Plot!",height = 1, \
            width = 5,command = self.click_btn_load, font = f1)
        #畫布 ， width & height 為 畫素
        self.cvs = tk.Canvas(self, width = 800, height = 600, bg = "white")
        #放置 grid 固定位置
        self.labx.grid(row = 0, column = 0, sticky = tk.E)
        self.laby.grid(row = 1, column = 0, sticky = tk.E)
        self.txtx.grid(row = 0, column = 1, sticky = tk.NE + tk.SW)
        self.txty.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.btnload.grid(row = 0 ,rowspan = 2, column = 2,sticky =tk.NE+ tk.SW)
        self.cvs.grid(row = 2, column = 0, columnspan = 3,sticky = tk.NE+ tk.SW)
    def click_btn_load(self):
        x = self.txtx.get("1.0",tk.END).split(",")  #先將字串用split分開，分開時為字串
        for i in range(len(x)): #將其轉成float()
            x[i] = float(x[i])
        y = self.txty.get("1.0", tk.END).split(",")
        for i in range(len(y)): 
            y[i] = float(y[i])
        self.makescatter(x,y)
        self.imageMain = ImageTk.PhotoImage(file = "C:\\Users\\b1013\\Desktop\\Pythoncode3\\tep.png")
        self.cvs.create_image(400, 300, image = self.imageMain, anchor = tk.CENTER)
        os.system("del tep.png")
    def makescatter(self, x, y):
        fig = pyplot.figure()  #空的圖
        ax = fig.add_subplot(111)  #因已存在 fig 因此只能用add_subplot
        pyplot.plot(x, y, "bo")
        rangeX = max(x) - min(x)
        rangeY = max(y) - min(y)
        pyplot.xlim(min(x) - 0.1 * rangeX, max(x) + 0.1 * rangeY)
        pyplot.ylim(min(y) - 0.1 * rangeY, max(y) + 0.1 * rangeY)
        for i,j in zip(x,y):
            ax.annotate("(%.2f,%.2f)"%(i,j) , xy = (i,j))  #因格式本身要求字串 則再轉換.2f
        pyplot.savefig("tep.png")
p1 = Plotter()
p1.master.title("My plotter")
p1.mainloop()