class Car:
def __init__(self, model, color, year):
    self.model = model
    self.year = year
    self.color = color
    def stop(self):
        print("Car stopped")
gentra = Car('Racon', 'Black', 2022)
gentra.stop()
