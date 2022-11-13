from random import randint
from typing import List


def get_unique_list_numbers(left: int = -10, right: int = 10, list_length: int = 15) -> List[int]:
    numbers_list = []
    while len(numbers_list) < list_length:
        rand_num = randint(left, right)
        if rand_num not in numbers_list:
            numbers_list.append(rand_num)
    return numbers_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
