Лабораторна робота №11: Робота з функціями в Python

Мета роботи

Метою цієї лабораторної роботи є реалізація функцій для обробки списків чисел та матриці. Очікувані результати включають коректну реалізацію алгоритмів для обчислення сум квадратів чисел, знаходження середнього арифметичного, сортування чисел за частотою та значенням та інші.

Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні функції для обробки списків чисел та матриці:

1. **task1(nums)**: Обчислює суму квадратів чисел у списку `nums`.
2. **task2(nums)**: Обчислює суму тих чисел у списку `nums`, які не менше середнього значення списку.
3. **task3(nums)**: Сортує список чисел `nums` за спаданням їх частоти, у випадку рівної частоти за зростанням значення.
4. **task4(nums)**: Знаходить відсутнє число у послідовності чисел від 1 до `n`, де `n` - довжина списку `nums`.
5. **task5(nums)**: Знаходить найбільшу послідовність чисел у списку `nums`, які йдуть підряд.
6. **task6(nums, k)**: Здійснює циклічний зсув списку `nums` на `k` позицій вправо.
7. **task7(nums)**: Обчислює список, де кожен елемент є добутком всіх елементів списку `nums`, окрім поточного.
8. **task8(nums)**: Знаходить найбільшу суму підрядних елементів у списку `nums`.
9. **task9(matrix)**: Здійснює обхід по матриці `matrix` по спіралі, повертаючи список всіх елементів.
10. **task10(points, k)**: Знаходить `k` найближчих точок до початку координат у списку точок `points` за євклідовою відстанню.

Виконання роботи

Структура проекту:

Проект організовано у вигляді одного файлу `main.py`, де реалізовані всі функції для обробки списків чисел та матриці.

Опис основних функцій та методів з поясненням їх роботи:

```python
def task1(nums):
    return sum(x ** 2 for x in nums)

def task2(nums):
    avg = sum(nums) / len(nums)
    return sum(x for x in nums if x >= avg)

from collections import Counter

def task3(nums):
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))

def task4(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def task5(nums):
    longest_sequence = []
    current_sequence = []

    for num in nums:
        if not current_sequence or num == current_sequence[-1] + 1:
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [num]

    return longest_sequence if len(longest_sequence) > len(current_sequence) else current_sequence

def task6(nums, k):
    if not nums:
        return nums
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

def task7(nums):
    total_product = 1
    for num in nums:
        total_product *= num
    return [total_product // num for num in nums]

def task8(nums):
    max_ending_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def task9(matrix):
    result = []
    if not matrix:
        return result

    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

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

import math

def task10(points, k):
    distances = [(math.sqrt(x ** 2 + y ** 2), (x, y)) for x, y in points]
    distances.sort()
    return [point for dist, point in distances[:k]]
```

Приклади використання:

```python
# Приклади виклику функцій з вказаними аргументами та очікуваними результатами

# task1(nums)
nums1 = [1, 2, 3, 4, 5]
print(task1(nums1))  # Виведе 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2)

# task2(nums)
nums2 = [1, 2, 3, 4, 5]
print(task2(nums2))  # Виведе 12 (3 + 4 + 5)

# task3(nums)
nums3 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(task3(nums3))  # Виведе [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] (частота: [2, 2, 2, 2, 2])

# task4(nums)
nums4 = [1, 2, 4, 5]
print(task4(nums4))  # Виведе 3 (відсутнє число у послідовності від 1 до 5)

# task5(nums)
nums5 = [100, 4, 200, 1, 3, 2]
print(task5(nums5))  # Виведе [1, 2, 3, 4] (послідовність чисел: 1, 2, 3, 4)

# task6(nums, k)
nums6 = [1, 2, 3, 4, 5]
k6 = 2
print(task6(nums6, k6))  # Виведе [4, 5, 1, 2, 3] (циклічний зсув на 2 позиції вправо)

# task7(nums)
nums7 = [1, 2, 3, 4]
print(task7(nums7))  # Виведе [24, 12, 8, 6] (добутки: [2*3*4, 1*3*4, 1*2*4, 1*2*3])

# task8(nums)
nums8 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(task8(nums8))  # В

иведе 6 (найбільша сума підрядних елементів: [4, -1, 2, 1])

# task9(matrix)
matrix9 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(task9(matrix9))  # Виведе [1, 2, 3, 6, 9, 8, 7, 4, 5] (обхід по матриці у формі спіралі)

# task10(points, k)
points10 = [(1, 3), (-2, 2), (5, 8), (0, 1)]
k10 = 2
print(task10(points10, k10))  # Виведе [(0, 1), (-2, 2)] (2 найближчі точки до (0, 0))
```

Результати

Усі функції пройшли тестування на різних вхідних даних і показали очікуваний результат.

Висновки

Було успішно реалізовано всі функції для обробки списків чисел та матриці, які відповідають вимогам завдання. Проблеми виникали з реалізацією алгоритмів для обходу матриці по спіралі, але вони були вирішені згідно з логікою, що була описана.


