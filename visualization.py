# visualization.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from data_generator import DataGenerator
from color_utils import ColorUtils
from sorting_algorithms import SortingAlgorithms

class Visualization:
    # Shows sorting animations using polar plots
    
    def __init__(self):
        # Set up needed tools
        self.data_generator = DataGenerator()
        self.color_utils = ColorUtils()
        self.sorting_algorithms = SortingAlgorithms()
    
    def visualize_sorting(self, data, sorting_func, algo_name=""):
        # Draw and animate the sorting process
        fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': 'polar'})
        ax.set_title(f"Color Sorting: {algo_name}", pad=20, fontsize=14)
        ax.set_xticks([])  # No radial numbers
        ax.set_yticks([])  # No angle numbers
        
        min_val, max_val = min(data), max(data)
        theta = np.linspace(0, 2 * np.pi, len(data), endpoint=False)
        # Make colored bars in circle
        bars = ax.bar(theta, np.ones(len(data)), width=2 * np.pi / len(data),
                      color=[self.color_utils.value_to_color(val, min_val, max_val) for val in data])
    
        def update_fig(data, bars):
            # Change colors during animation
            for bar, val in zip(bars, data):
                bar.set_color(self.color_utils.value_to_color(val, min_val, max_val))
            return bars
    
        # Animate using sorting steps
        anim = animation.FuncAnimation(
            fig, update_fig, frames=sorting_func(data, min_val, max_val),
            fargs=(bars,), interval=50, repeat=False, blit=False
        )
        plt.show()

    def menu(self):
        # Let user pick sorting method
        algos = {
            '1': ('Selection Sort', self.sorting_algorithms.selection_sort),
            '2': ('Insertion Sort', self.sorting_algorithms.insertion_sort),
            '3': ('Bubble Sort', self.sorting_algorithms.bubble_sort),
            '4': ('Comb Sort', self.sorting_algorithms.comb_sort),
            '5': ('Heap Sort', self.sorting_algorithms.heap_sort),
            '6': ('Quick Sort', self.sorting_algorithms.quick_sort),
            '7': ('Merge Sort', self.sorting_algorithms.merge_sort)
        }
        
        print("=== Color Sorting ===")
        for key, (name, _) in algos.items():
            print(f"{key}. {name}")
        
        choice = input("Choice: ").strip()
        if choice in algos:
            algo_name, algo_func = algos[choice]
            data = self.data_generator.generate_data()
            self.visualize_sorting(data, algo_func, algo_name)
        else:
            print("Invalid choice.")
            self.menu()

if __name__ == "__main__":
    visualizer = Visualization()
    visualizer.menu()