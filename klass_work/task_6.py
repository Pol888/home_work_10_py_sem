class Animals:

    def __init__(self, name:str, limb_type:str, color:list[str, str], body_covering_type:str, average_life_expectancy:int):
        self.name = name
        self.limb_type = limb_type # тип конечностей
        self.color = color
        self.body_covering_type = body_covering_type # покров
        self.average_life_expectancy = average_life_expectancy # средняя продолжительность жизни

    def information(self):
        print(f'{self.name = }')
        print(f'{self.limb_type = }')
        print(f'{self.color = }')
        print(f'{self.body_covering_type = }')
        print(f'{self.average_life_expectancy = }')