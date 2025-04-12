import random
import colorsys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Generate random data
def generate_data(num_elements=50, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(num_elements)]

# Convert a value to a color (using viridis colormap)
def value_to_color(val, min_val, max_val):
    if max_val == min_val:
        return plt.cm.viridis(0.5)  # Avoid division by zero
    normalized = (val - min_val) / (max_val - min_val)
    return plt.cm.viridis(normalized)

# Convert a value to an HSV hue for color-based sorting
def value_to_hue(val, min_val, max_val):
    if max_val == min_val:
        return 0.0  # Default hue if all values are identical
    normalized = (val - min_val) / (max_val - min_val)
    r, g, b, _ = plt.cm.viridis(normalized)
    h, _, _ = colorsys.rgb_to_hsv(r, g, b)
    return h

# Visualization using color-based sorting
def visualize_sorting(data, sorting_func, algo_name=""):
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': 'polar'})
    ax.set_title(f"Tri par couleur : {algo_name}", pad=20, fontsize=14)
    ax.set_xticks([])
    ax.set_yticks([])
    
    min_val, max_val = min(data), max(data)
    theta = np.linspace(0, 2 * np.pi, len(data), endpoint=False)
    bars = ax.bar(theta, np.ones(len(data)), width=2 * np.pi / len(data),
                  color=[value_to_color(val, min_val, max_val) for val in data])

    def update_fig(data, bars):
        for bar, val in zip(bars, data):
            bar.set_color(value_to_color(val, min_val, max_val))
        return bars

    anim = animation.FuncAnimation(
        fig, update_fig, frames=sorting_func(data, min_val, max_val),
        fargs=(bars,), interval=50, repeat=False, blit=False
    )
    plt.show()

# MODIFIED sorting algorithms to sort by hue
def selection_sort(data, min_val, max_val):
    data = list(data)
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if value_to_hue(data[j], min_val, max_val) < value_to_hue(data[min_index], min_val, max_val):
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            yield data
    return data

def insertion_sort(data, min_val, max_val):
    data = list(data)
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and value_to_hue(data[j], min_val, max_val) > value_to_hue(key, min_val, max_val):
            data[j + 1] = data[j]
            j -= 1
        if j + 1 != i:
            data[j + 1] = key
            yield data
    return data

def heap_sort(data, min_val, max_val):
    data = list(data)
    n = len(data)
    
    def restore_heap(arr, n, i):
        while True:
            maxVal = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and value_to_hue(arr[maxVal], min_val, max_val) < value_to_hue(arr[left], min_val, max_val):
                maxVal = left
                
            if right < n and value_to_hue(arr[maxVal], min_val, max_val) < value_to_hue(arr[right], min_val, max_val):
                maxVal = right
                
            if maxVal == i:
                break
                
            arr[i], arr[maxVal] = arr[maxVal], arr[i]
            i = maxVal
    
    for i in range(n // 2 - 1, -1, -1):
        restore_heap(data, n, i)
    yield data
    
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        restore_heap(data, i, 0)
        yield data
    return data

def quick_sort(data, min_val, max_val):
    data = list(data)
    stack = [(0, len(data) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_idx = low
            pivot_hue = value_to_hue(data[pivot_idx], min_val, max_val)
            i = low + 1
            j = high
            
            while True:
                while i <= j and value_to_hue(data[i], min_val, max_val) <= pivot_hue:
                    i += 1
                while i <= j and value_to_hue(data[j], min_val, max_val) > pivot_hue:
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

def bubble_sort(data, min_val, max_val):
    data = list(data)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if value_to_hue(data[j], min_val, max_val) > value_to_hue(data[j + 1], min_val, max_val):
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data
    return data

def comb_sort(data, min_val, max_val):
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
            if value_to_hue(data[i], min_val, max_val) > value_to_hue(data[i + gap], min_val, max_val):
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted_array = False
                yield data
    return data

def merge_sort(data, min_val, max_val):
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
            if value_to_hue(arr[i], min_val, max_val) <= value_to_hue(arr[j], min_val, max_val):
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

# Interactive menu
def menu():
    algos = {
        '1': ('Tri par sélection (couleur)', selection_sort),
        '2': ('Tri par insertion (couleur)', insertion_sort),
        '3': ('Tri à bulles (couleur)', bubble_sort),
        '4': ('Tri peigne (couleur)', comb_sort),
        '5': ('Tri par tas (couleur)', heap_sort),
        '6': ('Tri rapide (couleur)', quick_sort),
        '7': ('Tri fusion (couleur)', merge_sort)
    }
    
    print("=== Tri par couleur ===")
    for key, (name, _) in algos.items():
        print(f"{key}. {name}")
    
    choice = input("Choix : ").strip()
    if choice in algos:
        algo_name, algo_func = algos[choice]
        data = generate_data()
        visualize_sorting(data, algo_func, algo_name)
    else:
        print("Choix invalide.")
        menu()

# Launch the menu
menu()