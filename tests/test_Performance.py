import unittest
from sorting import SortNumbers
from perf_measures import Performance

class TestSortingPerformance(unittest.TestCase):

    def test_large_list(self):
        """Test performance on a very large list"""
        algo = SortNumbers()
        large_list = algo.generate_random_list(taille=100000)  
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_quick, large_list, "Sort Quick")
        
        # Test example: check if the sorted list has the correct length
        self.assertEqual(len(sorted_data), 100000)

    def test_sorted_list(self):
        """Test performance on an already sorted list"""
        algo = SortNumbers()
        sorted_list = list(range(10000))  
        algo.arr = sorted_list
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_bubble, sorted_list, "Sort Bubble")
        
        # Check that the list remains sorted
        self.assertEqual(sorted_data, sorted_list)

    def test_reverse_sorted_list(self):
        """Test performance on a list that is reverse sorted"""
        algo = SortNumbers()
        reverse_sorted_list = list(range(10000, 0, -1)) 
        algo.arr = reverse_sorted_list
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_insertion, reverse_sorted_list, "Sort Insertion")
        
        # Check if the sorting is correct
        self.assertEqual(sorted_data, list(range(1, 10001)))

    def test_small_list(self):
        test_data = [1, 2, 7]
        algo = SortNumbers(test_data)
        sorted_data = algo.sort_insertion()  
        print(sorted_data) 
        self.assertEqual(sorted_data, [1, 2, 7])
       
    def test_list_with_duplicates(self):
        # List with duplicates
        test_data = [5, 3, 8, 5, 9, 2, 3, 7, 2]
        algo = SortNumbers(test_data)
        print("\nTesting on list with duplicates:")
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_quick, test_data, "Sort quick")
        print(sorted_data)
        self.assertEqual(sorted_data, sorted(test_data))

    def test_empty_list(self):
        # Empty list
        test_data = []
        algo = SortNumbers(test_data)
        print("\nTesting on empty list:")
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_quick, test_data, "Sort quick")
        print(sorted_data)
        self.assertEqual(sorted_data, test_data)

    def test_non_numeric_data(self):
        # List with strings
        test_data = ["apple", "orange", "banana", "pear"]
        algo = SortNumbers(test_data)
        print("\nTesting on non-numeric data (strings):")
        performance = Performance()
        sorted_data = performance.measure_performance(algo.sort_quick, test_data, "Sort quick")
        self.assertEqual(sorted_data, sorted(test_data))

        
if __name__ == '__main__':
    unittest.main()
