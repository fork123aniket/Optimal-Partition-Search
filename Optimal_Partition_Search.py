import timeit

def optimal_partition_search(a, item):
    if item not in a:
        raise ValueError("The element you want to search is not available in the given array. "
                         "Please select an element among the available elements of the array.")
    a = sorted(a)
    found = False
    high = len(a) - 1
    low = mini = optimal = 0
    for partition in range(2, len(a) + 1):
        start_time = timeit.default_timer()
        while low <= high and not found:
            i, middle = 0, []
            while low <= high and i < partition - 1:
                mid = low + int((high - low) / partition)
                low = mid + 1
                i += 1
                middle.append(mid)
            for key in range(len(middle)):
                if item == a[middle[key]]:
                    found = True
                    break
                elif item < a[middle[key]]:
                    low = 0
                    high = middle[key] - 1
                    break
                elif item > a[middle[key]] and key < len(middle) - 1:
                    if item < a[middle[key + 1]]:
                        low = middle[key] + 1
                        high = middle[key + 1] - 1
                        break
                elif item > a[middle[key]] and key == len(middle) - 1:
                    if item < a[high]:
                        low = middle[key] + 1
                        high = high
                        break
            del middle
        end_time = timeit.default_timer()
        x = end_time - start_time
        if partition == 2 or x < mini:
            mini = x
            optimal = partition
    return optimal
