import time
import random
import heapq

# Génère des floats aléatoires
data = [random.uniform(-1000, 1000) for _ in range(10000)]

# Fonctions de tri
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        more = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)

# Benchmarking
def benchmark(sort_func, name, inplace=True):
    to_sort = data.copy()
    start = time.perf_counter()
    if inplace:
        sort_func(to_sort)
    else:
        to_sort = sort_func(to_sort)
    end = time.perf_counter()
    print(f"{name:17s}: {end - start:.6f} sec")

# Exécutions (désactive les très lents si tu veux gagner du temps)
# benchmark(bubble_sort, "Bubble Sort")
# benchmark(insertion_sort, "Insertion Sort")
# benchmark(selection_sort, "Selection Sort")
benchmark(merge_sort, "Merge Sort")
benchmark(heap_sort, "Heap Sort", inplace=False)
benchmark(quick_sort, "Quick Sort (rec)", inplace=False)
benchmark(lambda x: x.sort(), "Python .sort()")
