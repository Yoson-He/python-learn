#-*- coding: utf-8 -*-
import os
import pdb

'''求目标路径下每种文件类型的文件数'''
def count_of_file_type(path):
    file_list= os.listdir(path)
    all_file_types=[]
    file_types=[]
    result=[]
    
    for each in file_list:
        temp=os.path.splitext(each)
        
        if temp[1] not in file_types:
            file_types.append(temp[1])#去重，保存文件类型
            
        all_file_types.append(temp[1])#保存每个文件的文件类型
        
    for each in file_types:
        if each=="":
            result.append(("文件夹",all_file_types.count(each)))
        else:
            result.append((each,all_file_types.count(each)))
            
    return result


'''求目标路径下每个文件的大小'''
def size_of_file(path):
    file_list= os.listdir(path)
    result=[]

    for each in file_list:
        result.append((each,str(os.path.getsize(each))+"bytes"))
        
    return result

'''在指定路径下查找目标文件'''
def find_file(path,file_name):
    result=[]
    
    for each in os.walk(path):
        if file_name in each[2]:
            result.append(os.path.join(each[0],file_name))
    return result


'''遍历路径下所有的子目录，返回格式：[('目标路径'，[包含的目录]，[包含的文件])]'''
def my_walk(path):   
    dir_list=[]
    file_list=[]
    result=[]
    
    for each in os.listdir(path):
         
        if os.path.isdir(each):
            dir_list.append(each)
            result.append(my_walk(os.path.join(path,each)))
        else:
            file_list.append(each)
    result.append((path,dir_list,file_list))
    return result

def output_the_paths_of_vidofiles(start_path):
    with open('vedioList.txt','w') as f:
        for each in os.walk(start_path):
            for eachFile in each[2]:
                fileType=os.path.splitext(eachFile)[1]
                if fileType in ('.mp4','.rmvb','.avi'):
                    f.write(os.path.join(each[0],eachFile)+'\n')
	
	
'''逐层遍历路径下的目录及子目录，查找指定关键字在所有文件中出现的位置（第几行第几个字符)'''
def select_the_keyword_from_current_dir(keyword):
    for each in os.walk(os.getcwd()):
        for eachFile in each[2]:
            if os.path.splitext(eachFile)[1] in ('.txt','.TXT'):
                filePath=os.path.join(each[0],eachFile)
                
                with open(filePath) as f:
                    lineNum=0
                    
                    for eachline in f:
                        lineNum+=1
                        charNum=0
                        
                        for eachchar in eachline:
                            charNum+=1
                            if eachchar==keyword:
                                print(filePath+"  :",lineNum,',',charNum)
                                break               
                     
                        
                    
                
                
    
