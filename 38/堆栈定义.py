class Stack:
    def __init__(self,start=[]):
        self.data=[]
        for each in start:
            self.push(each)
        
    def isEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def push(self,x):
            self.data.append(x)

    def pop(self):
        if self.isEmpty():
            print('栈为空')
        else:
            return self.data.pop()

    def top(self):
        if self.isEmpty():
            print('栈为空')
        else:
            print(self.data[-1])

    def bottom(self):
        if self.isEmpty():
            print('栈为空')
        else:
            print(self.data[0])
