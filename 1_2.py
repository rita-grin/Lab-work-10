# 2. Сформувати функцію для обчислення цифрового кореню натурального числа.
# Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
# числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
# сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
# числа.
# Грінченко Маргарита 1 курс група 122Б


from time import time
from memory_profiler import profile


@profile
def start(n):  # допоміжна функція для обрахування пам'яті
    return cortex_rec(n)


def sum_rec(n):  # функція знаходження суми рекурсією
    if n < 10:
        return n
    return n % 10 + sum_rec(n // 10)
    return


def cortex_rec(n):  # функція знаходження цифрового кореня рекурсією
    if n < 10:
        return n
    return cortex_rec(sum_rec(n))


@profile
def cortex_cyc(n):  # функція знаходження цифрового кореня циклом
    s = str(n)
    while len(s) > 1:
        n = 0
        for i in s:
            n += int(i)
        s = str(n)
    return s


print("функція знаходження цифрового кореня рекурсією: ")
while True:
    try:
        n = int(input("Ведіть число: "))
        break
    except ValueError:
        print("тільки числа")

tic = time()  # час початку роботи функції
print(start(n))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї
print()

print("функція знаходження цифрового кореня циклом: ")
while True:
    try:
        n = int(input("Ведіть число: "))
        break
    except ValueError:
        print("тільки числа")

tic = time()  # час початку роботи функції
print(cortex_cyc(n))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї
# рекурсія працює швидше але цикл потребує менше пам'яті.Перше й друге не складне в реалізації.
