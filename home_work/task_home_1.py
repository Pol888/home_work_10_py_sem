import datetime  # банкомат


class AutomatedTellerMachine:

    def __init__(self, initial_amount: int):
        self.initial_amount = initial_amount
        self.count_operations_replenishment = 0

    def main(self):  # счетчик операций
        AutomatedTellerMachine._menu(self)

    def _print_account_amount(self):  # печать суммы на счете
        print(f'Сумма на счете = {self.initial_amount}')

    def _wealth_order(self, list_o: list):
        if self.initial_amount > 5000000:  # налог на богатство перед операцией
            self.initial_amount -= self.initial_amount / 100 * 10
            print('Сработал налог на богатство')
            list_o.append(f'налог на богатство 10%, сумма на счете {self.initial_amount}, {datetime.datetime.now()}')
            return list_o
        return list_o

    def _withdrawal(self, withdrawal_amount, list_o):
        if withdrawal_amount < 30 or withdrawal_amount > 600:  # снятие без процентов
            if self.initial_amount - withdrawal_amount < 0:
                print('Снятие невозможно, сумма снятия превышает сумму на счете')
            else:
                self.initial_amount -= withdrawal_amount
                list_o.append(f'Снятие без процентов {withdrawal_amount}$, сумма на счете{self.initial_amount}, '
                              f'{datetime.datetime.now()}')
                AutomatedTellerMachine._print_account_amount(self)
                self.count_operations_replenishment += 1
                if self.count_operations_replenishment % 3 == 0:
                    self.initial_amount -= self.initial_amount / 100 * 5
                    AutomatedTellerMachine._print_account_amount(self)
                    list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{self.initial_amount}, '
                                  f'{datetime.datetime.now()}')
                    return list_o
            return list_o

        else:  # снятие с процентами
            if self.initial_amount - withdrawal_amount + (withdrawal_amount / 100 * 1.5) < 0:
                print('Снятие невозможно, сумма снятия превышает сумму на счете')

            else:
                self.initial_amount -= withdrawal_amount + (withdrawal_amount / 100 * 1.5)
                list_o.append(f'Снятие с процентами {withdrawal_amount + (withdrawal_amount / 100 * 1.5)}$, '
                              f'сумма на счете{self.initial_amount}, '
                              f'{datetime.datetime.now()}')

                self.count_operations_replenishment += 1

                if self.count_operations_replenishment % 3 == 0:
                    self.initial_amount -= self.initial_amount / 100 * 5
                    list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{self.initial_amount}, '
                                  f'{datetime.datetime.now()}')
                    return list_o
            return list_o

    def _replenishment(self, withdrawal_amount, list_o):

        self.initial_amount += withdrawal_amount
        self.count_operations_replenishment += 1
        list_o.append(f'Пополнение на сумму {withdrawal_amount}$, '
                      f'сумма на счете{self.initial_amount}, '
                      f'{datetime.datetime.now()}')

        if self.count_operations_replenishment % 3 == 0:
            self.initial_amount -= self.initial_amount / 100 * 5

            list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{self.initial_amount}, '
                          f'{datetime.datetime.now()}')
            return list_o
        return list_o

    def _menu(self):
        list_o = []
        flag = True
        AutomatedTellerMachine._print_account_amount(self)
        while flag:
              # печать суммы
            action = input('1 - пополнить\n2 - снять\n3 - лист операций\n(любой знак) - выйти\n')
            if action == '1':
                flag_2 = True
                while flag_2:

                    list_o = AutomatedTellerMachine._wealth_order(self, list_o)  # налог
                    # на богатство перед операцией
                    AutomatedTellerMachine._print_account_amount(self)
                    replenishment_amount = int(input('Введите сумму пополнения кратную 50\n'))  # ввод суммы
                    if not (replenishment_amount % 50 == 0):  # проверка кратности
                        print('Сумма не кратная 50')

                    else:
                        list_o = AutomatedTellerMachine._replenishment(
                            self,
                            replenishment_amount,
                            list_o)
                    AutomatedTellerMachine._print_account_amount(self)
                    flag_2 = False

            elif action == '2':
                flag_2 = True
                while flag_2:
                    list_o = AutomatedTellerMachine._wealth_order(self, list_o)  # налог на богатство
                    # перед операцией
                    withdrawal_amount = int(input('Введите сумму снятия кратную 50\n'))
                    if not (withdrawal_amount % 50 == 0):  # проверка кратности
                        print('Сумма не кратная 50')
                        AutomatedTellerMachine._print_account_amount(self)
                    else:
                        list_o = AutomatedTellerMachine._withdrawal(
                            self,
                            withdrawal_amount,
                            list_o)
                    flag_2 = False

            elif action == '3':
                print(list_o)

            else:
                flag = False


if __name__ == '__main__':
    a = AutomatedTellerMachine(12000000)
    a.main()
