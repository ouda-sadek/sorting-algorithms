import random
import time

class SortNumbers:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.arr = arr

    def display(self):
        print("Current list:", self.arr)

    def sort_selection(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    def sort_insertion(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def sort_quick(self, arr):
        def _sort_quick(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            moins = [x for x in arr[1:] if x <= pivot]
            plus = [x for x in arr[1:] if x > pivot]
            return _sort_quick(moins) + [pivot] + _sort_quick(plus)
        return _sort_quick(arr)
    
    def sort_bubble(self, arr):
        arr_changed = True
        while arr_changed:
            arr_changed = False
            for i in range(len(arr) - 1):  # Can't finish on the last item
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    arr_changed = True
        return arr
    
    def sort_heapsort(self, arr):
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

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            restore_heap(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            restore_heap(arr, i, 0)

        return arr

    def measure_time(self, sort_method, arr):
        start_time = time.time()
        arr = sort_method(arr)  # Pass the array to the sorting method
        end_time = time.time()
        return arr, end_time - start_time
    
    def generate_random_list(self, taille=500, min_val=0.0, max_val=500000.0):
        self.arr = [round(random.uniform(min_val, max_val), 2) for _ in range(taille)]
        return self.arr
    
    def sort_comb(self):
        n = len(self.arr)
        gap = n
        shrink = 1.3
        sorted = False
        while not sorted:
            gap = int(gap /shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            for i in range (n -gap):
                if self.arr [i] > self.arr [i + gap]:
                    self.arr [i], self.arr [i + gap] = self.arr [i + gap], self.arr [i]
                    sorted = False
        return self.arr
    
    def sort_merge(self):
        if len (self.arr) <= 1:
            return self.arr
        mid = len (self.arr) // 2
        left = SortNumbers(self.arr[:mid]).sort_merge()
        right = SortNumbers(self.arr[mid:]).sort_merge()
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        while left and right:
            if left [0] < right [0]:
                result.append (left.pop(0))
            else:
                result.append(right.pop(0))

        result.extend(left or right)
        return result
