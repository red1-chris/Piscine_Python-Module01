#Parent Class: Plant
class Plant:
    def __init__(self) -> None:
        self.name
        self.height
        self.age

#Child classes :
class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        print(f"{self.name} ({self.class}): {self.height}cm, {self.age} days, {self.color} color")