def count_erosion(image, kernel):
    n_rows = len(image)
    n_cols = len(image[0])
    kernel_center_x = len(kernel) // 2
    kernel_center_y = len(kernel[0]) // 2
    
    n_eroded = 0
    for x in range(n_rows):
        for y in range(n_cols):
            if image[x][y] == 1:
                is_eroded = False
                for dx in range(-kernel_center_x, kernel_center_x + 1):
                    for dy in range(-kernel_center_y, kernel_center_y + 1):
                        if (0 <= (x + dx) < n_rows) and (0 <= (y + dy) < n_cols):
                            if not((image[x + dx][y + dy] == 1) and (kernel[kernel_center_x + dx][kernel_center_y + dy] == 1)):
                                is_eroded = True
                                break
                    if is_eroded:
                        break
                if is_eroded:
                    n_eroded += 1
            else:
                n_eroded += 1
    
    return n_rows * n_cols - n_eroded

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

print(count_erosion(image, kernel))

# import cv2
# import numpy as np

# eroded_image = cv2.erode(np.array(image, dtype=np.uint8), np.array(kernel, dtype=np.uint8), iterations=1)
# print(np.sum(eroded_image))