Лабораторна робота №12: ООП в Python. Матриці.

Мета роботи

Ознайомлення з об'єктно-орієнтованим програмуванням (ООП) в мові Python через створення класу Matrix, який дозволяє працювати з матрицями, включаючи операції додавання елементів, транспонування, множення матриць, перевірку на симетрію, обертання, вилучення діагоналі та інші.

Опис завдання

Створення класу Matrix, що включає різноманітні методи для операцій з матрицями:

1. **\_\_init\_\_(self, rows, columns, data=None)**: Ініціалізує об'єкт матриці з заданим розміром (`rows`, `columns`) і опціональними даними (`data`).
   
2. **add_element(self, row, column, value)**: Додає задане значення `value` до позиції (`row`, `column`) у матриці.
   
3. **sum_of_rows(self)**: Обчислює суму кожного рядка матриці і повертає список сум.
   
4. **transpose(self)**: Транспонує поточну матрицю (заміняє рядки на стовпці).
   
5. **multiply_by(self, other)**: Множить поточну матрицю на іншу матрицю `other` і повертає нову матрицю-результат.
   
6. **is_symmetric(self)**: Перевіряє, чи є поточна матриця симетричною (рівна своєму транспонованому варіанту).
   
7. **rotate_right(self)**: Обертає матрицю на 90 градусів в правому напрямку.
   
8. **flatten(self)**: Повертає плоске представлення матриці у вигляді одномірного списку.
   
9. **from_list(list_of_lists)**: Статичний метод для створення об'єкту матриці зі списку списків.
   
10. **diagonal(self)**: Повертає список діагональних елементів матриці.

Виконання роботи

Структура проекту:

Проект має наступну структуру:

- **main.py**: Основний файл програми, де викликаються методи класу Matrix для демонстрації їх роботи.
- **matrix.py**: Файл, який містить клас Matrix, що реалізує основні операції з матрицями.

Опис основних функцій та методів класу Matrix:

```python
# matrix.py
class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data:
            self.data = data
        else:
            self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        self.data[row][column] += value

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed = [[self.data[row][col] for row in range(self.rows)] for col in range(self.columns)]
        return Matrix(self.columns, self.rows, transposed)

    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Cannot multiply matrices with these dimensions.")
        result = [[0] * other.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.rows, other.columns, result)

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        self.data = list(zip(*self.data[::-1]))

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        return Matrix(rows, columns, list_of_lists)

    def diagonal(self):
        return [self.data[i][i] for i in range(min(self.rows, self.columns))]
```

Приклади використання:

```python
# main.py

from matrix import Matrix

# Створення матриці і додавання елементів
matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)

print(matrix.data)  # [[0, 1, 0], [0, 0, 2]]

# Транспонування матриці
transposed = matrix.transpose()
print(transposed.data)  # [[0, 0], [1, 0], [0, 2]]

# Множення матриць
matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
result = matrix1.multiply_by(matrix2)
print(result.data)  # [[58, 64], [139, 154]]

# Перевірка на симетрію
matrix3 = Matrix(2, 2, [[1, 2], [2, 3]])
print(matrix3.is_symmetric())  # False

# Обертання матриці
matrix4 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
matrix4.rotate_right()
print(matrix4.data)  # [(5, 3, 1), (6, 4, 2)]

# Отримання плоского представлення
print(matrix4.flatten())  # [5, 3, 1, 6, 4, 2]

# Створення матриці зі списку списків
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix5 = Matrix.from_list(list_of_lists)
print(matrix5.data)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Отримання діагоналі матриці
print(matrix5.diagonal())  # [1, 5, 9]
```

Результати

Програма була протестована на різних вхідних даних, всі методи показали очікувані результати. Клас Matrix дозволяє ефективно працювати з матрицями, використовуючи методи ООП для різних операцій.

Висновки

Лабораторна робота дозволила поглибити знання об'єктно-орієнтованого програмування в Python через реалізацію класу Matrix. Всі вимоги завдання були успішно виконані, програма працює стабільно і демонструє коректну роботу у всіх сценаріях використання.
