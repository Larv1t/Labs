import re

def task1(i):
    return bool(re.match(r'^([a-z0-9][a-z0-9])+$', i))

def task2(i):
    return bool(re.match(r'^[A-Z]+$', i))

def task3(i):
    a = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(a, i))

def task4(i):
    a = r'^([0-2]\d|2[0-3]):([0-5]\d|2[0-9]):([0-5]\d|2[0-9])'
    return bool(re.match(a, i))

def task5(i):
    return bool(re.match(r'^\d{5}(-\d{4})?$', i))

def task6(i):
    return bool(re.match(r'^[a-z0-9_-]{6,12}$', i))

def task7(i):
    a = r"^(4|5|6)\d{3}(-|\s)?\d{4}(-|\s)?\d{4}(-|\s)?\d{4}$"
    return bool(re.match(a, i))

def task8(i):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', i))

def task9(i):
    a = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(a, i))

def task10(i):
    a = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(a, i))