import sys
import time

def main():
    input_array = parse_input_arguments()

    time1 = time.time()
    array_result, count = bubble_sort(input_array)
    print("\nSorted after", count * 2, "tries.")
    print("Sorted:", array_result)
    print("---")
    print("Overall Time:", time.time() - time1, "seconds")

def parse_input_arguments():
    input_array = []
    if len(sys.argv) < 2:
        print("Please input list items as arguments")
        print("\nExample: ./main.py <item1> [item2] [item3] [item4] ...")
        sys.exit(1)

    i = 1
    while i < len(sys.argv):
        input_array.append(int(sys.argv[i]))
        i += 1

    return input_array

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
        print("Sorting...", array)

        if not swapped:
            break

    return array, count

if __name__ == "__main__":
    main()