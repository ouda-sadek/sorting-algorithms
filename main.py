from sorting import SortNumbers

def main():
    algo = SortNumbers()  

    algo.generate_random_list(taille=500, min_val=0.0, max_val=500000.0)

    print("Before sort: ")
    algo.display()  

    print ("Choose a sorting algorithm:")
    print ("1. Sort selection")
    print ("2. Sort insertion")
    print ("3. Sort quick")
    print ("4. bubble sort")
    print ("5. Sort by heap")
    print ("6. Sort comb")
    print ("7. Sort merge")

    choice = int (input("Enter the algorithm number : "))
    
    if choice == 1:
        sorted_list = algo.sort_selection()
    elif choice == 2:
        sorted_list = algo.sort_insertion()
    elif choice == 3:
        sorted_list = algo.sort_quick()
    elif choice == 4:
        sorted_list = algo.bubble_sort()
    elif choice == 5:
        sorted_list = algo.sort_by_heap()
    elif choice == 6:
        sorted_list = algo.sort_comb()
    elif choice == 7:
        sorted_list = algo.sort_merge()
    else:
        print("Invalid choice!")
        return
    
    print ("Sorted list:", sorted_list)
  
    algorithms = [
        ("Sort selection", algo.sort_selection),
        ("Sort insertion", algo.sort_insertion),
        ("Sort quick", algo.sort_quick),
        ("Sort comb", algo.sort_comb),
        ("Sort merge", algo.sort_merge),
    ]

    print("\nMeasurement of execution times for each algorithm:")
    for name, algorithm in algorithms:
        lst_copy = algo.arr.copy()  
        algo.arr = lst_copy  
        list_sorted, time_taken = algo.measure_time(algorithm)  
        print(f"{name}: {time_taken:.6f} seconds") 

if __name__ == "__main__":
    main()
