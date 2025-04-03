import random
import time

class SortNumbers:
    def __init__(self, arr = None):
        if arr is None:
            arr = []
        self.arr = arr

    def display(self):
        print("Current list:", self.arr)

    def sort_selection(self):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
    
    def sort_insertion(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
    
    def sort_quick(self):
        def _sort_quick(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            moins = [x for x in arr[1:] if x <= pivot]
            plus = [x for x in arr[1:] if x > pivot]
            return _sort_quick(moins) + [pivot] + _sort_quick(plus)
        self.arr = _sort_quick(self.arr)
        return self.arr
    
    def measure_time(self,sort_method):
        start_time = time.time()
        self.arr = sort_method()
        end_time = time.time()
        return self.arr, end_time - start_time
    
    def generate_random_list(self, taille=500, min_val=0.0, max_val=500000.0):
        self.arr = [round(random.uniform(min_val, max_val),2) for _ in range(taille)]
        return self.arr
