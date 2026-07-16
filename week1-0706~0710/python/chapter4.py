# n = 10
# def f(x: int):
#     x = x + 1
#     print("x:", x)

# f(n)
# print("n:", n)

''''''
# swap

# a = 10
# b = 20
# a, b = b, a
# print(a, b)


''''''
# unpacking

# def printPerson(name, age, address):
#     print("이름은", name)
#     print("나이은", age)
#     print("주소은", address)

# printPerson(*["이태경", 22, "서울"])
# # dict의 경우는 **을 붙여서 key와 매핑되는 매개변수에 값을 대입한다.
# printPerson(**{"age": 22, "address": "seoul", "name": "leetk"})


# def fc(w, h, **other):
#     print("몸무게 {}, 키 {}".format(w, h))
#     print(other)


''''''

# def add(data1, data2):
#     return data1 + data2

# def sub(data1, data2):
#     return data1 - data2

# def calculator(fc, data1, data2):
#     return fc(data1, data2)

# print(calculator(add, 10, 20))
# print(calculator(sub, 10, 20))

''''''

# 클로저

# def outer():
#     n = 0
#     def inner():
#         nonlocal n
#         n += 1
#         return n
#     return inner

# var1 = outer()
# print(var1())
# print(var1())

# var2 = outer()
# print(var2())


''''''
# 함수를 매개변수로 받아서 1부터 10까지 함수에 대입해서 그 결과를 list로 만들어서 리턴해주는 함수

# def g(fc):
#     return [fc(x) for x in range(1, 11)]

# def f(x):
#     return x * x

# # print(g(f))
# print(g(lambda x : x * x))


''''''
# map, filter 사용

# ages = [23, 34, 41, 22, 33, 31, 27]
# #나이에 해당하는 데이터를 1씩 증가시켜서 새로운 데이터 목록을 만들기

# result = list(map(lambda x : x + 1, ages))
# print(result)
# print(ages)

# # 30이 넘는 데이터만 추출
# result = list(filter(lambda x : x > 30, ages))
# print(result)


# # ages의 합계
# from functools import reduce

# result = reduce(lambda x, y: x + y, ages)
# print(result)

''''''
# decorator

# import time 
# #decorator로 사용되면 func가 호출하는 함수가 된다.
# def deco(func):
#     n = 0
#     def inner():
#         nonlocal n
#         n = n + 1
#         print(time.time())
#         print(n)
#         func()
#     return inner

# # target을 호출 할 때 deco라는 함수가 리턴하는 함수를 호출
# @deco
# def target():
#     print("running target")

# target()
# target()

''''''
# 팩토리얼 구하는 함수 재귀

# def fc(n):
#     if (n == 1 or n == 0):
#         return 1
    
#     return fc(n - 1) * n

# def main():
#     print(fc(5))

# main()

''''''
# 팩토리얼 구하는 함수의 작업시간 구하기 with decorator

# import time
# # decorator를 위한 함수
# def logging(func):
#     def logged(*args):
#         start = time.time()

#         # 실제 함수를 호출
#         result = func(*args)
#         print("함수 호출 결과", result)

#         end = time.time()
#         elapsed = end - start
#         print("함수가 작업에 걸린 시간:", elapsed)
#         return result

#     return logged

# @logging
# def fc(n):
#     if (n == 1 or n == 0):
#         return 1
    
#     return fc(n - 1) * n

# def main():
#     print(fc(5))

# main()

''''''
# 메모이제이션을 활용한 재귀 피보나치

import time
from functools import lru_cache
# decorator를 위한 함수
def logging(func):
    totalTime = 0
    def logged(*args):
        nonlocal totalTime
        start = time.time()

        # 실제 함수를 호출
        result = func(*args)
        print("함수 호출 결과", result)

        end = time.time()
        elapsed = (end - start) * 1000
        totalTime += elapsed
        print("함수가 작업에 걸린 시간:", elapsed)
        print("누적 시간:", totalTime)
        return result

    return logged

@lru_cache
@logging
def fibo(n):
    if (n == 1 or n == 2):
        return 1
    return fibo(n - 1) + fibo(n - 2)

def main():
    print(fibo(10))

main()
# 5.3272247314453125 - 메모이제이션 없이 걸린 시간
# 0.5271434783935547 - 메모이제이션 활용
    