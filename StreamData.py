class StreamData:
    def __init__(self, name, lat, long, vel, height):
        self.name = name
        self.lat = lat
        self.long = long
        self.vel = vel
        self.height = height
    def __str__(self):
        return f"{self.name}: Latitude: {self.lat}, Longitude: {self.long}, Velocity: {self.vel}, Height: {self.height}"   

stream1 = StreamData("Here", 10, 10, 10, 10)
print(stream1)