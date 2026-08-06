def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            # Partition the array around a pivot element
            pivot_index = partition(items, low, high)
            
            # Recursively sort elements before and after partition
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[high]  # Choose the last element as pivot
        i = low - 1          # Index of smaller element

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]

        # Swap the pivot element with the element at i + 1
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr

# Example usage:
if __name__ == "__main__":
    sample_list = [10, 7, 8, 9, 1, 5]
    sorted_list = quick_sort(sample_list)
    print("Sorted array:", sorted_list)
