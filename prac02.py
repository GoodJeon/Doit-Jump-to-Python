
# Q1
a = 80
b = 75
c = 55
(a+b+c)/3

# Q2
13 % 2

# Q3
pin = "881120-1068234"
yyyymmdd = "19%s"% (pin[:6])
num = "%s"% (pin[7:])
print(yyyymmdd)
print(num)

# Q4
pin = "881120-1068234"
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 06
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 07
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 08
a = (1, 2, 3)
a = a + (4,)
print(a)

# 09
a = dict()
a
{} #답 : 3번, 이유 : 3번은 리스트(변하는값)기 때문에 딕셔터리의 key값이 될 수가 없다.

# 10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12
a = b = [1, 2, 3]
a[1] = 4
print(b)
#b값은 a값과 동일하게 2가 4로바뀌어서 나타난다. 
# 그 이유는 a와 b에 동시에 같은 변수를 선언하여 같은 메모리(객체)에 저장되어있기 때문이다.