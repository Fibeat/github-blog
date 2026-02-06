# ● 举例说明

# 代码

#对字符串进行切片
str = "hello,world"
#需求:截取"hello"
slice_str = str[0:5]
print(f"截取的字符串是:{slice_str}")
# slice_use.py

#对列表进行切片
list_a =["jack", "tom", "yoyo", "nono", "hsp"]
#需求:截取["tom","nono"]
slice_list = list_a[1:4:2]
print(f"截取的列表是:{slice_list}")


# 对元组进行切片
tuple_a = (100, 200, 300, 400, 500, 600)
#需求:截取(200,300,400,500)
slice_tuple = tuple_a[1:5:2]
print(f"截取的元组是:{slice_tuple}")

# 1、切片语法:序列[起始索引:结束索引:步长],起始索引如果不写,默认为,结束索引如果不写,
# 默认为截取到结尾,步长如果不写,默认为1

str ="hello,韩顺平教育"
str_slice01 = str[:5:1]
print("str_slice01->", str_slice01)

str_slice02 = str[1 :: 1]
print("str_slice02->", str_slice02)

str_slice03 = str[ :: 1]
print("str_slice03->", str_slice03)

str_slice04 = str[2:5:]
print("str_slice04->", str_slice04)

# 课堂练习
# 列表定义
list_name=["Jack","Lisa","Hsp","Paul","Smith","Kobe"]

#- 取出前三个名字
# slice_a = list_name[0:3:1]
slice_a = list_name [:3:]

print("取出前三个名字:",slice_a)

#-取出后三个名字,并且保证原来顺序

# 思路分析:
# 1. 使用反向切片
# 2. 步长-1 起始索引-1 结束索引 -4

slice_b = list_name[-1 :- 4 :- 1]
slice_c = list_name[-3::1]
slice_b.reverse() 
# 对元素进行逆序操作
print("取出后三个名字:",slice_b) 
print("取出后三个名字:",slice_c)
##["Paul","Smith","Kobe"]

# 思考：
# 反向操作的顺序是倒着的
# 正向操作的顺序是正着的，方向不一样
