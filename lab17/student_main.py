from itertools import combinations


def number_generator(num):
    for i in num:
        yield i


def even_number_generator(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i


def odd_number_generator(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number_generator(limit):
    primes = []
    i = 2
    while i <= limit:
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            yield i
        i += 1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)


def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)


def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val


def dfs_traversal(graph, start):
    v = set()
    s = [start]
    while s:
        node = s.pop()
        if node not in v:
            v.add(node)
            yield node
            for i in graph[node][::-1]:
                s.append(i)


def bfs_traversal(graph, start):
    v = set()
    q = [start]
    v.add(start)
    while q:
        node = q.pop(0)
        yield node
        for i in graph[node]:
            if i not in v:
                v.add(i)
                q.append(i)


def dict_keys_generator(d):
    for k in d:
        yield k


def dict_values_generator(d):
    for v in d.values():
        yield v


def dict_items_generator(d):
    for k, v in d.items():
        yield k, v


def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for w in line.strip().split():
                yield w


def string_chars_generator(string):
    for c in string:
        yield c


def unique_elements_generator(lst):
    seen = set()
    for i in lst:
        if i not in seen:
            seen.add(i)
            yield i


def reverse_list_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


def cartesian_product_generator(lst1, lst2):
    for i1 in lst1:
        for i2 in lst2:
            yield i1, i2


def permutations_generator(lst):
    if not lst:
        yield ()
    else:
        for i in range(len(lst)):
            e = lst[i]
            r = lst[:i] + lst[i + 1:]
            for perm in permutations_generator(r):
                yield (e,) + perm


def combinations_generator(lst):
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            yield comb


def tuple_list_generator(lst):
    for tup in lst:
        yield tup


def parallel_lists_generator(*lists):
    iter = [iter(lst) for lst in lists]
    while True:
        values = []
        for it in iter:
            try:
                values.append(next(it))
            except StopIteration:
                return
        yield tuple(values)


def flatten_list_generator(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            yield from flatten_list_generator(i)
        else:
            yield i


def nested_dict_generator(nested_dict):
    for k, v in nested_dict.items():
        if isinstance(v, dict):
            yield from nested_dict_generator(v)
        else:
            yield k, v


def powers_of_two_generator(n):
    p = 1
    for i in range(n + 1):
        yield p
        p *= 2


def powers_of_base_generator(base, limit):
    p = 1
    while p <= limit:
        yield p
        p *= base


def squares_generator(start, end):
    for i in range(start, end + 1):
        yield i ** 2


def cubes_generator(start, end):
    for i in range(start, end + 1):
        yield i ** 3


def factorials_generator(n):
    f = 1
    for i in range(n + 1):
        yield f
        if i > 0:
            f *= i


def collatz_sequence_generator(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n


def geometric_progression_generator(initial, common_ratio, limit):
    t = initial
    while t <= limit:
        yield t
        t *= common_ratio


def arithmetic_progression_generator(initial, common_diff, limit):
    t = initial
    while t <= limit:
        yield t
        t += common_diff


def running_sum_generator(lst):
    t = 0
    for i in lst:
        t += i
        yield t


def running_product_generator(lst):
    p = 1
    for i in lst:
        p *= i
        yield p
