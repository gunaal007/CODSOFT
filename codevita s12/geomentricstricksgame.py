from itertools import combinations
from math import sqrt
def calculate_polygon_area(polygon):
    n = len(polygon)
    area = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2
def is_closed_figure(sticks):
    graph = {}
    for x1, y1, x2, y2 in sticks:
        graph[(x1, y1)] = graph.get((x1, y1), []) + [(x2, y2)]
        graph[(x2, y2)] = graph.get((x2, y2), []) + [(x1, y1)] 
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, node):
                return True
        return False  
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
def leftover_sticks(sticks, closed_polygon):
    closed_segments = set(tuple(sorted([p1, p2])) for p1, p2 in zip(closed_polygon, closed_polygon[1:] + closed_polygon[:1]))
    leftovers = []
    for x1, y1, x2, y2 in sticks:
        if (tuple(sorted([(x1, y1), (x2, y2)]))) not in closed_segments:
            leftovers.append((x1, y1, x2, y2))
    return leftovers
def can_form_same_shape_and_size(leftovers, area):
    for r in range(3, len(leftovers) + 1):
        for comb in combinations(leftovers, r):
            polygon = [(x1, y1) for x1, y1, x2, y2 in comb] + [(x2, y2) for x1, y1, x2, y2 in comb]
            if calculate_polygon_area(polygon) == area:
                return True
    return False
def main():
    n = int(input())
    sticks = []
    for _ in range(n):
        sticks.append(tuple(map(int, input().split())))
    
    if is_closed_figure(sticks):
        print("Yes")
        closed_polygon = [(x1, y1) for x1, y1, x2, y2 in sticks]
        area = calculate_polygon_area(closed_polygon)
        leftovers = leftover_sticks(sticks, closed_polygon)
        if can_form_same_shape_and_size(leftovers, area):
            print("Yes")
        else:
            print("No")
        print(f"{area:.2f}")
    else:
        print("No")
if _name_ == "_main_":
    main()