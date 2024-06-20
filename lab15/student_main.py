import re

def clean_data(a):
    return list(map(lambda x: x.strip().lower(), a.split(',')))

def filter_emails(a):
    b = a.split()
    return list(filter(lambda x: x.count('@') == 1, b))

def extract_keywords(a, b):
    c = a.split()
    return list(filter(lambda x: len(x)>b, c))

def process_text(a):
    b = a.split(',')
    def process_word(c):
        c = c.strip()
        c = re.sub(r'[^\w\s]', '', c)
        c = c.lower()
        return c
    d = map(process_word, b)
    return list(filter(lambda c: len(c) > 1, d))

def normalize_data(a):
    v = [float(x.strip()) for x in a.split(",")]
    m = max(v)
    n = [(x / m) for x in v]
    return [round(x, 3) for x in n]

def concatenate_strings(a, b):
    return ''.join(a.split(b))

def sum_numeric_strings(a):
    v = a.split(",")
    s = 0
    for i in v:
        try:
            s += int(i.strip())
        except ValueError:
            pass
    return s

def filter_numbers(a, b):
    return [int(i) for i in re.findall(r'\d+', a) if int(i) > b]

def map_to_squares(a):
    return [int(i)**2 for i in a.split(", ")]

def reverse_strings(a):
    return [i[::-1] for i in a.split(",")]