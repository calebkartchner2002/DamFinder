class StreamData:
    def __init__(self, name, lat, long, flow, height):
        self.name = name
        self.lat = lat
        self.long = long
        self.flow = flow
        self.height = height
    def __str__(self):
        return f"{self.name}: Latitude: {self.lat}, Longitude: {self.long}, Velocity: {self.flow}, Height: {self.height}"   
    def __gt__(self, other):
        selfE = self.flow*9.81*self.height*0.9
        otherE = other.flow*9.81*other.height*0.9
        if(selfE-otherE>0):
            return True
        else:
            return False
