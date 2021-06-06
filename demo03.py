#1. 先定一个函数，
def max(a, b):
    print("a== " + str(a), "b== " + str(b))
    if a > b:
        return a
    else:
        return b

#取两个数中的最小值
def min(a, b):
    if a < b:
        return a
    else:
        return b

#找出3个数中的最大值
def max2(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def max3(a, b, c=2, name="志彬1"):
    print(a, b, c,"我的名字 "+name)

#2.使用第1步定义的函数
b = 5
c = 7
#print(max3(2, b, name="志彬"))

# def hs(d,n):
#     return d * n
# print(hs(3,8))
def aa(list):
    sum = 1
    sum1 = 0
    for x in list:
        sum = sum * x
        sum1 = sum1 + x
    return sum,sum1
