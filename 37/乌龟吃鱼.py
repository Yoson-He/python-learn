import random
class Tortoise():
    def __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
        self.hp=100
        
    def move(self):
        self.setp=random.randint(1,2)
        self.direction=random.choice('xy')
        
        if self.direction=='x':
            if self.x==10:
                self.x-=self.setp
            else:
                self.x+=self.setp
                
        if self.direction=='y':
            if self.y==10:
                self.y-=self.setp
            else:
                self.y+=self.setp
                
        self.hp-=1
        
    def eat(self):
        self.hp+=20
            if self.hp>100:
                self.hp=100
        
class  Fish():
    def __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)

    def move(self):
        self.setp=1
        self.direction=random.choice('xy')
        
        if self.direction=='x':
            if self.xself.setp>10:
                self.x-=self.setp
            else:
                self.x+=self.setp
                
        if self.direction=='y':
            if self.y+self.setp>10:
                self.y-=self.setp
            else:
                self.y+=self.setp

a=Tortoise()
b=[Fish()for i in range(10)]

while a.hp>0 and len(b)>0:
    print('乌龟当前位置：[%s，%s],hp：%d' %(a.x,a.y,a.hp))
    length=len(b)
    print('当前鱼儿的数量:%d' % length)
    
    a.move() 
    for i in range(length):
        b[i].move()
    temp=[]     
    for i in range(length):   
        if (a.x==b[i].x and a.y==b[i].y):
            a.eat()
            temp.append(b[i]) #存储需要清理的鱼
            
    for each in temp:
        print('吃掉了一条鱼！')
        b.remove(each) #清理被吃掉的鱼
    temp.clear()
    
    
        
if a.hp==0:
    print('乌龟没体力了，游戏结束')
else:
    print('鱼被吃完了，游戏结束')
