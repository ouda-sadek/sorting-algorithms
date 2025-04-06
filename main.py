from sorting import SortNumbers

def main():
    algo = SortNumbers()  

    algo.generate_random_list(taille=600, min_val=0.0, max_val=500000.0)

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
        # Créer une nouvelle copie de la liste avant chaque appel d'algorithme
        lst_copy = algo.arr.copy()  

        # Passer la copie à measure_time
        lst_sorted, time_taken = algo.measure_time(algorithm, lst_copy)  
        print(f"{name}: {time_taken:.6f} seconds")  

# print(f"Sorted list: {lst_sorted}")
    
        

if __name__ == "__main__":
    main()