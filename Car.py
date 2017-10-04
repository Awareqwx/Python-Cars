class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if price > 10000 else 0.12
    def displayAll(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel * 100) + "%"
        print "Mileage: " + str(self.mileage) + " miles"
        print "Tax: " + str(self.tax * 100) + "%"

jalopy = Car(500, 10, 0.5, 250000)
sports = Car(25000, 120, 1, 15000)
race = Car(125000, 250, 0.3, 3000)
beetle = Car(7500, 75, 0.7, 100000)
sedan = Car(5000, 70, 0.8, 125000)
motorcycle = Car(2500, 85, 0.9, 75000)