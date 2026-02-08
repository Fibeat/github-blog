
# 函数介绍
# 1.为完成某一功能的程序指令集合，称为函数。
# 2.在python中，函数分为系统函数和自定义函数。
# 系统函数：
# 1.内置函数
# 2.模块函数
# 自定义函数:
# 1.函数的定义：使用def关键字来定义一个函数
# 2.函数的调用：通过函数名（）来调用一个函数

# 求和函数get_sum()
def get_sum():
    n1 = int(input("请输入一个数字："))
    n2 = int(input("请输入一个数字："))
    operator = input("请输入一个字符(+, -, *, /):")
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2
    else:
        print("输入错误")
    print(n1, operator, n2, "=", result)

# 调用函数
get_sum()


