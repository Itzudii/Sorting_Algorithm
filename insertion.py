import numpy as np
a = list(range(1,100))
np.random.shuffle(a)
size = len(a)
from constant import delay
import time as t

def insertion(a, size):
    step = 0
    for i in range(1, size):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            delay()
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a,step

    
if __name__ == '__main__':
    t0 = t.time()
    sorted_array,steps = insertion(a,size)
    t1 = t.time()
    print("Sorted array:", sorted_array)
    print("Total comparisons:", steps)
    print("Execution time (s):", round(t1 - t0, 6))