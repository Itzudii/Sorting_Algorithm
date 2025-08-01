import pygame
pygame.init()
import sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time as t

from bubble import bubblesort
from insertion import insertion
from merge import mergesort
from quicksort import quicksort
from selection import selection

num = 100
runtime = {
    "bubble":0,
    "insertion":0,
    "selection":0,
    "quick":0,
    "merge":0
}
transform = lambda x: x+' '*(10-len(x))

def gen_list(num):
    a = list(range(num))
    np.random.shuffle(a)
    return a
    
def b(a,size,r):
    t0 = t.time()
    bubblesort(a,size)
    t1 = t.time()
    r['bubble']=round(t1 - t0, 6)
    return round(t1 - t0, 6)

def i(a,size,r):
    t0 = t.time()
    insertion(a,size)
    t1 = t.time()
    r['insertion'] = round(t1 - t0, 6)
    return round(t1 - t0, 6)

def s(a,size,r):
    t0 = t.time()
    selection(a,size)
    t1 = t.time()
    r['selection'] = round(t1 - t0, 6)
    return round(t1 - t0, 6)

def q(a,size,r):
    t0 = t.time()
    quicksort(a,0,size-1)
    t1 = t.time()
    r['quick'] = round(t1 - t0, 6)
    return round(t1 - t0, 6)

def m(a,size,r):
    t0 = t.time()
    mergesort(a,0,size-1)
    t1 = t.time()
    r['merge']=round(t1 - t0, 6)
    return round(t1 - t0, 6)


def main(samples):
    width, height = 800, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algoritgm")
    font  =  pygame.font.Font(None,32)
    clock = pygame.time.Clock()


    def drawarray(array,x,y):
        width = 1
        gap = 1
        for i in range(len(array)):
            bar = pygame.Rect((x+i)*(width+gap),y,width,array[i])
            pygame.draw.rect(screen,'red',bar)

 
    running = True
    x = 14
    y = 18
    w = 226-x
    h = 117-y
    
    while running:
        screen.fill((30, 30, 30)) 
        i = 0
        for key,value in runtime.items():
            text = font.render(f'{key}: {value} second',True,'white')
            screen.blit(text,(300,(i*150)))
            i+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
        
        
        with ThreadPoolExecutor() as executor:
            for i in range(5):
                executor.submit(drawarray, samples[i],x,(y+h+20)*i)

        pygame.display.flip()     
    pygame.quit()
    sys.exit()

samples = [gen_list(num) for _ in range(5)]
with ThreadPoolExecutor() as executor:
        executor.submit(b, samples[0],num,runtime),
        executor.submit(i, samples[1],num,runtime),
        executor.submit(s, samples[2],num,runtime),
        executor.submit(q, samples[3],num,runtime),
        executor.submit(m, samples[4],num,runtime),
        executor.submit(main, samples),

print(runtime)