# Bubble Sort with Python

This is a Python script that demonstrates the Bubble Sort algorithm, a simple comparison-based sorting algorithm. The script accepts a list of integers as command-line arguments, sorts the list using the Bubble Sort algorithm, and then prints the sorted list along with the number of iterations it took to sort the list. The script also measures and displays the overall execution time.

## Usage

To use this script, follow these steps:

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script with the following command:
   ```bash
   python main.py <item1> [item2] [item3] [item4] ...
   ```
Replace `<item1>, [item2], [item3], and [item4]` with the integer values you want to sort. You can provide as many integers as you like.

## Example

Here's an example of how to use the script:

```bash
python main.py 7 2 5 1 8
```
This command will sort the list [7, 2, 5, 1, 8] using the Bubble Sort algorithm and display the sorted list and the number of iterations required to sort it.

## Bubble Sort Algorithm

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. In each pass, the largest unsorted element "bubbles up" to its correct position.

## Output
After sorting the list, the script will display the following information:

- The sorted list.
- The number of iterations it took to sort the list.
- The overall execution time in seconds.
