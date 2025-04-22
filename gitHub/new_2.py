import timeit

arr = [2, 3, 4, 10, 40]
x = 40
iterator = 0

def binary_search(arr, low, high, x, iterator):

    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            iterator += 1
            return mid, iterator
 
        elif arr[mid] > x:
            iterator += 1
            return binary_search(arr, low, mid - 1, x, iterator)
        else:
            iterator += 1
            return binary_search(arr, mid + 1, high, x, iterator)
 
    else:
        return -1


def fun():
        return binary_search(arr, 0, len(arr)-1, x, iterator)

start = timeit.default_timer()
print(f"The start time is: {start}")
result = fun()
print(f"The difference of time is: {timeit.default_timer() - start}")
 
 
if  result != -1:
    print("Element is present at index", str(result[0]))
    print("Amount of iterations:", str(result[1]))
else:
    print("Element is not present in array")