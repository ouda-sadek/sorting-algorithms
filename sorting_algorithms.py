from color_utils import ColorUtils

class SortingAlgorithms:
    # Different methods to sort by color
    
    def __init__(self):
        self.color_utils = ColorUtils()
    
    def selection_sort(self, data, min_val, max_val):
        # Find smallest item, swap to front
        data = list(data)
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.color_utils.value_to_hue(data[j], min_val, max_val) < self.color_utils.value_to_hue(data[min_index], min_val, max_val):
                    min_index = j
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
                yield data  # Show each step
        return data

    def insertion_sort(self, data, min_val, max_val):
        # Build sorted list one item at a time
        data = list(data)
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and self.color_utils.value_to_hue(data[j], min_val, max_val) > self.color_utils.value_to_hue(key, min_val, max_val):
                data[j + 1] = data[j]
                j -= 1
            if j + 1 != i:
                data[j + 1] = key
                yield data
        return data

    def bubble_sort(self, data, min_val, max_val):
        # Swap neighbors until sorted
        data = list(data)
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.color_utils.value_to_hue(data[j], min_val, max_val) > self.color_utils.value_to_hue(data[j + 1], min_val, max_val):
                    data[j], data[j + 1] = data[j + 1], data[j]
                    yield data
        return data

    def comb_sort(self, data, min_val, max_val):
        # Bubble sort with shrinking gaps
        data = list(data)
        n = len(data)
        gap = n
        shrink = 1.3
        sorted_array = False
        
        while not sorted_array:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_array = True
                
            for i in range(n - gap):
                if self.color_utils.value_to_hue(data[i], min_val, max_val) > self.color_utils.value_to_hue(data[i + gap], min_val, max_val):
                    data[i], data[i + gap] = data[i + gap], data[i]
                    sorted_array = False
                    yield data
        return data

    def heap_sort(self, data, min_val, max_val):
        # Sort using binary heap structure
        data = list(data)
        n = len(data)
        
        def restore_heap(arr, n, i):
            # Fix heap structure
            while True:
                maxVal = i
                left = 2 * i + 1
                right = 2 * i + 2
                
                if left < n and self.color_utils.value_to_hue(arr[maxVal], min_val, max_val) < self.color_utils.value_to_hue(arr[left], min_val, max_val):
                    maxVal = left
                    
                if right < n and self.color_utils.value_to_hue(arr[maxVal], min_val, max_val) < self.color_utils.value_to_hue(arr[right], min_val, max_val):
                    maxVal = right
                    
                if maxVal == i:
                    break
                    
                arr[i], arr[maxVal] = arr[maxVal], arr[i]
                i = maxVal
        
        # Build heap
        for i in range(n // 2 - 1, -1, -1):
            restore_heap(data, n, i)
        yield data
        
        # Extract from heap
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            restore_heap(data, i, 0)
            yield data
        return data

    def quick_sort(self, data, min_val, max_val):
        # Divide and conquer with pivot
        data = list(data)
        stack = [(0, len(data) - 1)]
        
        while stack:
            low, high = stack.pop()
            if low < high:
                pivot_idx = low
                pivot_hue = self.color_utils.value_to_hue(data[pivot_idx], min_val, max_val)
                i = low + 1
                j = high
                
                while True:
                    while i <= j and self.color_utils.value_to_hue(data[i], min_val, max_val) <= pivot_hue:
                        i += 1
                    while i <= j and self.color_utils.value_to_hue(data[j], min_val, max_val) > pivot_hue:
                        j -= 1
                    if i <= j:
                        data[i], data[j] = data[j], data[i]
                        yield data
                    else:
                        break
                
                data[low], data[j] = data[j], data[low]
                yield data
                stack.append((low, j - 1))
                stack.append((j + 1, high))
        return data

    def merge_sort(self, data, min_val, max_val):
        # Split, sort, and merge
        data = list(data)

        def sort(arr, left, right):
            # Recursive sort
            if right - left > 0:
                mid = (left + right) // 2
                yield from sort(arr, left, mid)
                yield from sort(arr, mid + 1, right)
                yield from merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            # Merge two sorted halves
            merged = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if self.color_utils.value_to_hue(arr[i], min_val, max_val) <= self.color_utils.value_to_hue(arr[j], min_val, max_val):
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1
            while i <= mid:
                merged.append(arr[i])
                i += 1
            while j <= right:
                merged.append(arr[j])
                j += 1
            for i, val in enumerate(merged):
                arr[left + i] = val
            yield arr.copy()

        yield from sort(data, 0, len(data) - 1)