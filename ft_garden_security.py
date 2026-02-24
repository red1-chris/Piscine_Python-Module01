class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, new_height) -> str:
        if new_height >= 0:
            self.__height += new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height "
                  f"{self.__height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age) -> str:
        if new_age >= 0:
            self.__age += new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age "
                  f"{self.__age} days [REJECTED]")
            print("Security: Negative age rejected")


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print("Plant created: Rose")
    rose.set_height(-12)
    rose.set_age(4)
    rose.set_height(14)
    rose.set_age(5)

    print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


if __name__ == "__main__":
    main()
