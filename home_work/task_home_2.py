class DateCheckForConsistency:  # проверка даты

    def __init__(self, date):
        self.date = date


    def date_check(self):
        dd, mm, yyyy = self.date.split('.')
        days = [31, DateCheckForConsistency.__definition_of_leap_year(self, yyyy), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 9999 >= int(yyyy) >= 1 and 12 >= int(mm) >= 1:
            if 1 <= int(dd) <= days[int(mm) - 1]:
                return True
        return False


    def __definition_of_leap_year(self, yyyy):
        yyyy = int(yyyy)
        if yyyy % 4 == 0:
            if yyyy % 100 != 0:
                return 29
            else:
                if yyyy % 400 == 0:
                    return 29
                else:
                    return 28
        else:
            return 28


if __name__ == '__main__':
    print(DateCheckForConsistency('10.13.9999').date_check())


