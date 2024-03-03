import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import permutations

# 使用Haversine公式计算两点间距离的函数
def haversine(coord1, coord2):
    # 地球半径（千米）
    R = 6371.0
    lat1, lon1 = np.radians(coord1)
    lat2, lon2 = np.radians(coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c

def find_shortest_path(points):
    coordinates = np.array(points)
    distance_matrix = squareform(pdist(coordinates, lambda u, v: haversine(u, v)))

    n = len(points)
    min_distance = float('inf')
    shortest_path = None

    # 减少一个点考虑
    for start_point in range(n-1):
        for perm in permutations(range(n)):
            if perm[0] == start_point:
                current_distance = sum(distance_matrix[perm[i], perm[i+1]] for i in range(n - 1))
                if current_distance < min_distance:
                    min_distance = current_distance
                    shortest_path = [points[index] for index in perm]

    return shortest_path, min_distance

# 最好少于8个
# points = [[116.4074, 39.9042], [116.232633,40.051922], [116.266965,39.623799], [116.717405,39.841358],
#           [115.864591,40.10026], [116.532364,38.858118], [118.509903,36.06821], [120.004044,36.387255], [120.597306,32.02812]]
# shortest_path, min_distance = find_shortest_path(points)
# print(shortest_path, min_distance)
#
#