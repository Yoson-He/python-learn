'''利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。'''
def f(s):
    return s.title()

#print(list(map(f,['adam', 'LISA', 'barT'])))

#--------------------------------
def not_empty(s):
    return s and s.strip()

#print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


#--------------------------------

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):

    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
'''
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''
#--------------------------------

def is_palindrome(num):
    list1=list(str(num)).reverse()
    return list1==list(str(num))

#output = filter(is_palindrome, range(1,1000))
#print(list(output))

#--------------------------------

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2=sorted(L,key=by_name)
#print(L2)

def by_score(t):
    return t[1]

L2=sorted(L,key=by_score)
#print(L2)



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        print("i=",i)
        fs.append(f)
    return fs

#f1, f2, f3 = count()
#print(f1(),f2(),f3())

def log(func):
    def wrapper():
        print('call %s():' % func.__name__)
        return func()
    return wrapper

@log
def now():
    print('2015-3-25')


















