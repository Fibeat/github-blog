
# 数据容器

# 01_hens_question.py
# 参考连接：https://docs.python.org/zh-cn/3.14/library/functions.html#round
# 使用的重点是内置函数round()
# print(round(3.567, 2))

# 02数据容器
# 定义：存放数据的容器，可以存放多个数据，增加或者减少
# 分类：1.列表list 2.元组tuple 3.集合set 4.字典dict 5.字符串str

    # 1.列表
    # 参考：https://docs.python.org/zh-cn/3.14/library/stdtypes.html#lists
    # ● 列表的定义
    # 创建一个列表,只要用逗号分隔的不同的数据项使用方括号括起来即可,示例如下:
    # ● 举例说明
    # list2 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

    # 列表的使用
    # ● 列表的使用语法
    # 列表名[索引]
        # print list2[2]
    # 列表的遍历
    # ●什么是列表的遍历
    # 简单的说,就是将列表的每个元素依次取出,进行处理的操作,就是遍历/迭代
    # list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']

        # 1.使用while实现遍历

        # 思路分析
        # 1. 先定义变量index=0 表示从第一个元素开始取出
        # 2. 列表list_color的个数 6,这里其实有一个内置函数 Len(列表),可以返回个数
        # 3. 每取出一个就输出/或者根据自己的业务处理

        # list_color = ['red', 'green', 'blue', 'yellow', 'red']
        # print(len(list_color))
        # index = 0

        # while index < len(list_color):
        #     print(f"第{index + 1}个元素是：{list_color[index]}")
        #     index += 1
        #     if list_color[index-1] == "yellow":
        #         print("找到green,yes")
        #         break
        #         # print("虚幻")

        # 2.使用for循环实现遍历
        # list_color = ['red', 'green', 'blue', 'yellow', 'red
        # for color in list_color:  
        #     print(f"元素是：{color}")
    # 列表的注意细节
    # 1、如何表示一个空列表，list[],注意缩进
    # list_empty = []
    # print(list_empty)
    # 2、列表的元素可以有多个,而且数据类型没有限制,允许有重复元素,并且是有序的
    # list_mix = [1, 2.5, 'hello', True, 2, 'hello']
    # 3、列表的索引/下标是从0开始的，而不是从1开始
    # list_index = ['a', 'b', 'c', 'd']
    # 4、列表索引必须在指定范围内使用,否则报:IndexError:list index out of range,比如 list1=[1,2.3],list1[3]就会报错
    # 5、索引也可以从尾部开始,最后一个元素的索引为-1,往前一位为-2,以此类推 values
    # 6、通过 列表[索引]=新值 对数据进行更新,使用 列表.append(值)方法来添加元素,使用del语句来删除列表的元
    # 素,注意不能超出有效索引范围


# 2.循环输出分数
# scores = []

# for i in range(5):
#     score = float(input("请输入分数："))
#     scores.append(score)
# #输出分数列表E
# print("分数列表为：", scores)