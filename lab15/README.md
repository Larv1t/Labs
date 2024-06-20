Лабораторна робота №15: Overview of Big Data Technologies.

Мета роботи

Освоїти основні концепції та функції для обробки текстових даних в мові програмування Python.

Опис завдання

Розробити набір функцій для обробки текстових даних, таких як очищення, фільтрація, видобуток ключових слів, нормалізація даних, об'єднання рядків, обчислення суми числових рядків, фільтрація чисел, відображення на квадрати чисел і зворотній порядок рядків.

Виконання роботи

Структура проекту: Кожна лабораторна робота завантажена у відповідну папку на GitHub. Назва папки відповідає номеру лабораторної роботи (наприклад, labX).

Опис кожного файлу та його призначення:
main.py: Основний код програми з реалізацією усіх функцій.
README.md: Файл з детальним поясненням проекту та виконані завдання.

Опис основних функцій та методів з поясненням їх роботи:

clean_data(a): Приймає рядок з комами, розділяє його на частини, видаляє зайві пробіли і перетворює до нижнього регістру.

filter_emails(a): Фільтрує список слів, залишаючи лише ті, які мають один символ '@'.

extract_keywords(a, b): Виділяє ключові слова з рядка a, які мають довжину більше b.

process_text(a): Обробляє рядок, видаляючи спеціальні символи, зайві пробіли і перетворює до нижнього регістру.

normalize_data(a): Нормалізує список чисел, розділених комами, переводячи їх до діапазону від 0 до 1.

concatenate_strings(a, b): Об'єднує рядок a, видаляючи всі входження b.

sum_numeric_strings(a): Обчислює суму всіх чисел, розділених комами, у рядку a.

filter_numbers(a, b): Фільтрує числа з рядка a, залишаючи лише ті, які більше b.

map_to_squares(a): Перетворює список чисел, розділених комами, в їх квадрати.

reverse_strings(a): Перевертає кожний рядок, розділений комами, у рядку a.

Приклади використання:

 Функція `clean_data`
```python
input_data = "   Apple,   Banana,   Orange   "
cleaned_data = clean_data(input_data)
print(cleaned_data)  # Output: ['apple', 'banana', 'orange']
```

 Функція `filter_emails`
```python
input_text = "john.doe@example.com jane.smith@gmail.com invalid_email"
filtered_emails = filter_emails(input_text)
print(filtered_emails)  # Output: ['john.doe@example.com', 'jane.smith@gmail.com']
```

### Функція `extract_keywords`
```python
input_text = "python programming language is awesome"
min_length = 5
keywords = extract_keywords(input_text, min_length)
print(keywords)  # Output: ['python', 'programming', 'language', 'awesome']
```

 Функція `process_text`
```python
input_data = "apple, banana,   orange, !grape!, kiwi"
processed_words = process_text(input_data)
print(processed_words)  # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi']
```

 Функція `normalize_data`
```python
input_data = "  10.5, 20.5, 30.5, 40.5  "
normalized_values = normalize_data(input_data)
print(normalized_values)  # Output: [0.25, 0.5, 0.75, 1.0]
```

 Функція `concatenate_strings`
```python
input_string = "Hello, World!"
separator = ","
concatenated_string = concatenate_strings(input_string, separator)
print(concatenated_string)  # Output: "Hello World!"
```

 Функція `sum_numeric_strings`
```python
input_data = "10, 20, 30, invalid, 40"
total_sum = sum_numeric_strings(input_data)
print(total_sum)  # Output: 100
```

 Функція `filter_numbers`
```python
input_text = "There are 123 apples and 456 oranges"
minimum_number = 200
filtered_numbers = filter_numbers(input_text, minimum_number)
print(filtered_numbers)  # Output: [123, 456]
```

 Функція `map_to_squares`
```python
input_numbers = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(input_numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

 Функція `reverse_strings`
```python
input_strings = "apple, banana, orange"
reversed_strings = reverse_strings(input_strings)
print(reversed_strings)  # Output: ['elppa', 'ananab', 'egnaro']
```

Ці приклади демонструють різноманітні аспекти функцій із вашого коду і показують, як вони можуть бути застосовані у практичних ситуаціях.

Результати

Усі функції були успішно перевірені з різними вхідними даними і повертали очікувані результати.

Висновки

Ця лабораторна робота дозволила ефективно ознайомитися з різноманітними методами обробки текстових даних у Python, що є важливим аспектом розвитку навичок у сфері аналізу та обробки даних.
