from sorting import SortNumbers
from perf_measures import Performance

def main():
    # Initialization
    algo = SortNumbers()  
    board = Performance()

    # Generate the starting list
    #data= algo.generate_random_list(taille=2000, min_val=0.0, max_val=500000.0)
    original_data= algo.generate_random_list(taille=500, min_val=0.0, max_val=500000.0)
    
    #print("Before sort: ")
    print("First 20 elements (unsorted):")
    print(original_data[:20], "...")
    

    # User choice
    #print ("Choose a sorting algorithm:")
    algorithms = {
        1: ("Sort selection", algo.sort_selection),
        2: ("Sort insertion", algo.sort_insertion),
        3: ("Sort quick",     algo.sort_quick),
        4: ("Sort bubble",    algo.sort_bubble),
        5: ("Sort heap",      algo.sort_heapsort),
        6: ("Sort comb",      algo.sort_comb),
        7: ("Sort merge",     algo.sort_merge)
    }
    print("\nChoose a sorting algorithm:")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")
    
    try:
        choice = int (input("Enter the algorithm number : "))
        if choice in algorithms:
            name, method = algorithms[choice]
            algo.arr = original_data.copy()
            print(f"\nRunning {name}...")
            sorted_list = method()
            print(f"\n {name} result (first 20 values):", sorted_list[:20], "...")
        else:
            print("Invalid choice!")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Performance measurement for all algorithms
    print("\nMeasuring execution time and memory for each algorithm:\n")
    for name, method in algorithms.values():
       algo.arr = original_data.copy()  
       board.measure_performance(method, original_data.copy(), name)
        
    # Displaying the final table
    board.display_tests()
    board.export_to_json()
  
if __name__ == "__main__":
    main()