class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main():
    creations = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    created_plants = []
    print("=== Plant Factory Output ===")
    for plant in creations:
        new_plant = Plant(plant[0], plant[1], plant[2])
        created_plants.append(new_plant)
        print(new_plant)
    print(f"\nTotal plants created: {len(created_plants)}")


if __name__ == "__main__":
    main()
