# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     @classmethod
#     def from_square(cls, side_length: float) -> 'Rectangle':
#         return cls(side_length, side_length)

# rectangle1: Rectangle = Rectangle(3.0, 4.0)
# rectangle2: Rectangle = Rectangle.from_square(2.0)

# print(rectangle1.area())  # 12.0
# print(rectangle2.area())  # 4.0


# import datetime

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
#         age = cls.get_age(birth_year)
#         return cls(name, age)

#     @staticmethod
#     def get_age(birth_year: int) -> int:
#         return datetime.date.today().year - birth_year

# person: Person = Person.from_birth_year('John', 1990)
# print(person.name)  # John
# print(person.age)  # 33


# class Car:
#     total_cars_sold: int = 0

#     def __init__(self, make: str, model: str):
#         self.make = make
#         self.model = model
#         Car.total_cars_sold += 1

#     @classmethod
#     def get_total_cars_sold(cls) -> int:
#         return cls.total_cars_sold

# car1: Car = Car('Toyota', 'Camry')
# car2: Car = Car('Honda', 'Civic')

# print(Car.get_total_cars_sold())  # 2


# class Point:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls, point_tuple: tuple[float, float]) -> 'Point':
#         x, y = point_tuple
#         return cls(x, y)

# point: Point = Point.from_tuple((3, 4))
# print(point.x)  # 3
# print(point.y)  # 4


# class Student:
#     all_students: list['Student'] = []

#     def __init__(self, name: str, grade: float):
#         self.name = name
#         self.grade = grade
#         Student.all_students.append(self)

#     @classmethod
#     def get_highest_grade(cls) -> 'Student':
#         return max(cls.all_students, key=lambda student: student.grade)

#     @classmethod
#     def get_lowest_grade(cls) -> 'Student':
#         return min(cls.all_students, key=lambda student: student.grade)

# student1: Student = Student('John', 90)
# student2: Student = Student('Jane', 95)
# student3: Student = Student('Alice', 80)

# print(Student.get_highest_grade().name)  # Jane
# print(Student.get_lowest_grade().name)  # Alice


# Task Nr.1:

# Create a class method to return the factorial of a given number.


# class MathOperations:
#     @classmethod
#     def factorial(cls, number: int) -> int:
#         if number == 0:
#             return 1
#         else:
#             return number * cls.factorial(number - 1)


# print(MathOperations.factorial(5))


# Mindaugo pvz


# class Factorial:
#     @classmethod
#     def factorial(cls, number: int) -> int:
#         fact = 1
#         for num in range(2, number + 1):
#             fact *= num
#         return fact


# some_thing: Factorial = Factorial.factorial(5)
# print(some_thing)


# Task Nr.2:

# Create a class method to return the reversed string of a given string.


# class StringRevers:
#     @classmethod
#     def reversed_string(cls, n: str) -> str:
#         return n[::-1]


# print(StringRevers.reversed_string("Hello World"))


# Task Nr.3:

# Create a class method to return the list of prime numbers up to a given number.


# from typing import List


# class MathOperations:
#     prime_numbers = [1, 2, 15, 6]

#     @classmethod
#     def numbers_up(cls) -> List[int]:
#         cls.prime_numbers_numbers = [num + given_number for num in cls.prime_numbers]
#         return cls.prime_numbers


# given_number = 2
# print(MathOperations.numbers_up())


# from typing import List


# class Prime:
#     @classmethod
#     def get_primes(cls, number: int) -> List[int]:
#         prime_no_list = []
#         for number in range(0, number + 1):
#             if number > 1:
#                 for i in range(2, number):
#                     if (number % i) == 0:
#                         break
#                 else:
#                     prime_no_list.append(number)
#         return prime_no_list


# print(Prime.get_primes(20))




