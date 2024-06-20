import collections


def task1(nums):
    return sum(x ** 2 for x in nums)


def task2(nums):
    avg = sum(nums) / len(nums)
    return sum(x for x in nums if x >= avg)


def task3(nums):
    freq = collections.Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))


def task4(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)


def task5(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


def task6(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


def task7(nums):
    left_products = [1]
    right_products = [1]
    result = []

    for i in range(1, len(nums)):
        left_products.append(left_products[-1] * nums[i - 1])

    for i in range(len(nums) - 2, -1, -1):
        right_products.insert(0, right_products[0] * nums[i + 1])

    for i in range(len(nums)):
        result.append(left_products[i] * right_products[i])

    return result


def task8(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def task9(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []

    top = left = 0
    bottom = rows - 1
    right = cols - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


def task10(points, k):
    return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]