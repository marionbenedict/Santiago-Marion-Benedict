class toy():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describeToys(self):
        print(f"The name of this toy is {self.name} and the {self.price}")

class car(toy):
    def __init__(self, name, price):
        super().__init__(name, price)

laruan = toy("Joyboy", 1200)
laruan.describeToys()
asd = car("trycicle", 100000)
asd.describeToys()