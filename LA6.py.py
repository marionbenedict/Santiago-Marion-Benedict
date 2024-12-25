class Laptop:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    
    def laptop_information(self):
        pass

laptop = Laptop("Lenovo", "Legion Pro 7i Gen 8")

print(laptop.laptop_information())