# for 变量名 in 可迭代对象: # 此时只需知道可迭代对象可以是字符串\列表\字典，其实也可以是tuple(),set()
# list_a = list(range(10))
# list_a = ['hahah','1','3','wwww']
# print(list_a)
# for i in list_a:
#     print(i,end=' ')
# 简单版：for循环的实现方式，遍历字典
dic = {'name': 'lsj', 'age': 18, 'gender': 'male'}
for k in dic:  # for 循环默认取的是字典的key赋值给变量名k
    print(k, dic[k])
