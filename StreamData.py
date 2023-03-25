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
        return self-other
    
def quicksort(arr):
    quicksortRec(arr, 0, len(arr)-1)

def quicksortRec(arr, left, right):

    if left >= right:
        return
    pivot = int((right+left)/2)
    updatedPivot = partition(arr, left, right, pivot)
    quicksortRec(arr, left, updatedPivot-1)
    quicksortRec(arr, updatedPivot+1, right)

def partition(arr, beg, end, pivotPosition):
    pivotElem = arr[pivotPosition]

    swap(arr, pivotPosition, end)
    right = end
    left = beg
    while(left<right):
        while(arr[left] <= arr[pivotElem] and left<end):
            left = left+1

        while(arr[right] >= arr[pivotElem] and right>beg):
            right = right-1
        if left < right:
            swap(arr, left, right)
    swap(arr, left, end)
    return left
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp




test = [0]*10
for i in range(10):
    test[i] = 10-i

stream1 = StreamData("Here", 10, 10, 10, 10)
stream2 = StreamData("Not Here", 20, 10, 5, 15)
streamArr = [stream1, stream2]
print(stream1.height)
print(stream1)
quicksort(test)
for elem in test:
    print(elem)