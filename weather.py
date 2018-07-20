class weather:
    def __init__(self, city, date, high, low):
        self.city = city
        self.date = date
        self.high = high 
        self.low = low
        
    def printWeather(self):
        print(self.city)
        print(self.date)
        print(self.high)
        print(self.low)