#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = 0
        self.set_height(height)
        self.is_blooming = False

    def get_height(self) -> int:
        return self._height

    def set_height(self, height) -> str:
        if height >= 0:
            self._height = height
        else:
            print(f"Invalid operation attempted: height "
                  f"{height}cm [REJECTED]")
            
    def bloom(self) -> None:
        self.is_blooming = True
        self._height += 1

    def __str__(self):
        return f"{self.name}: {self.get_height()}cm"
        
class FloweringPlant(Plant):
    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def blooming(self) -> str:
        if self.is_blooming:
            return "(blooming)"
        return ""
        
    def __str__(self):
        status = self.blooming()
        return f"{super().__str__()}, {self.color} flowers {self.blooming()}"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize) -> None:
        super().__init__(name, height, color)
        self.prize = 0
        self.prizepoint()

    def prizepoint(self) -> int:
        if self.get_height() > 30:
            self.prize = 10

    def bloom(self) -> None:
        super().bloom()
        self.prizepoint()

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.prize}"

class GardenManager:
    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    @classmethod
    def create_garden_network(cls) -> list['GardenManager']:
        alice_garden = cls("Alice")
        bob_garden = cls("Bob")
        oak = Plant("Oak Tree", 101)
        rose = FloweringPlant("Rose", 26, "red")
        sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
        alice_garden.add_plant(oak)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        return [alice_garden, bob_garden]
        
    class GardenStats:
        @staticmethod
        def height_valid(plant) -> str:
            if plant._height >= 0:
                return (f"Height validation test: True")
            else:
                return (f"Height validation test: False")

        @staticmethod
        def count_by_type(plants: list) -> str:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                elif isinstance(plant, Plant):
                    counts["regular"] += 1
            total = sum(counts.values())
            return (f"Plants added: {total}, Total growth: {total}cm\n"
                    f"Plant types: {counts['regular']} regular, "
                    f"{counts['flowering']} flowering, {counts['prize']} prize flowers")


def main():
    print("=== Garden Management System Demo ===")



    print(GardenStats.height_valid(rose))