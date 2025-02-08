from collections import defaultdict
import math
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
def find_intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  # Lines are parallel
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    if (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2) and
            min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4)):
        return (px, py)
    return None
def calculate_intensity(lines, k):
    intersections = defaultdict(list)
    n = len(lines)
    for i in range(n):
        for j in range(i + 1, n):
            intersection = find_intersection(lines[i], lines[j])
            if intersection:
                intersections[intersection].append((i, j))
    total_intensity = 0
    for point, contributing_lines in intersections.items():
        if len(contributing_lines) != k:
            continue
        intensities = []
        px, py = point
        for line_index in set(i for pair in contributing_lines for i in pair):
            x1, y1, x2, y2 = lines[line_index]
            if (px, py) == (x1, y1):
                intensities.append(distance(px, py, x2, y2))
            elif (px, py) == (x2, y2):
                intensities.append(distance(px, py, x1, y1))
            else:  # The star cuts the line into two parts
                intensities.append(distance(px, py, x1, y1))
                intensities.append(distance(px, py, x2, y2))
        total_intensity += min(intensities)
    return total_intensity
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
k = int(input())
print(calculate_intensity(lines, k))