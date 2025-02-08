def max_cycle_length(grid):
    m, n = len(grid), len(grid[0])
    graph = {}
    for i in range(m):
        for j in range(n):
            graph[(i, j)] = []
            if grid[i][j] == '/':
                if i + 1 < m and j - 1 >= 0:
                    graph[(i, j)].append((i + 1, j - 1))
                if i - 1 >= 0 and j + 1 < n:
                    graph[(i, j)].append((i - 1, j + 1))
            elif grid[i][j] == '\\':
                if i + 1 < m and j + 1 < n:
                    graph[(i, j)].append((i + 1, j + 1))
                if i - 1 >= 0 and j - 1 >= 0:
                    graph[(i, j)].append((i - 1, j - 1))
    def dfs(node, visited, path_len):
        if node in visited:
            return path_len - visited[node]
        visited[node] = path_len
        max_len = 0
        for neighbor in graph[node]:
            max_len = max(max_len, dfs(neighbor, visited, path_len + 1))
        return max_len
    max_len = 0
    visited = {}
    for node in graph:
        max_len = max(max_len, dfs(node, visited, 1))
    return max_len
grid = [
    ["/", "/", "0", "0", "\\"],
    ["0", "0", "0", "/", "0"],
    ["0", "\\", "0", "0", "/"],
    ["/", "\\", "/", "/", "0"],
    ["0", "0", "\\", "\\", "\\"]
]
print(max_cycle_length(grid))