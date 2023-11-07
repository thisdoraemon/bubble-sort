import unittest

def bubble_sort(array):
    length = len(array)
    count = 0

    while True:
        swapped = False
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                count += 1

        if not swapped:
            break

    return array, count

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        # Test with an unsorted list
        input_array = [5, 4, 3, 1, 7]
        sorted_array, count = bubble_sort(input_array)
        self.assertEqual(sorted_array, [1, 3, 4, 5, 7])
        self.assertEqual(count, 6)

        # Test with an already sorted list
        input_array = [1, 2, 3, 4, 5]
        sorted_array, count = bubble_sort(input_array)
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(count, 0)

if __name__ == "__main__":
    unittest.main()