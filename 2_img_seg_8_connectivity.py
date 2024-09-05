def eight_connectivity(image):
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    n_rows = len(image)
    n_cols = len(image[0])
    
    visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
    
    def dfs(row, col):
        stack = [(row, col)]
        visited[row][col] = True
        
        while stack:
            r, c = stack.pop()
            for dx, dy in neighbors:
                x, y = r + dx, c + dy
            
                if (0 <= x < n_rows) and (0 <= y < n_cols):
                    if (image[x][y] == 1) and (visited[x][y] == False):
                        stack.append((x, y))
                        visited[x][y] = True
    
    num_components = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if (image[i][j] == 1) and (visited[i][j] == False):
                dfs(i,j)
                num_components += 1
                
    return num_components

image = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

print(eight_connectivity(image))
