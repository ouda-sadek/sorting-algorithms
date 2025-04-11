import unittest
from sorting import SortNumbers
from perf_measures import Performance

class TestSortingPerformance(unittest.TestCase):

    def setUp(self):
        """Initialize the objects needed for testing"""
        self.algo = SortNumbers() 
        self.performance = Performance()  

    def test_large_list(self):
        """Test performance on a very large list"""
        large_list = self.algo.generate_random_list(taille=100000)  
        sorted_data = self.performance.measure_performance(self.algo.sort_quick, large_list, "Sort Quick")
        
        # Test example: check if the sorted list has the correct length
        self.assertEqual(len(sorted_data), 100000)

    def test_sorted_list(self):
        """Test performance on an already sorted list"""
        sorted_list = list(range(10000))  
        sorted_data = self.performance.measure_performance(self.algo.sort_bubble, sorted_list, "Sort Bubble")
        
        # Check that the list remains sorted
        self.assertEqual(sorted_data, sorted_list)

    def test_reverse_sorted_list(self):
        """Test performance on a list that is reverse sorted"""
        reverse_sorted_list = list(range(10000, 0, -1)) 
        sorted_data = self.performance.measure_performance(self.algo.sort_insertion, reverse_sorted_list, "Sort Insertion")
        
        # Check if the sorting is correct
        self.assertEqual(sorted_data, list(range(1, 10001)))

    def test_small_list(self):
        test_data = [1, 2, 7]
        sorted_data = self.algo.sort_insertion(test_data)  
        print(sorted_data) 
        self.assertEqual(sorted_data, [1, 2, 7])
       
    def test_list_with_duplicates(self):
        # List with duplicates
        test_data = [5, 3, 8, 5, 9, 2, 3, 7, 2]
        print("\nTesting on list with duplicates:")
        sorted_data = self.performance.measure_performance(self.algo.sort_quick, test_data, "Sort quick")
        print(sorted_data)
        self.assertEqual(sorted_data, sorted(test_data))

    def test_empty_list(self):
        # Empty list
        test_data = []
        print("\nTesting on empty list:")
        sorted_data = self.performance.measure_performance(self.algo.sort_quick, test_data, "Sort quick")
        print(sorted_data)
        self.assertEqual(sorted_data, test_data)

    def test_non_numeric_data(self):
        # List with strings
        test_data = ["apple", "orange", "banana", "pear"]
        print("\nTesting on non-numeric data (strings):")
        sorted_data = self.performance.measure_performance(self.algo.sort_quick, test_data, "Sort quick")
        self.assertEqual(sorted_data, sorted(test_data))

    def test_invalid_input(self):
        """Test performance on invalid input """
        with self.assertRaises(TypeError):
            test_data = [1, 2, "banana", 4]
            self.algo.sort_quick(test_data)

    def tearDown(self):
        """Optionally clean up after each test"""
        pass  # Nothing to clean in this case

        
if __name__ == '__main__':
    unittest.main()
