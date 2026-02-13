#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    garden = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for plant in garden:
        print(plant)


if __name__ == "__main__":
    main()
