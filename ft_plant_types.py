# Parent Class: Plant
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


# Child classes :
class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_class(self) -> str:
        return "Flower"

    def __str__(self) -> str:
        return (f"{self.name} ({self.get_class()}): {self.height}cm,"
                f" {self.age} days, {self.color} color\n"
                f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_class(self) -> str:
        return "Tree"

    def produce_shade(self) -> int:
        return 78

    def __str__(self) -> str:
        return (f"{self.name} ({self.get_class()}): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter\n"
                f"{self.name} provides {self.produce_shade()}"
                " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def get_class(self) -> str:
        return "Vegetable"

    def nutritional_value(self) -> str:
        return "vitamin C"

    def __str__(self) -> str:
        return (f"{self.name} ({self.get_class()}): {self.height}cm,"
                f" {self.age} days, {self.harvest_season} harvest\n"
                f"{self.name} is rich in {self.nutritional_value()}")


def main():
    flowers = [
        ["Rose", 25, 30, "red"],
        ["Tulip", 15, 60, "orange"]
    ]
    trees = [
        ["Oak", 500, 1825, 50],
        ["Birch", 800, 920, 15]
    ]
    vegetables = [
        ["Tomato", 80, 90, "summer"],
        ["Pumpkin", 45, 60, "Fall"]
    ]
    print("=== Garden Plant Types ===\n")
    for plant in flowers:
        new_flower = Flower(plant[0], plant[1], plant[2], plant[3])
        print(new_flower, "\n")
    for plant in trees:
        new_tree = Tree(plant[0], plant[1], plant[2], plant[3])
        print(new_tree, "\n")
    for plant in vegetables:
        new_vegetable = Vegetable(*plant)
        print(new_vegetable, "\n")


if __name__ == "__main__":
    main()
