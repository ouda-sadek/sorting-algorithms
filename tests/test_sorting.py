import unittest
from sorting import SortNumbers

class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted = [5, 3, 8, 1, 9, 2]
        self.sorted_expected = sorted(self.unsorted)

    def test_sort_selection(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_selection(), self.sorted_expected)

    def test_sort_insertion(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_insertion(), self.sorted_expected)

    def test_sort_quick(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_quick(), self.sorted_expected)

    def test_sort_bubble(self):
        sorter = SortNumbers(self.unsorted.copy())
        print(self.unsorted)
        sorter.sort_bubble(debug=True)
        self.assertEqual(sorter.arr, self.sorted_expected)

    def test_sort_heapsort(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_heapsort(), self.sorted_expected)

    def test_sort_comb(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_comb(), self.sorted_expected)

    def test_sort_merge(self):
        sorter = SortNumbers(self.unsorted.copy())
        self.assertEqual(sorter.sort_merge(), self.sorted_expected)

if __name__ == "__main__":
    unittest.main()