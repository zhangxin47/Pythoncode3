class youtuber:
    subnum = 0
    totalclicknum = 0
    def __init__(self, chanelname, field):
        self.chanelname = chanelname
        self.field = field
    def predictrevenue(self, totalclicknum, sponser_rev):
        prerev = totalclicknum /1000000 * 30000 + sponser_rev
        return prerev
    def __str__(self):
        return self.tostr()
    def tostr(self):
        printstr = "Youtube: " + self.chanelname + "在 "+ self.field + " 領域賺了:" 
        return printstr
Tsaibro = youtuber("Tsaibrother", "embarrassment")
Tsaibro.subnum = 190000
prerev = Tsaibro.predictrevenue(1200000, 15000)
print(Tsaibro , str(prerev))