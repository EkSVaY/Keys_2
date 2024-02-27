# Part of case-study #2: Reforma
# Developer: Ekin V., Tolkochokov A., Sokolov I., Gazizov A.
#

import ru_local as ru


def main():
    '''
    Main function.
    :return: None
    '''

    this_year = 2023
    budget_in_year = float(input()) * 10 ** 9
    cost_fabric = 4 * 10 ** 9
    length_of_roads = 1575.6 * 10 ** 3
    cost_km_2023 = 55 * 10 ** 6
    cost_km_2024 = 35 * 10 ** 6
    worker_2023 = 550
    worker_2024 = 1100
    salary = 100 * 10 ** 3
    tax = 0.13

    final_year = this_year + (((length_of_roads - (budget_in_year / cost_km_2023))
                               * cost_km_2024 + (cost_fabric * 20)) / budget_in_year)
    total_price =
    km_of_workers =
    percentage_of_salaries = ((worker_2023 * salary *  tax * 12)
                              / budget_in_year + (worker_2024 * salary * tax * (final_year - 2024) * 12)
                              / (budget_in_year * (final_year - 2024)))
    budget_in_year_5 =


if __name__ == '__main__':
    main()
