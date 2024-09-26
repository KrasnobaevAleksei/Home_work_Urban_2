class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(new_floor):
                print(i+1)
        else:
            print("Такого этажа не существует в этом доме")

# if __name__ == "__main":
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)