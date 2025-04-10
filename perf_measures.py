import time
import psutil
import tracemalloc
from sorting import SortNumbers
import json

class Performance: 
    def __init__(self):
        self.results = []
    
    def measure_performance(self, algo_func, data, algo_name):
        tracemalloc.start() # Start the RAM test

        cpu_before = psutil.cpu_percent(interval=None) # Give the actual CPU used and an instant measure

        # Dictionary for complexity estimates
        complexity_estimates = {
            'Sort bubble': 'O(n^2)',
            'Sort selection': 'O(n^2)',
            'Sort insertion': 'O(n^2)',
            'Sort heap': 'O(n log n)',
            'Sort quick': 'O(n log n)',
            'Sort comb': 'O(n^2)',
            'Sort merge': 'O(n log n)',
        }

        try:
            # Time measure
            start_time = time.time() # record time now
            #sorted_data = algo_func(data.copy()) #sorting running with a simple copy
            # Sort without parameters because self.arr already defined
            sorted_data = algo_func()
            end_time = time.time() # time at the end

            # Calculators
            time_taken = end_time - start_time #time calculator
            cpu_used = max(0, psutil.cpu_percent(interval=None) -cpu_before)# CPU calculator
            memory_used = tracemalloc.get_traced_memory()[1] / (1024 * 1024)# RAM : Calculate the peak with [1] and translate in Mo with (1024*1024) 

            tracemalloc.stop()

            self.results.append(
            {
                'algorithm' : algo_name,
                'time' : time_taken,
                'cpu' : cpu_used,
                'memory' : memory_used,
                'complexity': complexity_estimates.get(algo_name, 'Unknown'),
            } )
        except Exception as e:
            print(f"An error occurred during the execution of {algo_name}: {e}")
            # Return original data on error
            sorted_data = data  


        return sorted_data
    
    def display_tests(self):

        #Board Design
        print("\nPerformance Results:")
        print("{:<20} {:<15} {:<15} {:<15} {:<20}".format(
            'Algorithm', 'Time (s)', 'CPU (%)', 'Memory (MB)', 'Complexity'))
        print("-" * 85)

        for result in self.results:
            print("{:<20} {:<15.6f} {:<15.2f} {:<15.2f} {:<20}".format(
                result['algorithm'],
                result['time'],
                result['cpu'],
                result['memory'],
                result['complexity']))
        
        print("\n")

    def export_to_json(self, filename='performance_results.json'):
        # Export the performance results to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(self.results, json_file, indent=4)

        print(f"Results have been exported to {filename}")

    def reset(self):
        self.results.clear()