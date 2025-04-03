from sorting import SortNumbers

def main():
    algo = SortNumbers()  

    algo.generate_random_list(taille=500, min_val=0.0, max_val=500000.0)

    print("Before sort: ")
    algo.display()  

    algorithms = [
        ("Sort selection", algo.sort_selection),
        ("Sort insertion", algo.sort_insertion),
        ("Sort quick", algo.sort_quick),
    ]

    print("\nMeasurement of execution times for each algorithm:")
    for name, algorithm in algorithms:
        lst_copy = algo.arr.copy()  
        algo.arr = lst_copy  
        lst_sorted, time_taken = algo.measure_time(algorithm)  
        print(f"{name}: {time_taken:.6f} seconds")  

if __name__ == "__main__":
    main()
