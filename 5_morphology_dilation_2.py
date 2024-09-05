def count_dilation(image, kernel):
    pass

image = [
    [0,0,0,0],
    [0,1,1,0],
    [0,0,0,0],
]

kernel = [
    [1,0],
    [1,1],
]

print(count_dilation(image, kernel))