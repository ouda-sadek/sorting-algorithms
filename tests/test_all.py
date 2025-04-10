import unittest
from sorting import SortNumbers
from perf_measures import Performance

class TestSortingPerformance(unittest.TestCase):

    def setUp(self):
        # Creates an object for sorting algorithms
        self.algo = SortNumbers() 
        # Creates an object to measure performance 
        self.board = Performance()  

    def test_performance_all_algorithms(self):
        # Tests the performance of all sorting algorithms
        algorithms = [
            ("Sort Bubble", self.algo.sort_bubble),
            ("Sort selection", self.algo.sort_selection),
            ("Sort insertion", self.algo.sort_insertion),
            ("Sort Heap", self.algo.sort_heapsort),
            ("Sort quick", self.algo.sort_quick),
            ("Sort comb", self.algo.sort_comb),
            ("Sort merge", self.algo.sort_merge),
        ]
        
        # List to store results
        results = []

        for name, algorithm in algorithms:
            # Generates a new list at each iteration
            self.algo.generate_random_list(taille=500, min_val=0.0, max_val=500000.0)
            print(f"\nTesting {name}...")
            
            # Measure the performance of the algorithm
            sorted_data = self.board.measure_performance(algorithm, self.algo.arr, name)

            # Save results to view later
            results.append({
                "algorithm": name,
                "sorted_data": sorted_data
            })

        # Displays the results in summary at the end of the test in terminal
        self.board.display_tests() 

        # To ensure that all tests pass, we can add a check for the sorting test
        for result in results:
            with self.subTest(result=result["algorithm"]):
                # We check that the list is sorted correctly
                self.assertEqual(result["sorted_data"], sorted(result["sorted_data"]))


if __name__ == "__main__":
    unittest.main()
