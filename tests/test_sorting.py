import unittest
from sorting import SortNumbers

class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted = [5, 3, 8, 1, 9, 2]
        self.sorted_expected = sorted(self.unsorted)

    def test_sort_selection(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort selection:", self.unsorted)
        sorter.sort_selection(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_insertion(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort insertion:",self.unsorted)
        sorter.sort_insertion(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_quick(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort quick:",self.unsorted)
        sorter.sort_quick(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_bubble(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort bubble:",self.unsorted)
        sorter.sort_bubble(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_heapsort(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort heapsort:",self.unsorted)
        sorter.sort_heapsort(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_comb(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort comb:",self.unsorted)
        sorter.sort_comb(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_merge(self):
        sorter = SortNumbers(self.unsorted.copy())
        print("\nTest sort merge:",self.unsorted)
        sorter.sort_merge(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

if __name__ == "__main__":
    unittest.main()