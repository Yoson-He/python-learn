import easygui as ui
import os
filename=ui.fileopenbox()
with open(filename) as f:
    text=f.read()
    
    newtext=ui.textbox(msg='文件“'+os.path.split(filename)[1]+'”的内容如下：',text=text)
    
choices=['覆盖保存','不保存','另存为']
if text!=newtext[:-1]:#textbox返回的文本
    case=ui.buttonbox(msg='文件发生改变，是否要保存？',choices=choices)
        
    if case==choices[0]:
        with open(filename,'w') as f:
            f.writelines(newtext)
    elif case==choices[2]:
        with open(ui.filesavebox(default='.txt'),'w') as f:
            f.writelines(newtext)
            
    else:
        pass
