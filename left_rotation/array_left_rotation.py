def array_left_rotation(a, n, k):
    # a: list, n : length of the list, k : rotating number
    class RotatingNumber(object):
        def __init__(self, value, i, n, k):
            """ i: original index, n: length of the array, k : rotating number """
            self.index = (i - k) % n
            self.value = value
        
        def index(self):
            return self.index
    result = []    
    for i in range(n):
        rn = RotatingNumber(a[i], i, n, k)
        result.insert(rn.index, rn.value)
    return result

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
