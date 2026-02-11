class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
    def growth(self) -> None:
            self.height += 1
            self.age += 1

def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    garden = [rose, sunflower, cactus]
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        for plant in garden:
            print(plant)
            plant.growth()
    print(f"Growth this week: +{i - 1}cm")


if __name__ == "__main__":
    main()