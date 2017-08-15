import random as r
import math as m

class Point:
    def __init__(self):
        self.x=r.randint(-10,10)
        self.y=r.randint(-10,10)

class Line():
    def __init__(self,p1,p2):
        self.x=p1.x-p2.x
        self.y=p1.y-p2.y
        

    def getLen(self):
        self.lenth=m.sqrt(self.x*self.x+self.y*self.y)
        return self.lenth
    
p1=Point()
p2=Point() 
line=Line(p1,p2)
print(line.getLen())
