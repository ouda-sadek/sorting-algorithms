from sorting import SortNumbers
from perf_measures import Performance

def main():
    algo = SortNumbers()  
    board = Performance()

    data= algo.generate_random_list(taille=2000, min_val=0.0, max_val=500000.0)

    print("Before sort: ")
    algo.display()  


    algorithms = [
        ("Sort Bubble", algo.sort_bubble),
        ("Sort selection", algo.sort_selection),
        ("Sort insertion", algo.sort_insertion),
        ("Sort Heap", algo.sort_heapsort),
        ("Sort quick", algo.sort_quick),

    ]

    print("\nMeasurement of execution times for each algorithm:")
    for name, algorithm in algorithms:
       
        sorted_data = board.measure_performance(algorithm, data, name)
       
    
    board.display_tests()
# print(f"Sorted list: {lst_sorted}"    
        

if __name__ == "__main__":
    main()