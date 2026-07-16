''''''
# class

# class Student:
#     # 인스턴스가 호출할 수 있는 메서드
#     def display(self):
#         print("OOP")

# # 인스턴스 생성 - 인스턴스의 참조를 다른 곳에 저장하지 않았으므로 여기서 만들어진 인스턴스는 바로 소멸
# Student().display()

# # 인스턴스의 참조를 s에 저장하고 호출: 인스턴스는 s가 소멸될 때까지 메모리에 남아있음
# s = Student()
# s.display()

# # 파이선은 인스턴스가 호출할 수 있는 메서드를 클래스가 호출 가능: 언바운드 호출
# # 첫 번째 매개변수로 인스턴스를 대입해서 호출이 가능
# Student.display(s)

''''''
# class

# class Student:
#     schoolName = "RAPA"

# # 클래스가 클래스 속성을 호출
# print(Student.schoolName)

# # 인스턴스가 클래스 속성을 호출
# s = Student()
# print(s.schoolName)
# print()

# # 클래스를 이용해서 클래스 속성을 수정
# print("클래스 속성을 수정")
# Student.schoolName = "AutoEver"
# print(Student.schoolName)
# print(s.schoolName + "\n")

# # 인스턴스를 이용해서 클래스 속성을 수정: 인스턴스는 클래스 속성을 수정할 수 없음
# # 인스턴스는 자신의 것만 수정
# print("인스턴스는 속성을 수정할 때 자신에게 없으면 생성")
# print("클래스 속성을 수정")
# s.schoolName = "HYUNDAE"
# print(Student.schoolName)
# print(s.schoolName)

''''''
# 인스턴스 별로 번호와 이름을 속성으로 갖는 클래스

# class Student:
#     num = 0
#     name = ""

#     @staticmethod
#     def sMethod():
#         print("static method")

#     def __init__(self, num = 0, name = "noName"):
#         print("인스턴스 생성")
#         self.num = num
#         self.name = name

#     def getNum(self):
#         return self.num
    
#     def setNum(self, num):
#         self.num = num

#     def getName(self):
#         return self.name
    
#     def setName(self, name):
#         self.name = name

#     def __del__(self):
#         print("인스턴스가 소멸되었습니다.")

# def main():

#     Student.sMethod()

# main()

''''''
# 속성을 private으로

# class Student:
#     # __name = ""
#     # __age = 0

#     def __init__(self, name, age):
#         self.__age = age
#         self.__name = name # 앞에 __가 붙으면 속성이 private이 된다. 클래스 외부에서 사용 불가

#     def getName(self):
#         return self.__name
    
#     def setName(self, name):
#         self.__name = name
    
#     def getAge(self):
#         return self.__age
    
#     def setAge(self, age):
#         self.__age = age

#     name = property(fget = getName, fset = setName)
#     age = property(fget = getAge, fset = setAge)

# def main():
#     s = Student("noName", 0)
#     s.name = "adam"
#     print(s.name)

# main()

''''''
# @property 사용

# class Student:
#     # __name = ""
#     # __age = 0

#     def __init__(self, name, age):
#         self.__age = age
#         self.__name = name # 앞에 __가 붙으면 속성이 private이 된다. 클래스 외부에서 사용 불가

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         print("name의 setter 호출")
#         self.__name = name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age


# def main():
#     s = Student("noName", 0)
#     s.name = "adam"
#     print(s.name)

# main()

''''''
# 연산자 오버로딩

# class Student:
#     # __name = ""
#     # __age = 0

#     def __init__(self, name, age):
#         self.__age = age
#         self.__name = name # 앞에 __가 붙으면 속성이 private이 된다. 클래스 외부에서 사용 불가

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         print("name의 setter 호출")
#         self.__name = name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age

#     # 연산자의 기능을 overloading: __name을 결합
#     def __add__(self, other):
#         return self.__name + "," + other.__name
    
#     # == 연산자의 기능을 오버로딩
#     def __eq__(self, other):
#         return self.__name == other.__name
    
#     # print문 오버로딩
#     def __str__(self):
#         return self.__name

# def main():
#     s1 = Student("adam", 30)
#     s2 = Student("rusia", 27)
#     s3 = Student("adam", 40)
#     print(s1 + s2) # 연산자 오버로딩 때문에 name을 결합한 결과
#     print(s1 == s2)
#     print(s1 == s3)
#     print(s1)

# main()

''''''
# 상속

# class Person:
#     def __init__(self, num):
#         self.num = num

#     def superMethod(self):
#         print("상위 클래스의 메서드")

# # Person 클래스가 상위 클래스가 되도록 설정
# class Student(Person):
#     # 상위 클래스에 매개변수가 있는 __init__이 있는 경우는 직접 호출해줘야 함.
#     def __init__(self):
#         super().__init__(3)

#     def subMethod(self):
#         print("하위 클래스의 메서드")

# def main():
#     s = Student()
#     s.subMethod()
#     s.superMethod() # 상위 클래스의 메서드 호출
#     print(s.num) # 상위 클래스의 __init__에 매개변수가 있고 초기값이 없으면 에러
#     # 이런 경우에는 하위 클래스에 __init__을 만들어서 super().__init__()를 호출해줘야 함

# main()

''''''
# 상속2 - 오버라이딩

# class Person:
#     def method(self):
#         print("상위 클래스의 메서드")

# class Student(Person):
#     # 메서드 오버라이딩: 기능 확장이 목적이므로 상위 클래스의 메서드를 호출해야 한다.
#     def method(self):
#         super().method()
#         print("하위 클래스의 메서드")

# def main():
#     s = Student()
#     s.method()

# main()

''''''
# 추상 클래스

# import abc
# class Sample(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def method(self):
#         pass

# # 추상클래스를 상속 받으면 반드시 추상 메서드를 구현해야 함
# class Sub(Sample):
#     def method(self):
#         print("추상 메서드 구현")

# # obj = Sample() # 추상 클래스는 인스턴스를 만들 수 없기 때문에 에러
# obj = Sub()
# obj.method()

''''''
# 다형성 예시

# from abc import *
# class Starcraft(metaclass = ABCMeta):
#     @abstractmethod
#     def attack(self):
#         pass

# class Terran(Starcraft):
#     def attack(self):
#         print("테란의 공격")

# class Zerg(Starcraft):
#     def attack(self):
#         print("저그의 공격")

# class Protoss(Starcraft):
#     def attack(self):
#         print("프로토스의 공격")

# def main():
#     menu = int(input("종족을 선택하세요: (1. 테란 2. 저그 3. 프로토스) "))
#     s = None
#     if (menu == 1):
#         s = Terran()
#     elif (menu == 2):
#         s = Zerg()
#     elif (menu == 3):
#         s = Protoss()

#     s.attack()

# main()

''''''
# coroutine

# def tot_coroutine():
#     tot = 0
#     while True:
#         # next를 호출하면 이 자리에서 대기하고 있다가 send를 호출하면 데이터를 받아서 수행하고
#         # 다시 이 자리에서 대기
#         data = (yield tot)
#         tot = tot + data
#         print("현재까지의 합계:", tot)

# # coroutine을 변수에 담기
# co = tot_coroutine()

# # 맨 처음에 한 번 호출
# result = next(co)
# print(result)

# # 코루틴 수행
# result = co.send(2)
# print(result)
# result = co.send(1)
# print(result)


