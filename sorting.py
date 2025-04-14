import random
import time
from collections import deque

class SortNumbers:
    def __init__(self, arr=None):
        """if arr is None:
            arr = []"""
        self.arr = arr if arr else []

    def display(self):
        print("Current list:", self.arr)

    def generate_random_list(self, taille=500, min_val=0.0, max_val=500000.0):
        self.arr = [round(random.uniform(min_val, max_val), 2) for _ in range(taille)]
        return self.arr
    
    def measure_time(self, sort_method):
        start_time = time.time()
        sorted_data = sort_method()
        end_time = time.time()
        return sorted_data, end_time - start_time

    def sort_selection(self, debug=False):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            if debug:
                print(f"Step: {self.arr}")
        return self.arr
    
    def sort_insertion(self, debug=False):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
            if debug:
                print(f"Step: {self.arr}")
        return self.arr
    
    def sort_quick(self, debug=False):
        def _sort_quick(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            moins = [x for x in arr[1:] if x <= pivot]
            plus = [x for x in arr[1:] if x > pivot]
            if debug:
                print(f"Pivot: {pivot}, Moins: {moins}, Plus: {plus}")
            return _sort_quick(moins) + [pivot] + _sort_quick(plus)
            
        self.arr = _sort_quick(self.arr)
        if debug:
                print(f"Step: {self.arr}")
        return self.arr
    
    

    
    def sort_bubble(self, debug=False):
        arr_changed = True
        while arr_changed:
            arr_changed = False
            for i in range(len(self.arr) - 1):  # Can't finish on the last item
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    arr_changed = True
                    if debug:
                        print(f"Step: {self.arr}")
        return self.arr
    
    def sort_heapsort(self, debug=False):
        def restore_heap(arr, n, i):
            while True:
                maxVal = i  # take the largest as root
                left = 2 * i + 1  # formula to find the left child index
                right = 2 * i + 2  # formula to find the right child index

                if left < n and arr[maxVal] < arr[left]:  # left child exist and is largest than the root
                    maxVal = left  # Change value

                if right < n and arr[maxVal] < arr[right]:  # right child exist and is largest than the root
                    maxVal = right  # Change value

                if maxVal == i:  # Heap property is satisfied
                    break
                arr[i], arr[maxVal] = arr[maxVal], arr[i]
                i = maxVal

        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            restore_heap(self.arr, n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            restore_heap(self.arr, i, 0)
            if debug:
                print(f"Step: {self.arr}")
        return self.arr
    
    def sort_comb(self, debug=False):
        n = len(self.arr)
        gap = n
        shrink = 1.3
        sorted = False
        while not sorted:
            gap = int(gap /shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            for i in range (n - gap):
                if self.arr [i] > self.arr [i + gap]:
                    self.arr [i], self.arr [i + gap] = self.arr [i + gap], self.arr [i]
                    sorted = False
                    if debug:
                        print(f"Step: {self.arr}")
        return self.arr
    
    def sort_merge(self, debug=False):
        def _merge_sort(arr, debug=False):
            if len(arr) <= 1:
                return arr
            if debug and len(arr) == len(self.arr):  
                print(f"Merging: {deque(arr[:len(arr)//2])} and {deque(arr[len(arr)//2:])}")

            mid = len(arr) // 2
            left = _merge_sort(arr[:mid], debug)
            right = _merge_sort(arr[mid:], debug)
            return merge(left, right, debug)

        def merge(left, right, debug=False):
            result = []
            left = deque(left)
            right = deque(right)
            if debug:
                print(f"Merging: {left} and {right}")
            while left and right:
                if left[0] < right[0]:
                    result.append(left.popleft())
                else:
                    result.append(right.popleft())
            result.extend(left)
            result.extend(right)

            if debug:
                print(f"Result after merge: {result}")
            
            return result
        self.arr = _merge_sort(self.arr,debug)
        if debug:
                print(f"Step: {self.arr}")
        return self.arr