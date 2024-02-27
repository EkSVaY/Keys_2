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

    final_year = (this_year + 1) + (((length_of_roads - (budget_in_year - (cost_fabric * 20) / cost_km_2023))
                               * cost_km_2024) / budget_in_year)
    total_price =
    km_of_workers = ((((worker_2023 * salary * 12) * tax) / cost_km_2023)
                     + (((worker_2024 * salary * 12) * (final_year - 2023) * tax) / cost_km_2024))
    percentage_of_salaries =
    budget_in_year_5 =

    print(f"{ru.FINAL_YEAR_BUILD} - {int(final_year)}")
    print(f"{ru.TOTAL_PRICE_BUILD} - {total_price}")
    print(f"{ru.KM_WORKERS} - {int(km_of_workers)}")
    print(f"{ru.PERCENT} - {int(percentage_of_salaries)}")
    print(f"{ru.PROJECT_5} - {int(budget_in_year_5)}")


if __name__ == '__main__':
    main()
