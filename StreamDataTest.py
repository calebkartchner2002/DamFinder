from StreamData import StreamData

def sort(arr):
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if(arr[x].compareTo(arr[y])<0):
                temp = arr[x]
                arr[x] = arr[y]
                arr[y] = temp
stream1 = StreamData("Here", 10, 10, 10, 10)
stream2 = StreamData("L", 10, 10, 10, 20)
streams = []
streams.append(stream1)
streams.append(stream2)
sort(streams)
print(stream1)
print(streams[0])