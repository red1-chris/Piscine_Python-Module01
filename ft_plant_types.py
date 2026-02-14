#Parent Class: Plant
class Plant:
    def __init__(self) -> None:
        self.name
        self.height
        self.age

#Child classes :
class Flower(Plant):
    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.color = color

    def get_class(self) -> str:
        self.get_class = "Flower"

    def __str__(self) -> str:
        print(f"{self.name} ({self.get_class}): {self.height}cm,"
              f" {self.age} days, {self.color} color")
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, trunk_diameter) -> None:
        super().__init__(name)
        self.trunk_diameter = trunk_diameter

    def get_class(self) -> None:
        self.get_class = "Tree"

    def produce_shade(self) -> int:
        self.produce_shade = 78

    def __str__(self) -> str:
        print(f"{self.name} ({self.get_class}): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade} square meters of shade")

class Veetable(Plant):
    def __init__(self, name, harvest_season):
        super().__init__()