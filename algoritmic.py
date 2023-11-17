#1
# class Student:
#     def __init__(self, number, name, age, ball, course):
#         self.name = name
#         self.age = age
#         self.ball = ball
#         self.course = course
#         self.number = number
#
#     def average_ball(self):
#         return sum(self.ball) / len(self.ball)
#
#
# Mihail = Student('/// С Т У Д Е Н Т  Н О М Е Р 1 ///','Михаил', "16", [4, 2, 3, 4, 2, 5 ,5 , 5 ,5 , 5, 5, 3 , 3, 5, 3 ,4 ,2 ,4 ,3], 1)
# print(Mihail.number)
# print('Имя:', Mihail.name)
# print('Возраст:', Mihail.age)
# print('Средний балл:', Mihail.average_ball())
# print('Курс:', Mihail.course)
#
# Alena = Student('/// С Т У Д Е Н Т  Н О М Е Р 2 ///','Алёна', "18", [3, 5, 2, 4, 2, 3 , 3 ,2 , 2, 5, 4 , 5, 4, 3 ,5 ,2 ,4 ,3], 2)
# print(Alena.number)
# print('Имя:', Alena.name)
# print('Возраст:', Alena.age)
# print('Средний балл:', Alena.average_ball())
# print('Курс:', Alena.course)

#2

# class Square:
#     def __init__(self, dlina, shirina):
#         self.dlina = dlina
#         self.shirina = shirina
#
#
#     def perimetr(self):
#         return self.dlina + self.dlina + self.shirina + self.shirina
#
#     def ploshad(self):
#         return self.dlina * self.shirina
#
# sq1 = Square(14, 28)
# print('Длина:', sq1.dlina)
# print('Ширина:', sq1.shirina)
# print('Периметр', sq1.perimetr())
# print('Площадь:', sq1.ploshad())
#
# sq2 = Square(342522343, 234668483578)
# print('Длина:', sq2.dlina)
# print('Ширина:', sq2.shirina)
# print('Периметр', sq2.perimetr())
# print('Площадь:', sq2.ploshad())


#3

# class car:
#     def __init__(self, marka, year, probeg):
#         self.marka = marka
#         self.year = year
#         self.probeg = probeg
#
# print('Введите марку, год выпуска, и пробег в отдельных строчках:')
# car1 = car(str(input()), int(input()), int(input()))
# print('Марка машины:', car1.marka)
# print('Год выпуска:', car1.year)
# print('Пробег:', car1.probeg, 'км')
#
# print('Введите марку, год выпуска, и пробег (в км) в отдельных строчках:')
# car2 = car(str(input()), int(input()), int(input()))
# print('Марка машины:', car2.marka)
# print('Год выпуска:', car2.year)
# print('Пробег:', car2.probeg, 'км')

#4

# class bank_account():
#     def __init__(self, username, balance):
#         self.username = username
#         self.balance = balance
#
#
#     # def operations_add_money(self, add_money, balance):
#     #     print('Введите сумму пополнения в рублях:')
#     #     add_money = int(input())
#     #     return f'Ваш счет успешно пополнен на {add_money} ₽! Ваш текущий баланс - {self.balance} руб.'
#     #
#     #
#     # def operations_snyat_money(self, snyat_money):
#     #     print('Введите сумму снятия в рублях:')
#     #     snyat_money = int(input())
#     #     return f'Вы успешно сняли со счета {snyat_money} ₽!'
#
# user1 = bank_account('Роман', 1386)
# user2 = bank_account('Алиса', 238700)
#
#
# print('Выберите пользователя, 1 =', user1.username, '2 = ', user2.username)
# election = int(input())
# if election == 1:
#     print('Имя:', user1.username)
#     print('Баланс:', user1.balance)
#
#
#
#     print('Введите номер операции. 1 - пополнить счет, 2 - снять деньги со счета')
#     operation = int(input())
#     if operation == 1:
#         print('Введите сумму пополнения в рублях:')
#         add_money = int(input())
#         print(f'Ваш счет успешно пополнен на {add_money} ₽!')
#         print('Ваш текущий баланс - ',user1.balance + add_money,'  руб.')
#     if operation == 2:
#         print('Введите сумму снятияв рублях:')
#         snyat_money = int(input())
#         if snyat_money <= user2.balance:
#             print('С вашего счета успешно сняты', snyat_money, '. Ваш текущий баланс:', user1.balance - snyat_money)
#
# if election == 2:
#     print('Имя:', user2.username)
#     print('Баланс:', user2.balance)
#
#     print('Введите номер операции. 1 - пополнить счет, 2 - снять деньги со счета')
#     operation = int(input())
#     if operation == 1:
#         print('Введите сумму пополнения в рублях:')
#         add_money = int(input())
#         print(f'Ваш счет успешно пополнен на {add_money} ₽!')
#         print('Ваш текущий баланс - ', user2.balance + add_money, '  руб.')
#     if operation == 2:
#         print('Введите сумму снятияв рублях:')
#         snyat_money = int(input())
#         if snyat_money <= user2.balance:
#             print('С вашего счета успешно сняты', snyat_money,'. Ваш текущий баланс:', user2.balance - snyat_money)


#5

# import math
#
#
# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def get_triangle_type(self):
#         if self.side1 == self.side2 == self.side3:
#             return "Равносторонний треугольник"
#         elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
#             return "Равнобедренный треугольник"
#         else:
#             return "Разносторонний треугольник"
#
#     def calculate_area(self):
#         s = (self.side1 + self.side2 + self.side3) / 2
#         area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
#         return area
#
#
# triangle1 = Triangle(int(input()), int(input()), int(input()))
# print(triangle1.get_triangle_type())
# print('Площадь треугольника равна:', triangle1.calculate_area())

