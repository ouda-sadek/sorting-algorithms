import random
import colorsys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Generate a list of unsorted random values
def generate_data(num_elements=100, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(num_elements)]

def value_to_color (data, min_val, max_val):
    normalized = (data- min_val) / (max_val - min_val)
    return plt.cm.viridis(normalized)  

def visualize_sorting(data, sorting_func, algo_name="" ):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.set_title(f"Tri visuel : {algo_name}", fontsize=16)
    ax.axis('off') 

   
    theta = np.linspace(0, 2 * np.pi, len(data), endpoint=False)
    radii = np.ones(len(data))  
    width = 2 * np.pi / len(data)  
 

    bars = ax.bar(theta, radii, width=width, bottom=0.0,
                  color=[value_to_color(val, min(data), max(data)) for val in data])

 
    def update_fig(data, bars):
        for bar, val in zip(bars, data):
            bar.set_color(value_to_color(val, min(data), max(data)))


    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        frames=sorting_func(data),
        fargs=(bars,),
        interval=1,  
        repeat=False
    )

    plt.show()


data = np.random.randint(1, 100, 50)


def selection_sort(data):
    data = list(data)
    n = len(data)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            yield data
    
    return data

def insertion_sort(data):
    data = list(data)
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        if j + 1 != i:  # Only yield if we actually moved an element
            data[j + 1] = key
            yield data
        
    return data

def heap_sort(data):
    # Convert input to list to ensure we're working with a mutable object
    data = list(data)
    n = len(data)
    
    # Function to restore heap property
    def restore_heap(arr, n, i):
        while True:
            maxVal = i  # take the largest as root
            left = 2 * i + 1  # formula to find the left child index
            right = 2 * i + 2  # formula to find the right child index
            
            if left < n and arr[maxVal] < arr[left]:  # left child exists and is larger than the root
                maxVal = left  # Change value
                
            if right < n and arr[maxVal] < arr[right]:  # right child exists and is larger than the root
                maxVal = right  # Change value
                
            if maxVal == i:  # Heap property is satisfied
                break
                
            arr[i], arr[maxVal] = arr[maxVal], arr[i]
            i = maxVal
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        restore_heap(data, n, i)
    yield data  # Yield after building the initial heap
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Move current root to end
        restore_heap(data, i, 0)  # Restore heap property for reduced heap
        yield data  # Yield after each step
    return data

def quick_sort(data):
    data = list(data)
    n = len(data)
    
    if n <= 1:
        return data
    
    # We'll use a stack to simulate recursion
    stack = [(0, n-1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            # Choose pivot (using the first element as in your original)
            pivot_idx = low
            pivot = data[pivot_idx]
            
            # Partition
            i = low + 1
            j = high
            
            while True:
                # Find element greater than pivot
                while i <= j and data[i] <= pivot:
                    i += 1
                
                # Find element smaller than pivot
                while i <= j and data[j] > pivot:
                    j -= 1
                
                if i <= j:
                    # Swap elements
                    data[i], data[j] = data[j], data[i]
                    yield data
                else:
                    break
            
            # Swap pivot to its final position
            data[low], data[j] = data[j], data[low]
            yield data
            
            # Add sub-arrays to stack
            if low < j-1:
                stack.append((low, j-1))
            if j+1 < high:
                stack.append((j+1, high))
    
    return data

def bubble_sort(data):
    n = len(data)
    data = list(data)  
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data


def comb_sort(data):
    data = list(data)
    n = len(data)
    gap = n
    shrink = 1.3
    sorted_array = False
    
    while not sorted_array:
        # Update the gap
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_array = True  # Will be set to False if any swap occurs
        
        # Compare elements with current gap
        for i in range(n - gap):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted_array = False
                yield data  # Yield after each swap
    
    return data


def merge_sort(data):
    data = list(data)

    def sort(arr, left, right):
        if right - left > 0:
            mid = (left + right) // 2
            yield from sort(arr, left, mid)
            yield from sort(arr, mid + 1, right)
            yield from merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        merged = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
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


# MENU
def menu():
    algos = {
        '1': ('Selection Sort', selection_sort),
        '2': ('Insertion Sort', insertion_sort),
        '3': ('Bubble Sort', bubble_sort),
        '4': ('Comb Sort', comb_sort),
        '5': ('Heap Sort', heap_sort),
        '6': ('Quick Sort', quick_sort),
        '7': ('Merge Sort', merge_sort),
    }

    print("=== Choisissez un algorithme de tri à visualiser ===")
    for key, (name, _) in algos.items():
        print(f"{key}. {name}")
    
    choice = input("Entrez le numéro de l'algorithme : ").strip()
    
    if choice in algos:
        algo_name, algo_func = algos[choice]
        print(f"Lancement de : {algo_name}")
        data = generate_data()
        visualize_sorting(data, algo_func, algo_name)
    else:
        print("Choix invalide. Veuillez réessayer.")
        menu()

# Visualisation
menu()
 
