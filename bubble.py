import numpy as np
import time as t
a = list(range(1,100))
np.random.shuffle(a)
size = len(a)
from constant import delay

def bubblesort(a,size):
    step = 0
    isSwap = False
    delay()
    while not isSwap:
        for i in range(size-1):
            delay()
            if a[i] > a[i+1]:
                delay()
                a[i],a[i+1] = a[i+1],a[i]
                isSwap = True
            step+=1
        isSwap = False if isSwap else True
        

    return a,step

    
if __name__ == '__main__':
    
    t0 = t.time()
    sorted_array,steps = bubblesort(a,size)
    t1 = t.time()
    print("Sorted array:", sorted_array)
    print("Total comparisons:", steps)
    print("Execution time (s):", round(t1 - t0, 6))