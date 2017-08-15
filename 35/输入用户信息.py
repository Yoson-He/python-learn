import easygui as ui
fieldnames=['*用户名','*真实姓名','固话','QQ','*E-mail','*手机号码']
fieldvalues=[]
while 1:
    error=''
    temp=ui.multenterbox(fields=fieldnames,values=fieldvalues)
    if temp==None:
        break
    
    fieldvalues=[]
    for each in temp:
        fieldvalues.append(''.join(each.split()))
    
    for i in range(len(fieldnames)):
        if fieldnames[i][0]=='*' and fieldvalues[i]=='':
            error+=fieldnames[i]+'为必填项\n'
    if error!='':
        ui.msgbox(error)
    else:
        with open('用户信息.txt','w') as f:
            for i in range(len(fieldnames)):
                f.writelines(fieldnames[i]+':'+fieldvalues[i]+'\n')
        break
    
    
    




