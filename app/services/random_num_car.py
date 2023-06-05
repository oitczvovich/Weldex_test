import random
import string
import asyncio

NUM = str(random.randint(1000, 9999))
LETTER = list(string.ascii_uppercase)
LETTER.remove('O')


def random_num_car():
    """Функция для создания рандомного номера в формате '1000A'."""
    res = str(random.randint(1000, 9999)) + random.choice(LETTER)
    return res
