array1 = ['a', 'b', 'c', 'd', 'a', 'b', 'f', 's', 'r']
array2 = ['a', 'b', 'c']


def intersection(arr1, arr2):
    x = list(dict.fromkeys(sorted(arr1)))
    y = list(dict.fromkeys(sorted(arr2)))
    arr3 = [value for value in x if value in y]
    return arr3


def union(arr1, arr2):
    return set.union(set(arr1), set(arr2))


print(union(['a', 'b', 'c', 'd', 'a', 'b', 'f', 's', 'r'], ['a', 'b', 'c']))
