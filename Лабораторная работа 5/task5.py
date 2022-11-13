from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int = 8) -> str:
    all_symbols = ascii_lowercase + ascii_uppercase + digits
    return "".join(sample(all_symbols, n))


print(get_random_password())
