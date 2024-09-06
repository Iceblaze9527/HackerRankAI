def count_dilation(image, kernel):
    n_rows = len(image)
    n_cols = len(image[0])
    
    kernel_center_x = len(kernel) // 2
    kernel_center_y = len(kernel[0]) // 2
    
    n_dilated = 0
    for x in range(n_rows):
        for y in range(n_cols):
            if (image[x][y] == 0):
                is_to_dilate = False
                for dx in range(-kernel_center_x,kernel_center_x + 1):
                    for dy in range(-kernel_center_y,kernel_center_y + 1):
                        if (0 <= x+dx < n_rows) and (0 <= y+dy < n_cols):
                            if (image[x+dx][y+dy] == 1) and (kernel[kernel_center_x+dx][kernel_center_y+dy] == 1):
                                is_to_dilate = True
                                break
                    if is_to_dilate:
                        break
                if is_to_dilate:
                    n_dilated += 1
            else:
                n_dilated += 1
    
    return n_dilated

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

print(count_dilation(image, kernel))

# import cv2
# import numpy as np

# dilated_image = cv2.dilate(np.array(image, dtype=np.uint8), np.array(kernel, dtype=np.uint8), iterations=1)
# print(np.sum(dilated_image))

