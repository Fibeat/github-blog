
# ● 字典使用示例:dict_define.py
# 代码

#字典的基本使用案例
tel = {'jack': 4098, 'tom': 4139}
print(f"dict_tel:{tel}类型:{type(tel)}")
# 查询jack的tel
print("jack的tel:",tel['jack'])


#1字典的Key(关键字)通:是字符串或数字，Value可以是任意数据类型

dict_a = {
    "jack": [100, 200, 300],
    "mary": (10, 20, "hello"),
    "nono": {"apple", "pear"},
    "smith":"计算机老师",
    "周星驰":{
        "性别":"男",
        "age": 18,
        "地址":"香港"
    }
}

print(f"dict_a: {dict_a} : {type(dict_a)}")



# 3、既然字典不支持索引,所以对字典进行遍历不支持while,只支持for
dict_b = {'one' : 1, 'two': 2, 'three': 3}
# 遍历方式1-依次取出key,再通过dict[key]取出对应的value

print("--遍历方式1")
for key in dict_b:
    print(f"key:{key} value:{dict_b[key]}")

# 遍历方式2-依次取出value
print("--遍历方式2-")
for value in dict_b.values():
    print(f"value:{value}")

#?遍历方式3-依次取出key-value
print("-遍历方式3")
for k,v in dict_b.items():
    print(f"key:{k} value:{v}")

#4、创建空字典可以通过[,或者 dict()
dict_c = {}
dict_d = dict()
print(f"dict_c: {dict_c} %W: {type(dict_c)}") # {} dict
print(f"dict_d:{dict_d}类型:{type(dict_d)}")#{} dict|



#5、字典的key必须是唯一的,如果你指定了多个相同的key,后面的键值对会覆i

dict_e = {'one': 1, 'two': 2, 'three': 3, 'two': 200}
print(f"dict_e: {dict_e}") # {'one': 1, (two': 2, 'three': 3, }


# 演示字典常用操作
'''
    演示字典的常用操作
    {"one": 1, "two": 2, "three": 3}

'''


dict_a = {"one": 1, "two": 2, "three": 3}
# 1 len(d):返回字典 d 中的项数
print(f"dict_a 的元素个数是 :{len(dict_a)} ")

#2 d[key]:返回d 中以 key 为键的项。如果映射中不存在 key 则会引发 KeyError
print("key为three对应的value:",dict_a['three']) #3

#3 d[key]=value:将 d[key]设为 value,如果key已经存在,则是修改value,
# 如果key没有存在,则是增加 key-value,注意会直接修改原来的字典-示意图
# 修改 需求:修改 key='one'对应的value为 第一
dict_a['one']='第一'

print(f"dict_a: {dict_a}") #{"one": 1, "two": 2,"three": 3}

# 增加需求，增加 key='four' , value=4
dict_a['four']=4
print(f"dict_a: {dict_a}")


#4 del d[key]:将 d[key] 从 d 中移除。如果映射中不存在 key 则会引发 KeyError
# 需求 删除key为'four'的元素
del dict_a["four"]
print(f"dict_a: {dict_a}")

# 5

# pop(key[, default]) :
# 如果 key 存在于字典中则将其移除并返回其值,否则返回 default。
# 如果 default 未给出且 key 不存在于字典中,则会引发 KeyError
# 需求:将key为‘one’的值返回,并将该元素从字典移除
# val = dict_a.pop('one1', "False") #注意后面的default参数
val = dict_a.pop('one') #注意后面的default参数
print(f"val: {val}")
print(f"dict_a: {dict_a}")

# 6 keys():返回字典所有的key
dict_a_keys = dict_a.keys()
print(f"dict_a_keys: {dict_a_keys}，类型是{type(dict_a_keys)}")
for k in dict_a_keys:
    print("k_>:", k)

#7 key in d: 如果 d 中存在键 key 则返回 True,否则返回 False
# 需求:判断 字典中是否有 key 'two'
print("two" in dict_a) # True

#8 clear():移除字典中的所有元素
# 需求:将字典清空
dict_a.clear()
print(f"dict_a: {dict_a}") 


# 字典推导式示例

books=["红楼梦","三国演义","西游记","水浒传"]
authors=["曹雪芹","罗贯中","吴承恩","施耐庵"]
dict_book = {book: author for book, author in zip(books, authors)}
print("dict_book:" ,dict_book)
# 结果dict_book: {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}

# 思考题:
str1 = "韩顺平"
dict_str = {ele1: ele2*2 for ele1, ele2 in zip(str1, str1)} #== 得到=>{}
print("dict_str:", dict_str)


# 3、再举一个案例(dict_create.py)

# 给出两个列表:
english_list = ["red", "black", "yellow", "white"]
chinese_list=["红色","黑色","黄色","白色"]
# english_list_upper = english_list.upper(english_list)
# 需求:将两个列表的数据,组成一个字典,要求:
# 生成一个字典:
# {'红色 !: 'RED','黑色:'BLACK','黄色!‘YELLOW",'白色!"WHITE’}

# print("english_list_upper:", english_list_upper)
dict_color = {c:e.upper() for c, e in zip(chinese_list, english_list)}
print("dict_color:", dict_color)

