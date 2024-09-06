def dilation(image, kernel):
    n_x = len(image)
    n_y = len(image[0])
    
    kernel_center_x = len(kernel) // 2
    kernel_center_y = len(kernel[0]) // 2
    
    new_image = [[0 for _ in range(n_y)] for _ in range(n_x)]
    for x in range(n_x):
        for y in range(n_y):
            if (image[x][y] == 0):
                is_to_dilate = False
                for dx in range(-kernel_center_x,kernel_center_x + 1):
                    for dy in range(-kernel_center_y,kernel_center_y + 1):
                        if (0 <= x+dx < n_x) and (0 <= y+dy < n_y):
                            if (image[x+dx][y+dy] == 1) and (kernel[kernel_center_x+dx][kernel_center_y+dy] == 1):
                                is_to_dilate = True
                                break
                    if is_to_dilate:
                        break
                if is_to_dilate:
                    new_image[x][y] = 1
            else:
                new_image[x][y] = 1
    
    return new_image

def erosion(image, kernel):
    n_x = len(image)
    n_y = len(image[0])
    
    kernel_center_x = len(kernel) // 2
    kernel_center_y = len(kernel[0]) // 2
    
    new_image = [[1 for _ in range(n_y)] for _ in range(n_x)]
    for x in range(n_x):
        for y in range(n_y):
            if image[x][y] == 1:
                is_to_erode = False
                for dx in range(-kernel_center_x, kernel_center_x + 1):
                    for dy in range(-kernel_center_y, kernel_center_y + 1):
                        if (0 <= (x + dx) < n_x) and (0 <= (y + dy) < n_y):
                            if not((image[x + dx][y + dy] == 1) and (kernel[kernel_center_x + dx][kernel_center_y + dy] == 1)):
                                is_to_erode = True
                                break
                    if is_to_erode:
                        break
                if is_to_erode:
                    new_image[x][y] = 0
            else:
                new_image[x][y] = 0
    
    return new_image

def count_opening(image, kernel):
    opened_image = dilation(erosion(image, kernel), kernel)
    
    n_opening = sum([sum(row) for row in opened_image])
    
    return n_opening


image = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

kernel = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

print(count_opening(image, kernel))

# import cv2
# import numpy as np

# opened_image = cv2.morphologyEx(np.array(image, dtype=np.uint8), cv2.MORPH_OPEN, np.array(kernel, dtype=np.uint8))
# print(np.sum(opened_image))