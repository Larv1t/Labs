import json
def task1(filePa, ageThre):
    with open(filePa, 'r') as file:
        data = json.load(file)
    namesAboveThreshold = [entry['name'] for entry in data if entry['age'] > ageThre]
    return namesAboveThreshold

def task2(data, filePa):
    with open(filePa, 'w') as file:
        json.dump(data, file)


def task3(filePa):
    invalid_files = []
    for filePa in filePa:
        with open(filePa, 'r') as file:
            try:
                data = json.load(file)
                pass
            except json.JSONDecodeError:
                invalid_files.append(filePa)
    return invalid_files


def task4(filePa, key):
    def extract_values(obj, key):
        values = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    values.append(v)
                elif isinstance(v, (dict, list)):
                    values.extend(extract_values(v, key))
        elif isinstance(obj, list):
            for item in obj:
                values.extend(extract_values(item, key))
        return values

    with open(filePa, 'r') as file:
        data = json.load(file)
    values = extract_values(data, key)
    return values


def task5(filePa, category, updateFunc):
    with open(filePa, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item.get('category') == category:
                updateFunc(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def increase_price(item):
    item['price'] += 10


