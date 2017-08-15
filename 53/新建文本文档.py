# coding=utf-8
import urllib.request,chardet

#import os
f=open('新建文本文档.txt')
urllist = f.read().splitlines()
for each in urllist:
    re=urllib.request.urlopen('http://'+each).read()
    #print(re)
    #print('----------------')
    encode=chardet.detect(re)['encoding']
      
    if encode == 'GB2312':
        encode = 'GBK'
    print(encode)   
    sf=open('url_'+each+'.txt','w',encoding=encode)
    sf.writelines(re.decode(encode,'ignore'))
    sf.close()
f.close()
  

