class phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        print(f"The phone brand is {self.brand} and {self.model}")

class android(phone):
    def __init__(self, brand, model):
        phone.__init__(self,brand, model)

selpon = phone("Samsung","A03s")
selpon.describePhone()
cp = android("Xiaomi", "A23")
cp.describePhone()