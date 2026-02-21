#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = 0
        self.height_error = ""
        self.set_height(height)
        self.is_blooming = False

    def get_height(self) -> int:
        return self._height

    def set_height(self, height) -> str:
        if height >= 0:
            self._height = height
        else:
            self._height = height
            self.height_error = " [REJECTED]"
            
    def bloom(self) -> None:
        self.is_blooming = True
        self._height += 1

    def __str__(self) -> str:
        base = f"{self.name}: {self.get_height()}cm"
        return f"{base} {self.height_error}".strip()
        
class FloweringPlant(Plant):
    def __init__(self, name, height, color) -> None:
        super().__init__(name, height)
        self.color = color

    def blooming(self) -> str:
        if self.is_blooming:
            return "(blooming)"
        return ""
        
    def __str__(self) -> str:
        status = self.blooming()
        res = f"{super().__str__()}, {self.color} flower {self.blooming()}"
        return res.strip()

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

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize}"

class GardenManager:
    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        if "True" in self.GardenStats.height_valid(plant):
            self.plants.append(plant)
        else:
            print(f"Addition denied: {plant.name} on account of {plant._height}cm {plant.height_error}")

    @classmethod
    def create_garden_network(cls) -> list['GardenManager']:
        alice_garden = cls("Alice")
        bob_garden = cls("Bob")
        oak = Plant("Oak Tree", 101)
        rose = FloweringPlant("Rose", 26, "red")
        sunflower = PrizeFlower("Sunflower", 28, "yellow", 10)
        alice_garden.add_plant(oak)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        return [alice_garden, bob_garden]
    
    def garden_scores(self) -> str:
        total_height = 0
        for plant in self.plants:
            total_height += plant._height
        return total_height

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


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    gardens = GardenManager.create_garden_network()
    alice_garden = gardens[0]
    cactus = Plant("Cactus", 18)
    cow = PrizeFlower("Cow", -120, "blue", 0)
    tulipe = FloweringPlant("Tulip", 30, "orange")
    gardens[1].add_plant(cactus)
    gardens[1].add_plant(cow)
    gardens[1].add_plant(tulipe)
    rose = alice_garden.plants[1]
    print("\n* Blooming Flowers: *")
    print(f"Before Growth: {rose}")
    rose.bloom()
    print(f"After Growth: {rose}\n")
    sunflower = alice_garden.plants[2]
    print(f"Before Growth: {sunflower}")
    for _ in range(12):
        sunflower.bloom()
    print(f"After Growth: {sunflower}\n")
    print("* Gardens: *")
    for garden in gardens:
        print(f"Gardener: {garden.owner}")
        for p in garden.plants:
            valid = GardenManager.GardenStats.height_valid(p)
            print(f" > {p} | {valid}")

        stats = GardenManager.GardenStats.count_by_type(garden.plants)
        print(f"\n{garden.owner}'s Results:")
        print(stats.strip())
        print(f"Garden score: {garden.garden_scores()}\n")


if __name__ == "__main__":
    main()
