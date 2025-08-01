import numpy as np
a = list(range(1,100))
np.random.shuffle(a)
size = len(a)
from constant import delay
import time as t
def selection(a,size):
    step = 0
    for i in range(size):
        small = i
        for j in range(i,size):
            delay()
            if a[j] < a[small]:
                small = j
            step+=1
        delay()
        a[i],a[small] = a[small],a[i]
        

    return a,step

    
if __name__ == '__main__':
    t0 = t.time()
    sorted_array,steps = selection(a,size)
    t1 = t.time()
    print("Sorted array:", sorted_array)
    print("Total comparisons:", steps)
    print("Execution time (s):", round(t1 - t0, 6))