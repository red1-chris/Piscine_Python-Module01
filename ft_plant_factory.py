class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"

    def create_plants(data_list: list) -> list:
        created_plants = []
        for data in data_list:
            new_plant = Plant(data[0], data[1], data[2])
            created_plants.append(new_plant)
        return created_plants


def main():
    creations = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    print("=== Plant Factory Output ===")
    created_plants = Plant.create_plants(creations)
    for plant in created_plants:
        print(plant)
    print(f"\nTotal plants created: {len(created_plants)}")


if __name__ == "__main__":
    main()
