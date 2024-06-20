import re
import numpy as np

def interpolate_missing(numb):
    interpolated = []
    for i, num in enumerate(numb):
        if num is None:
            leftind = i - 1
            rightind = i + 1
            leftval = None
            rightval = None
            while leftind >= 0:
                if numb[leftind] is not None:
                    leftval = numb[leftind]
                    break
                leftind -= 1
            while rightind < len(numb):
                if numb[rightind] is not None:
                    rightval = numb[rightind]
                    break
                rightind += 1
        
            if leftval is not None and rightval is not None:
                distance = rightind - leftind
                interpolatedval = leftval + ((rightval - leftval) / distance) * (i - leftind)
                interpolated.append(round(interpolatedval))
            elif leftval is not None:
                interpolated.append(leftval)
            elif rightval is not None:
                interpolated.append(rightval)
            else:
                interpolated.append(None)
        else:
            interpolated.append(num)
    return interpolated

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_batches(lst, batch_size):
    return [max(lst[i:i+batch_size]) for i in range(0, len(lst), batch_size)]

def encode_string(s):
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded

def decode_string(s):
    decoded = ""
    i = 0
    while i < len(s):
        count = int(s[i])
        decoded += s[i + 1] * count
        i += 2
    return decoded

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def regex_search(strings, pattern):
    return [s for s in strings if re.search(pattern, s)]

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def group_by_key(data, key):
    grouped = {}
    for item in data:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped

def remove_outliers(lst):
    mean = np.mean(lst)
    std_dev = np.std(lst)
    return [x for x in lst if abs(x - mean) <= 2 * std_dev]