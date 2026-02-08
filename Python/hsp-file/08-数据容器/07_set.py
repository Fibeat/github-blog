
# 集合的基本使用案例

set_a = {100, 200, 300, 400, 500}
basket = {'apple', 'orange' , 'pear', 'banana'}
print(f"set_a的内容是:{set_a}类型是:{type(set_a)}")#{100,200,300,400,500)
print(f"basket的内容是：{basket},类型是：{type(basket)}")


# 3、既然集合不支持索引,所以对集合进行遍历不支持while,只支持for
# - 老韩解读

# 使用for对集合进行遍历
print("-" * 30)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for ele in basket:
    print(ele)


# 创建空集合只能用 set(),不能用 },{} 创建的是空字典,下一小节介绍:字典
# 上面这样定义空集合不对,他是一个空字典
# 创建空集合

set_b = {}
set_c = set()
#
print(f"set_b:{set_b} 类型:{type(set_b)} set_c: {set_c}类型:{type(set_c)}")



# 演示集合常用操作

#定义集合
basket = {'apple', 'orange' , 'apple', 'pear', 'orange', 'banana'}

#1 Len(集合):集合元素个数
print("basket的元素个数:",len(basket))#?

#2 x in s:检测 X 是否为 S 中的成员
# 需求:判断apple是否在集合中
print("apple" in basket)

# 3 add(elem):向集合添加元素 elem。
# 需求:将grape添加到集合中
basket.add("grape")
print("basket的元素:",basket)

# 4 remove(elem):从集合中移除元素 elem。
# 如果 elem 不存在于集合中则会引发 KeyError
# 需求:将 apple从集合删除
basket.remove("grape")
print("袁术：", basket)

# 5 pop():从集合中移除并返回一个随机元素。
# 如果集合为空则会引发 KeyError
# 需求:从集合中随机删除一个元素
ele = basket.pop()
print("ele:",ele,"类型是:",type(ele))
# 注意pop()操作会影响到原集合
print("basket的元素:",basket)

# 6 union(*others):返回一个新集合,
# 其中包含来自原集合以及 others 指定的所有集合中的元素
# 示意图说明一下
books = {'天龙八部','笑傲江湖'}
books_2={'雪山飞狐','神雕侠侣','天龙八部'}
# 需求:将books 和 books_2 进行合集操作[即:求出在books合或者在books_2集合的元素]
books_3 = books | books_2
# books_3 = books.union(books_2)

# books_3 = ?
print("books_3:", books_3)

# 8 intersection(*others):返回一个新集合,
# 其中包含原集合以及 others 指定的所有集合中共有的元素
# 需求:对 books 和 books_2 求交集[即:求出既在books|又在books_2集合的下素]
# books_4 = books.intersection(books_2)

books_4 = books & books_2
print("books_4->", books_4)


# 8 difference(*others):返回一个新集合,
# 其中包含原集合中在 others 指定的其他集合中不存在的元素
# 也就是:set - other -

books ={'天龙八部','笑傲江湖'}
books_2={'雪山飞狐','神雕侠侣','天龙八部'}

#?需求:求出 只存在books集合的元素
# books_5 = books - books_2
books_5 = books.difference(books_2)
print("books_5:", books_5)


#需求:求出只存在books2集合的元素
books_6 = books_2 - books
# books_6 = ?
print("books_6:", books_6)



# 课后练习：

# 1、用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课),
s_history={'小明','张三','李四','王五','Lily',"Bob"}
s_politic={'小明',"小花",'小红',"二狗"}
s_english={'小明','Lily',"Bob","Davil","李四"}

# -求选课学生总共有多少人
# -求只选了第一个学科的学生数量和学生名字
# -求只选了一门学科的学生数量和学生名字
# -求三门学科都选的学生名字


s_total = s_history.union(s_politic).union(s_english)
print("选课学生总人数：", len(s_total))
s_only_history = s_history.difference(s_politic).difference(s_english)
print("只选历史的学生有：", len(s_only_history), s_only_history)
s_only_politic = s_politic.difference(s_english).difference(s_history)
s_only_english = s_english.difference(s_history).difference(s_politic)
s_only_one = s_only_history.union(s_only_politic).union(s_only_english)
print("只选一门课的学生数量和名字：", len(s_only_one), s_only_one)

print("选三门课程的学生有：", s_history.intersection(s_politic).intersection(s_english))
