import os
import easygui as ui

temp=os.walk(ui.diropenbox())#walk()遍历目标路径,返回一个三元组:(路径,[包含目录],[包含文件])
number_of_files=0
number_of_lines=0

for each in temp:
    for eachFile in each[2]:
        if os.path.splitext(eachFile)[1] == '.py':
            number_of_files+=1
            filePath=os.path.join(each[0],eachFile)
            with open(filePath) as f:
                for eachline in f:
                    number_of_lines+=1
ui.textbox(text='[.py]源文件%d个,源代码%d行',number_of_files,number_of_lines)
      
