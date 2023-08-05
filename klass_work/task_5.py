from klass_work.task_6 import Animals


class Fish(Animals):

    def __init__(self, name: str, limb_type: str, color: list[str, str], body_covering_type: str,
                 average_life_expectancy: int,
                 immersion_depth: tuple[int, int], type_of_reservoir: list[str, str]):
        self.immersion_depth = immersion_depth  # глубина обитания(от, до)
        self.type_of_reservoir = type_of_reservoir  # тип водоема
        super().__init__(name, limb_type, color, body_covering_type, average_life_expectancy)

    def information(self):
        super().information()
        print(f'{self.immersion_depth = }')
        print(f'{self.type_of_reservoir = }')


class Birds(Animals):

    def __init__(self, name: str, limb_type: str, color: list[str, str], body_covering_type: str,
                 average_life_expectancy: int,
                 flight_altitude: tuple[int, int], habitat: list[str, str]):
        self.flight_altitude = flight_altitude  # высота полета(от, до)
        self.habitat = habitat  # тип местности
        super().__init__(name, limb_type, color, body_covering_type, average_life_expectancy)

    def information(self):
        super().information()
        print(f'{self.flight_altitude = }')
        print(f'{self.habitat = }')


class Insects(Animals):

    def __init__(self, name: str, limb_type: str, color: list[str, str], body_covering_type: str,
                 average_life_expectancy: int,
                 number_of_legs: int, presence_of_wings: bool):
        self.number_of_legs = number_of_legs  # количество ног(от, до)
        self.presence_of_wings = presence_of_wings  # наличие крыльев
        super().__init__(name, limb_type, color, body_covering_type, average_life_expectancy)

    def information(self):
        super().information()
        print(f'{self.number_of_legs = }')
        print(f'{self.presence_of_wings = }')


if __name__ == '__main__':
    f = Fish('Карась', 'Плавник', ['золотой', 'серовато-желтый'], 'чашуя', 10, (0, 50), ['Река', 'Озеро'])
    f.information()
