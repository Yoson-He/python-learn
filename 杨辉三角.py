'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1

'''
def t():
    list1=[1]
    while True:
        yield list1
        temp=[]
        lenght=len(list1)
        if lenght==1:
            temp=[1,1]
        else:
            for j in range(lenght+1):
                if j==0 or j==lenght:
                    temp.append(1)
                else:
                    temp.append(list1[j-1]+list1[j])        
        list1=temp

g=t()
i=10
for each in g:
    print(each)
    i-=1
    if i==0:
        break
    
