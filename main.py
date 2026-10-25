class Car:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def get_into(self):
        print(self.year, self.marka, self.model)

        my_car = Car("Toyota", "Camry", 2022)

print("Marka -", my_car.marka)
print("Model -", my_car.model)
print("Year -", my_car.year)

my_car.get_info()