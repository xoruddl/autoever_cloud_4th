''''''
# list 정렬

# class Person:
#     def __init__(self, num = 0, name = ""):
#         self.num = num
#         self.name = name
    
#     def getNum(self):
#         return self.num
    
#     def getName(self):
#         return self.name
    
#     # < 연산자를 오버로딩, 크기 비교가 가능하게 해서 정렬이 되도록 함
#     def __lt__(self, other):
#         return self.num < other.num
    
#     def __str__(self):
#         return self.num + ": " + self.name
    
# person1 = Person(1, "park")
# person2 = Person(2, "jesicca")
# li = [person1, person2]

# names = ["Park", "adam", "rusia", "RYU"]

# # 대소문자 구분없이 비교
# names.sort(key = str.upper)
# print(names)

# # 인스턴스들의 list 정렬은 특정한 값 하나를 리턴하는 함수를 이용
# li.sort(key = Person.getNum)
# print(li)

# li.sort()

''''''
# list comprehension

# l = list(range(1, 11))
# result = []
# for i in l:
#     result.append(i * i)

# print(result)

# # Comprehension 이용
# reuslt = [i * i for i in l]
# print(result)

# result = [i * i for i in range(1, 11) if i % 2 == 0]
# print(result)

# # 2개의 시퀀스를 사용하는 것도 가능
# result = [i + j for i in range(1, 11) for j in range(101, 111)]
# print(result)

# # 2차원 배열 활용
# l = [[1, 2, 3], [4, 5, 6]]
# result = [j for i in l for j in i]
# print(result)

''''''
# 조건에 따라 다른 작업

# # 1부터 10까지의 숫자에서 짝수이면 제곱을 하고 홀수이면 그대로
# result = [i * i if i % 2 == 0 else i for i in range(1, 11)]
# print(result)

''''''
# Counter 클래스

from collections import Counter

data = ["Python", "Go", "Python", "Python", "Go", "Java", "C"]
counter = Counter(data)

# Go의 개수
print(counter["Go"])

# 모든 데이터의 개수를 dict로 생성
print(dict(counter))

''''''
# 집계

# data = [
#     ("사과", 3, 2000),
#     ("수박", 2, 20000),
#     ("사과", 5, 2000),
#     ("수박", 1, 25000),
# ]

# from collections import Counter

# # 각 데이터가 몇개 나왔는지
# counter = Counter()
# for name, cnt, price in data:
#     counter[name] = counter[name] + 1
# print(counter)

# # 각 데이터에 수량 * 가격을 더한 값을 누적
# counter = Counter()
# for name, cnt, price in data:
#     counter[name] = counter[name] + cnt * price
# print(counter)

''''''
# itertools 모듈

# from itertools import product
# l1 = ['A', 'B']
# l2 = [12, 34, 56]

# for i in product(l1, l2, repeat = 1):
#     print(i)

''''''




