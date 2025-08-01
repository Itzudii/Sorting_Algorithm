import numpy as np
a = list(range(1,100))
np.random.shuffle(a)
size = len(a)
from constant import delay
import time as t

def merge(a,x1,y1,x2,y2):
    i = x1
    j = x2
    while True:
        delay()
        if j >= y2:
           break
        delay()
        if a[i] >= a[j]:
            delay()
            a.insert(i,a.pop(j))
            j+=1
        else:
            i+=1

def mergesort(a,low,high):
    delay()
    if len(a[low:high]) <= 1:
        return low,high
    mid = low+(abs(high-low)//2)
    x1,y1 = mergesort(a,low,mid)
    x2,y2 = mergesort(a,mid,high)
    merge(a,x1,y1,x2,y2)
    return low,high



if __name__ == '__main__':
    t0 = t.time()
    sorted_array = mergesort(a,0,len(a))
    t1 = t.time()
    print("Sorted array:", a)
    print("Execution time (s):", round(t1 - t0, 6))