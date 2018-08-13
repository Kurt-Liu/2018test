# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # __author: 金鑫
# # 2018/4/8
# Python11	期第二次考试（基础数据类型与函数部分）
# 考试时长：3个小时										满分：105分
# 一，选择题（每题2分，共24分）
# 1、python不支持的数据类型有 A
#
# A、char
#
# B、int
#
# C、float
#
# D、list
# 2、
#
# x = “foo”
#
# y = 2
#
# print(x+y) E
#
# 	A.foo	 B.foofoo	   C.foo2     D.2	   E.TypeError
#
# 3、关于字符串下列说法错误的是 A
#
# A、字符应该视为长度为1的字符串
#
# B、字符串可以转化成数字
#
# C、既可以用单引号，也可以用双引号创建字符串
#
# D、在三引号字符串中可以包含换行回车等特殊字符
#
# 4、以下不能创建一个字典的语句是 C
#
# A、dic1 = {}
#
# B、dic2 = {123:345}
#
# C、dic3 = {[1,2,3]:'uestc'}
#
# D、dic3 = {(1,2,3):'uestc'}
#
# 5、Kvps = {‘1’:1,’2’:2} D
#
# theCopy = kvps
#
# kvps[‘1’] = 5
#
# sum = kvps[‘1’] + theCopy[‘1’]
#
# print(sum)
#
# A.1       B.2        C.7	       D.10
#
# 6、已知x=43，ch=‘A’，y = 1，则表达式(x>=y and ch <‘b’ and y)的值是 B

# A、0      B、1     C、出错     D、True
# 7、下列Python语句正确的事（多选） A,D
#
# A、min = x if x < y else y
#
# B、max = x > y ? x : y
#
# C、if(x>y) print(x)
#
# D、while True:pass
#
# 8、若k为整形，下述while循环执 的次数为：B
# k=1000
# while k>1:
#     print(k)
#     k=k/2
#
# 	A.9	       B.10       C.11	     D.100
# 9、以下叙述正确的是：B
# A、continue语句的作用是结束整个循环的执行
# B、只能在循环体内使用break语句
# C、在循环体内使用break语句或continue语句的作用相同
# D、从多层循环嵌套中退出时，只能使用goto语句
# 10、下面的语句哪个会无限循环下去：B
#
# A、for a in range(10):
# time.sleep(10)
#
# B、while 1<10:
# time.sleep(10)
#
# C、while True:
# break
#
# D、a = [3,-1,',']
# for i in a[:]:
#  	if not a: break
# 11、下列说法正确的是(多选,选错不得分)：C
# A，
# a = [1,2,3]
# b = [1,2,3]
# a与b指向同一个内存地址。
# B，
# i1 = 356
# I2 = 356
# i1 与 i2是同一个内存地址。
# C，
# s1 = ‘laonanhai’
# s2 = ‘laonanhai’
# s1 与 s2 是同一个内存地址。
# D，tu = (1) tu是元组类型。
# 12、下面的代码，哪些会输出1,2,3三个数字(多选,选错不得分): B
# A、
# for i in range(3):
#
#     print(i)
#
#     print(i+1)
# B、
# aList = [0,1,2]
# 		   for i in aList:
#    		   print(i+1)
# C、
# 	    i = 1
# 	    while i < 3:
#               print(i)
#     	      i+=1
# D、
# 	    for i in range(3):
#                print(i+1)
# 二，简答题（共42分）
# 1、is 和 == 的区别 （2分）
#
# 2、Python 如何实现tuple和list的转换。（2分）
#
# 3、list和tuple有什么不同 （2分）
#
# 4、*args和**kwargs在什么情况下会使到？请给出使 **kwargs的事例（2分）
#
# 5、Python中什么数据类型存在小数据池？小数据池有什么作用？（2分）
#
# 6、在Python3x版本中，s1 = ‘老男孩’，如何将s1转化成utf-8的bytes类型？转化成功之后，得到了s2，如何将s2转化成gbk的bytes类型（请写出具体代码）？（3分）
#
# 7、有如下操作，最后dic的结果是什么？为什么？（2分）
# dic = dict.fromkeys(['barry','alex',],[])
# dic['barry'].append(666)
# 	print(dic)
#
# 8、请描述unicode,utf-8,gbk等编码之间的关系？（2分）
#
# 9、l = [1,1,2,2,3,4,5,5,6,6,7,8]将此列表去重。（2分）
# 	10、有如下代码，写出最后结果，并解释为什么。（3分）
# l1 = [1,[22,33,44],3,4,]
# l2 = l1
# 	l3 = l1.copy()
# l1.append(666)
# 	l1[1].append('55')
# Print(l1,l2,l3)
#
# 11、有如下代码，说出l1与l2的关系？（2分）
# l1 = [1,2,3,4,5]
# l2 = l1[:]
#浅copy
# 12、‘1,2,3’如何变成[‘1’,’2’,’3’]？ [‘1’,’2’,’3’]如何变成[1,2,3]?（写具体代码）（4分）
# s1 = '1,2,3'
# print(s1.split(','))
# print([int(i) for i in ['1','2','3']])

# 13、如何生成[1,4,9,16,25,36,64,81,100]尽量用一行实现。（2分）
#
# 14、map(str,[1,2,3,4,5,6,7,8,9])输出什么？（2分）
#
# 15、下面代码输出结果是什么？两次list1的结果相同么？为什么？（4分）
# def extendList(val,list=[]):
#     	list.append(val)
#     	return list
# 	list1 = extendList(10)
# print('list1=%s'%list1)
# 	list2 = extendList(123,[])
# print('list2=%s'%list2)
# 	list3 = extendList('a')
# print('list3=%s'%list3)
# 	print('list1=%s'%list1)
# 16、下面代码的执行结果是什么？为什么？（4分）
#  a = 1
# 	 def func1():
#      	a += 1
#     	print(a)
# 	 func1()
# 这段代码呢？
# def wrapper():
#           a = 1
#           def inner():
#               a += 1
#               print(a)
#           inner()
# 	   wrapper()
# 17、什么是闭包（closure），为什么要用它？（2分）
#
# 三，代码题。
#
# 1、用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# 	name=[‘oldboy’,'alex','wusir']（4分）
# name=['oldboy','alex','wusir']
# for i in map(lambda x:x+'_sb',name):
#     print(i)

# 2，用filter函数过滤出单价大于100的股票。（4分）
# portfolio = [
#     {'name':'IBM','shares':100,'price':91.1},
#     {'name':'AAPL','shares':50,'price':543.22},
#     {'name':'FB','shares':200,'price':21.09},
#     {'name':'HPQ','shares':35,'price':31.75},
#     {'name':'YHOO','shares':45,'price':16.35},
#     {'name':'ACME','shares':75,'price':115.65}]
# for i in filter(lambda x:x['price'] > 100, portfolio):
#     print(i)



# 3，有文件t1.txt里面的内容为：（6分）
# id,name,age,phone,job
# 		1,alex,22,13651054608,IT
# 		2,wusir,23,13304320533,Tearcher
# 		3,taibai,18,1333235322,IT
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},
# ......]
# l1 = []
# with open('t1.txt',encoding='utf-8') as f1:
#     name_list = f1.readline().strip().split(',')
#     for i in f1:
#         dic = {}
#         i_list = i.strip().split(',')
#         for j in range(len(i_list)):
#             dic[name_list[j]] = i_list[j]
#         l1.append(dic)
# print(l1)

#
# 4，写程序完成下列功能：(20分，有5分加分项，共计25分)
#
# 1)，启动程序，首页面应该显示成如下格式：
#     欢迎来到博客园首页
#     1:请登录
#     2:请注册
#     3:文章页面
#     4:日记页面
#     5:评论页面
#     6:收藏页面
#     7:注销
#     8:退出程序
# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程	序运行，成功之后，可以选择访问3~6项，访问页面之前，必须要在log文件中打印日志，	日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，访问页面时，页面内容为：欢	迎xx用户访问评论（文章，日记，收藏）页面
# 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录（完成自动登录+5	分），然后进入首页选择。
# 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
# 6)，退出程序为结束整个程序运行。
status_dic = {
    'username': None,
    'status': False,
}

flag1 = True

def login(*args,**kwargs):
    i = 0
    while i < 3:
        if args:
            status_dic['username'] = args[0]
            status_dic['status'] = True
            return True
        else:
            username = input('请输入用户名：').strip()
            password = input('请输入密码：').strip()
            with open('register',encoding='utf-8') as f1:
                for line in f1:
                    line_list = line.strip().split()
                    if username == line_list[0] and password == line_list[1]:
                        print('登录成功')
                        status_dic['username'] = username
                        status_dic['status'] = True
                        return True
                else:
                    print('输入不正确，请重新输入,还剩%s机会' % (2-i))
                    if i == 2: return Quit()
                i += 1


def register(*args, **kwargs):
    flag = True
    while flag:
        username = input('请输入要注册的用户名:')
        f1 = open('register',encoding='utf-8')
        for i in f1:
            if username in i:
                print('用户名重复,请重新输入')
                f1.close()
                break
        else:
            f1.close()
            password = input('请输入要注册的密码:').strip()
            f2 = open('register', encoding='utf-8', mode='a')
            f2.write('\n{}\t{}'.format(username, password))
            f2.close()
            print('恭喜你,注册成功,已经自动为您登录，现在跳转到首页...')
            return login(username,password)


def wrapper(func):
    def inner(*args,**kwargs):
        if status_dic['status']:
            ret = func(*args,**kwargs)
            return ret
        else:
            print('请先进行登录')
            if login():
                ret = func(*args, **kwargs)
                return ret
    return inner

def log_record(func):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
        with open('log_func','a',encoding='utf-8') as f1:
            f1.write('用户:%s 在%s 执行了 %s函数\n'%(status_dic['username'],time_now,func.__name__))
        ret = func(*args,**kwargs)
        return ret
    return inner

@wrapper
@log_record
def article():
    print('欢迎%s访问文章页面' % status_dic['username'])

@wrapper
@log_record
def diary():
    print('欢迎%s访问日记页面' % status_dic['username'])

@wrapper
@log_record
def comment():
    print('欢迎%s访问评论页面' % status_dic['username'])

@wrapper
@log_record
def enshrine():
    print('欢迎%s访问收藏页面' % status_dic['username'])


def login_out():
    status_dic['username'] = None
    status_dic['status'] = False
    print('注销成功')

def Quit():
    global flag1
    flag1 = False
    return flag1

choice_dict = {
    1: login,
    2: register,
    3: article,
    4: diary,
    5: comment,
    6: enshrine,
    7: login_out,
    8: Quit,
}



while flag1:
    print('欢迎来到博客园首页\n1:请登录\n2:请注册\n3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面\n7:注销\n8:退出程序')
    choice = input('请输入您选择的序号:').strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(choice_dict):
                choice_dict[choice]()
        else:
            print('您输入的超出范围，请重新输入')

    else:
        print('您输入的选项有非法字符，请重新输入。')