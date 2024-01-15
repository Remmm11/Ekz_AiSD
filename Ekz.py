import random as r

sum_str = 0
min_sum = 10 ** 10

n = int(input('Введите размерность матрицы: '))

matrix = [[r.randint(-10, 10) for i in range(n)] for j in range(n)]

print('Матрица:')
for i in range(n): print(matrix[i])

for i in range(n):
    sum_str = sum(matrix[i])
    if sum_str % 2 != 0 and sum_str < min_sum:
        min_sum = sum_str
        index = i

print(f'Строка с минимальной нечётной суммой элементов: {matrix[index]} Сумма строки: {min_sum}')
