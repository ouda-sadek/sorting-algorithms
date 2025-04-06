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
    
    def sort_bubble(self):
        arr_changed = True
        while arr_changed:
            arr_changed = False
            for i in range(len(self.arr)-1): # Can't finish on the last item
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    arr_changed = True
        return self.arr
    
    def sort_heapsort(self):
        n = len(self.arr)

        def restore_heap(arr, n, i):
            while True:
                maxVal = i # take the largest as root
                left = 2 *i + 1 # formula to find the left child index
                right = 2 * i + 2 # formula to find the right child index

                if left < n and arr[maxVal] < arr[left]: # left child exist and is largest than the root
                    maxVal = left # Change value

                if right < n and arr[maxVal] < arr[right]: # right child exist and is largest than the root
                    maxVal = right# Change value
            
                # if largest isn't the root, change values and continue
                if maxVal == i :
                    break
                
                arr[i], arr[maxVal] = arr[maxVal], arr[i]
                i = maxVal
        
        for i in range(n // 2 - 1, -1, -1):
            restore_heap(self.arr, n, i)
        
        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            restore_heap(self.arr, i, 0)
        return self.arr

    

        



    
    def measure_time(self,sort_method):
        start_time = time.time()
        self.arr = sort_method()
        end_time = time.time()
        return self.arr, end_time - start_time
    
    def generate_random_list(self, taille=500, min_val=0.0, max_val=500000.0):
        self.arr = [round(random.uniform(min_val, max_val),2) for _ in range(taille)]
        return self.arr
