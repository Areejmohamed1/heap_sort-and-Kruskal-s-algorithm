def heap_sort(input_list, field):
    """
    Heap sort implementation for a list of objects or dictionaries.
    Sorts the list in-place based on a specified field or attribute.

    Parameters:
        input_list (list): The list to be sorted.
        field (str): The key or attribute to sort by.

    Returns:
        list: The sorted list.
    """
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and get_value(input_list[child]) < get_value(input_list[child + 1]):
                child += 1
            if get_value(input_list[root]) < get_value(input_list[child]):
                input_list[root], input_list[child] = input_list[child], input_list[root]
                root = child
            else:
                break

    def get_value(item):
        # Handles both dictionary keys and object attributes
        return item[field] if isinstance(item, dict) else getattr(item, field)

    # Build the max heap
    n = len(input_list)
    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    # Extract elements from the heap
    for end in range(n - 1, 0, -1):
        input_list[0], input_list[end] = input_list[end], input_list[0]
        sift_down(0, end - 1)

    return input_list
