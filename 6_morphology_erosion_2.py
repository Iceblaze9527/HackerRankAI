def count_erosion(image, kernel):
    pass

image = [
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,1,1,0],
    [1,1,1,1,1],
]

kernel = [
    [1],
    [1],
    [1],
]

print(count_erosion(image, kernel))