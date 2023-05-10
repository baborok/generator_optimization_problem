import numpy as np
from itertools import product
from numba import njit
from tqdm import tqdm

@njit
def fuel_consumption(generator_powers):
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

    powers = np.arange(generator_power + 1)
    combinations = np.array(list(product(powers, repeat=generators_count)))

    min_fuel_consumption = np.inf
    optimal_combination = None

    iterations_count = combinations.shape[0]

    with tqdm(total=iterations_count, desc="Progress") as pbar:
        for combination in combinations:
            fuel_cons = fuel_consumption(combination)

            if np.sum(combination) == total_power:
                if fuel_cons < min_fuel_consumption:
                    min_fuel_consumption = fuel_cons
                    optimal_combination = combination

            pbar.update(1)  # Обновление прогресс бара

    return min_fuel_consumption, optimal_combination, iterations_count

total_power = 360

min_fuel, combination, iterations = find_min_fuel_consumption(total_power)

print(f"Минимальное потребление топлива: {min_fuel}")
print("Оптимальная комбинация мощностей генераторов:", combination)
print(f"Количество итераций: {iterations}")