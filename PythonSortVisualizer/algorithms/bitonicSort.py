import time
from colors import *

def c_swap(a, b, c, d):
    if (d == 1 and a[b] > a[c]) or (d == 0 and a[b] < a[c]):
        a[b], a[c] = a[c], a[b]

def merge(a, b, cnt, d):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(b, b + k):
            c_swap(a, i, i + k, d)
        merge(a, b, k, d)
        merge(a, b + k, k, d)
 
def bitonic_sort(a, b, cnt, d, drawData, timeTick):
    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort(a, b, k, 1, drawData, timeTick)
        bitonic_sort(a, b + k, k, 0, drawData, timeTick)
        merge(a, b, cnt, d)
        
        drawData(a, [PURPLE if x >= b and x < k else YELLOW if x == k 
                        else DARK_BLUE if x > k and x <=cnt else BLUE for x in range(len(a))])
        time.sleep(timeTick)

    drawData(a, [BLUE for x in range(len(a))])