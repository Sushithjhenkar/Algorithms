import time
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force_closest_pair(points):
    min_dist = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (i, j)
    return pair


def closest_pair_dc(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)

    mid = len(points) // 2
    mid_point = points[mid]

    dl = closest_pair_dc(points[:mid])
    dr = closest_pair_dc(points[mid:])

    if distance(points[dl[0]], points[dl[1]]) < distance(points[dr[0]], points[dr[1]]):
        dmin = distance(points[dl[0]], points[dl[1]])
        min_pair = dl
    else:
        dmin = distance(points[dr[0]], points[dr[1]])
        min_pair = dr

    strip = [p for p in points if abs(p[0] - mid_point[0]) < dmin]
    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < dmin:
                dist = distance(strip[i], strip[j])
                if dist < dmin:
                    dmin = dist
                    min_pair = (points.index(strip[i]), points.index(strip[j]))
            else:
                break
    return min_pair


def measure_runtime(func, points):
    start_time = time.time()
    func(points)
    return (time.time() - start_time) * 1000


def main():
    points = [(1, 2), (2, 1), (7, 5), (12, 3), (15, 8), (12,9), (20,9), (29,10), (1,10)]

    bf_start_time = time.time()
    bf_pair = brute_force_closest_pair(points)
    bf_time = (time.time() - bf_start_time) * 1000

    dq_start_time = time.time()
    dq_pair = closest_pair_dc(points)
    dq_time = (time.time() - dq_start_time) * 1000

    # Print results
    print("Brute-Force Closest Pair:", points[bf_pair[0]], ",", points[bf_pair[1]])
    print("Brute-Force Execution Time:", f"{bf_time:.2f} milliseconds")

    print("Divide-and-Conquer Closest Pair:", points[dq_pair[0]], ",", points[dq_pair[1]])
    print("Divide-and-Conquer Execution Time:", f"{dq_time:.2f} milliseconds")


if __name__ == "__main__":
    main()
