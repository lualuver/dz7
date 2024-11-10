class Person:
    def __init__(self, age=int(input("Введите ваш возраст: "))):
        self.age = 0
        self.set_age(age)

    def set_age(self, age):
        if age > 120 or age < 0:
            raise InvalidAgeError("Возраст который вы ввели недопустим")
        else:
           self.age = age

class InvalidAgeError(Exception):
    def __init__(self, error):
        super().__init__(error)







try:
    p = Person()
    p.set_age(18)
except InvalidAgeError as p:
    print(f"Произошла ошибка: {p}")

