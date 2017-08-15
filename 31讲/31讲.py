import pickle
import os

def split_file(file_name):
    p=1
    boy=[]
    girl=[]
    f = open(file_name)
    for each_line in f:
        if each_line[:4]=="小甲鱼:":
            boy.append(each_line[4:])
        if each_line[:4]=="小客服:":
            girl.append(each_line[4:])
            
        if each_line[:3]=="===":
            save_file('girl_'+str(p)+'.txt',girl)
            save_file('boy_'+str(p)+'.txt',boy)
           
            boy=[]
            girl=[]
            p+=1
            
    save_file('girl_'+str(p)+'.txt',girl)
    save_file('boy_'+str(p)+'.txt',boy)

    f.close()

def save_file(file_name,data):
    f=open(file_name,'wb')
    pickle.dump(data,f)
    f.close()
    

#split_file('record.txt')

file_list=os.listdir('E:\\python学习笔记\\31讲')
for each_file in file_list:
    if ('boy' in each_file) or ('girl' in each_file):
        f=open(each_file,'rb')
        data=pickle.load(f)
        for each_line in data:
            print(each_line)
        f.close()

