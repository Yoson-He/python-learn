import random

def int_input(temp):
    while 1:
        try:
            int(temp)
        except ValueError:
            temp = input('输入有误，请输入整数：')
        else:
            return (int(temp))
def gusse():   
    secret = random.randint(1,10)
    temp = input("不妨猜一下我现在心里想的是哪个数字：")
    guess = int_input(temp)
    while guess != secret:
        temp = input("哎呀，猜错了，请重新输入吧：")
        guess = int_input(temp)
        if guess == secret:
            print("我草，你是我心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    print("游戏结束，不玩啦^_^")


try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
else:
    f.close()
