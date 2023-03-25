class StreamData:
    def __init__(self, name, lat, long, vel, height):
        self.name = name
        self.lat = lat
        self.long = long
        self.vel = vel
        self.height = height
    def __str__(self):
        return f"{self.name}: Latitude: {self.lat}, Longitude: {self.long}, Velocity: {self.vel}, Height: {self.height}"   
    def compareTo(self, other):
        selfE = self.vel*9.81*self.height*0.9
        otherE = other.vel*9.81*other.height*0.9
        return selfE-otherE
