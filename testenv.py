from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time as t

from bubble import bubblesort
from insertion import insertion
from merge import merge
from quicksort import quicksort
from selection import selection

num = 100
runtime = []
transform = lambda x: x+' '*(10-len(x))

def gen_list(num):
    a = list(range(num))
    np.random.shuffle(a)
    return a
    
def b(a,size,r):
    t0 = t.time()
    bubblesort(a,size)
    t1 = t.time()
    print('bubble')
    r.append('bubble')
    return round(t1 - t0, 6)

def i(a,size,r):
    t0 = t.time()
    insertion(a,size)
    t1 = t.time()
    print('insertion')
    r.append('insertion')
    return round(t1 - t0, 6)

def m(a,size,r):
    t0 = t.time()
    merge(a)
    t1 = t.time()
    print('merge')
    r.append('merge')
    return round(t1 - t0, 6)

def q(a,size,r):
    t0 = t.time()
    quicksort(a)
    t1 = t.time()
    print('quick')
    r.append('quick')
    return round(t1 - t0, 6)

def s(a,size,r):
    t0 = t.time()
    selection(a,size)
    t1 = t.time()
    print('selection')
    r.append('selection')
    return round(t1 - t0, 6)



with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(b, gen_list(num),num,runtime),
        executor.submit(i, gen_list(num),num,runtime),
        executor.submit(m, gen_list(num),num,runtime),
        executor.submit(q, gen_list(num),num,runtime),
        executor.submit(s, gen_list(num),num,runtime),
    ]
    results = [f.result() for f in futures]
    print(runtime)
    print()
    for algo,time in zip(['bubble','insertion','merge','quick','selection'],results):
        print(f'{algo} => {time} (seconds)')

