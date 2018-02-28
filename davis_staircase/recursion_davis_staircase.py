def get_ways_staircases(height):
    height = height - 1
    heights = [1, 2, 4]
    if height <= 3:
        return heights[height]
    for i in range(3, height + 1):
        heights[i % 3] = heights[0] + heights[1] + heights[2]
    return heights[height % 3]

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(get_ways_staircases(n))
