class PersonCard:
    def __init__(self, surname:str, name:str, patronymic:str, age:int):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.surname.capitalize()} {self.name.capitalize()} {self.patronymic.capitalize()}'
    def age(self):
        return self.__age

if __name__ == '__main__':
    p = PersonCard('-я-', "-яя-", "-и_еще_раз_я-", 188)
    print(p.full_name(), p.age())
    p.birthday()
    print(p.age())
