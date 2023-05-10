import numpy as np
from itertools import product
from numba import njit

# Декоратор njit компилирует функцию fuel_consumption для ускорения выполнения
@njit
def fuel_consumption(generator_powers):
    # Здесь можно определить функции потребления топлива для каждого генератора
    # в виде полиномов второго порядка или любых других функций
    # В данном примере использованы произвольные функции

    generator1 = lambda x: 8 + 0.14*x+6.8/10000*x**2
    generator2 = lambda x: 7.9 + 0.141*x+7/10000*x**2
    generator3 = lambda x: 8 + 0.139*x+7.9/10000*x**2

    consumption1 = generator1(generator_powers[0])
    consumption2 = generator2(generator_powers[1])
    consumption3 = generator3(generator_powers[2])

    return consumption1 + consumption2 + consumption3

def find_min_fuel_consumption(total_power):
    generator_power = 200
    generators_count = 3

    # Создание массива мощностей генераторов с использованием numpy
    powers = np.arange(generator_power + 1)

    # Создание массива всех возможных комбинаций мощностей генераторов с использованием itertools и numpy
    combinations = np.array(list(product(powers, repeat=generators_count)))

    # Инициализация переменных для минимального потребления топлива и оптимальной комбинации
    min_fuel_consumption = np.inf
    optimal_combination = None

    # Получение количества итераций
    iterations_count = combinations.shape[0]

    # Перебор всех комбинаций мощностей генераторов
    for combination in combinations:
        fuel_cons = fuel_consumption(combination)

        # Проверка, что сумма мощностей генераторов равна требуемой общей мощности
        if np.sum(combination) == total_power:
            # Обновление минимального потребления топлива и оптимальной комбинации
            if fuel_cons < min_fuel_consumption:
                min_fuel_consumption = fuel_cons
                optimal_combination = combination

    return min_fuel_consumption, optimal_combination, iterations_count

# Требуемая общая мощность
total_power = 360

# Поиск минимального потребления топлива и оптимальной комбинации мощностей генераторов
min_fuel, combination, iterations = find_min_fuel_consumption(total_power)

# Вывод результатов
print(f"Минимальное потребление топлива: {min_fuel}")
print("Оптимальная комбинация мощностей генераторов:", combination)
print(f"Количество итераций: {iterations}")