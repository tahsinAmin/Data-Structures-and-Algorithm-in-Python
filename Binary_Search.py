def binary_search(data, target, low, high):
    """Return True if target is found in indecated portion of a Python list.

    The search only considers the protion from data[low] to data[high] inclusive.
    """

    if low > high:
        return False  # Interval is empty
    else:
        mid = (low+high) // 2
        if target == data[mid]:
            # print(mid)
            return True
        elif target < data[mid]:
            # recur on the potion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the iddle
            return binary_search(data, target, mid+1, high)


a = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
print(binary_search(a, 22, 0, 15))
