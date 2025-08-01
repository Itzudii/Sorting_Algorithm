import numpy as np
a = list(range(1,100))
np.random.shuffle(a)
size = len(a)
from constant import delay
import time as t

# frames = []

def partition(arr,low,high):
    pivot = arr[high]
    swapi = low
    for k in range(low,high):
        delay()
        if arr[k] <= pivot:
            delay()
            arr[k],arr[swapi] = arr[swapi],arr[k]
            # frames.append(arr.copy())
            swapi+=1
    delay()
    arr[high],arr[swapi] = arr[swapi],arr[high]
    # frames.append(arr.copy())
    return swapi


def quicksort(arr,low,high):
    delay()
    if low < high:
        index = partition(arr,low,high)
        quicksort(arr,low,index-1)
        quicksort(arr,index,high)



if __name__ == '__main__':
    t0 = t.time()
    quicksort(a,0,len(a)-1)
    t1 = t.time()
    print("Sorted array:", a)
    print("Execution time (s):", round(t1 - t0, 6))