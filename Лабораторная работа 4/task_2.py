def get_count_char(str_):
    chars_dict = {}
    DEFAULT_COUNT = 0
    lower_str = str_.lower()
    for char in lower_str:
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, DEFAULT_COUNT) + 1

    return chars_dict


def chars_percentage(chars_dict):
    new_chars_dict = {}
    for char, count in chars_dict.items():
        new_chars_dict[char] = round(count / sum(chars_dict.values()) * 100, 2)

    return new_chars_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
