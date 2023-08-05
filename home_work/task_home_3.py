class TheExistenceOfATriangle:    # треугольник
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def existence_check(self):
        combinations = [self.a + self.b > self.c, self.b + self.c > self.a, self.c + self.a > self.b]

        if False in combinations:
            print("Треугольник не существует")
        else:
            print("Треугольник существует")
            if self.a == self.b == self.c:
                print("Он равносторонний")
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                print("Он равнобедренный")
            else:
                print("Он разносторонний")


if __name__ == '__main__':
    TheExistenceOfATriangle(3, 6, 8).existence_check()