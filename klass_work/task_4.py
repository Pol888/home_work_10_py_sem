from task_3 import PersonCard


class Employee(PersonCard):
    id_cr = 1

    def __init__(self, surname: str, name: str, patronymic: str, age: int):
        self.id_employee: str = self.create_id()
        self.access_level: int = sum(list(map(int, list(self.id_employee)))) % 7
        super().__init__(surname, name, patronymic, age)

    def create_id(self):
        id_id = '0' * (6 - len(str(self.id_cr))) + str(self.id_cr)
        Employee.id_cr += 1
        return id_id


if __name__ == '__main__':
    e_1 = Employee('Воронкин', 'Иртыш', "Закружиевич", 22)
    print(e_1.id_employee, e_1.access_level)
    print(e_1.full_name())

    e_2 = Employee('Курних', "Перц", "агаракисьевич", 83)
    print(e_2.id_employee, e_2.access_level)
    print(e_2.full_name())
