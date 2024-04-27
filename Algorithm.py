import random
import time
import math


def generate_points(n):
    points = set()
    while len(points) < n:
        x = random.randint(0, 32767)
        y = random.randint(0, 32767)
        points.add((x, y))
    return list(points)


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
    ns = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    results = []
    test_points = [(1, 2), (2, 1), (7, 5), (12, 3), (15, 8), (12, 9), (20, 9), (29, 10), (1, 10)]
    bf_start_time = time.time()
    bf_pair = brute_force_closest_pair(test_points)
    bf_time = (time.time() - bf_start_time) * 1000

    dq_start_time = time.time()
    dq_pair = closest_pair_dc(test_points)
    dq_time = (time.time() - dq_start_time) * 1000

    # Print results
    print("Brute-Force Closest Pair:", test_points[bf_pair[0]], ",", test_points[bf_pair[1]])
    print("Brute-Force Execution Time:", f"{bf_time:.2f} milliseconds")

    print("Divide-and-Conquer Closest Pair:", test_points[dq_pair[0]], ",", test_points[dq_pair[1]])
    print("Divide-and-Conquer Execution Time:", f"{dq_time:.2f} milliseconds")
    for n in ns:
        print(f"Running for n = {n}...")
        points = generate_points(n)
        points.sort(key=lambda point: point[0])

        bf_time = measure_runtime(lambda pts: brute_force_closest_pair(pts), points)
        dq_time = measure_runtime(lambda pts: closest_pair_dc(pts), points)

        results.append((n, bf_time, dq_time))

    for result in results:
        print(
            f"n = {result[0]}, "
            f"ALG1 : Brute-Force : {result[1]:.2f} milliseconds, "
            f"ALG2: Divide-and-Conquer : {result[2]:.2f} milliseconds"
        )


if __name__ == "__main__":
    main()
