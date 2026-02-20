#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height

 
    def get_height(self) -> int:
        return self._height


class FloweringPlant(Plant):
    def __init__(self, name, get_height, color) -> None:
        super().__init__(name, get_height)
        self.color = color

    def bloom(self) -> None:
        self._height += 1

    def set_height(self, bloom) -> str:
        if bloom(self._height) >= 0:
            self._height += bloom(self._height)
        else:
            print(f"Invalid operation attempted: height "
                  f"{self._height}cm [REJECTED]")
            

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize) -> None:
        super().__init__(name, height, color)
        self.prize = prize

class GardenManager:
    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)

    @classmethod
    def create_garden_network(cls) -> list['GardenManager']:
        alice_garden = cls("Alice")
        bob_garden = cls("Bob")
        oak = Plant("Oak", 101)
        rose = FloweringPlant("Rose", 26, "red")
        sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
        alice_garden.add_plant(oak)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        return [alice_garden, bob_garden]
        
    class GardenStats:
        @staticmethod
        def height_valid(plant) -> str:
            if plant.height >= 0:
                return (f"Height validation test: True")
            else:
                return (f"Height validation test: False")

        @staticmethod
        def count_by_type(plants: list) -> str:
            regular = 0
            flowering = 0
            prize = 0
            total = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                    total += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                    total += 1
                elif isinstance(plant, Plant):
                    regular += 1
                    total += 1
                return (f"Plants added: {total}, Total growth: {total}cm\n"
                        f"Plant types: {regular} regular, "
                        f"{flowering} flowering, {prize} prize flowers")
                

    

def main():
    print("=== Garden Management System Demo ===")



    print(GardenStats.height_valid(rose))