def four_connectivity(image):
    # Define the 4-connectivity (neighbors)
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Get the dimensions of the image
    rows = len(image)
    cols = len(image[0])
    
    # Initialize a visited matrix with False
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Function to perform DFS and mark all connected pixels
    def dfs(r, c):
        # Stack for DFS
        stack = [(r, c)]
        visited[r][c] = True
        
        while stack:
            x, y = stack.pop()
            for dr, dc in neighbors:
                nx, ny = x + dr, y + dc
                if 0 <= nx < rows and 0 <= ny < cols:  # Check bounds
                    if image[nx][ny] == 1 and not visited[nx][ny]:  # Unvisited and part of a component
                        visited[nx][ny] = True
                        stack.append((nx, ny))
    
    # Initialize the number of connected components
    num_components = 0
    
    # Iterate over each pixel in the image
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == 1 and not visited[i][j]:  # Start a new component
                dfs(i, j)
                num_components += 1  # Increment count for each new component
    
    return num_components

# Example binary image based on the input provided
image = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

print(four_connectivity(image))
