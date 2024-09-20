def main(string):
    for_calculating = string.split()
    if "+" in for_calculating:
        return summation()
    elif "-" in for_calculating:
        return substraction()
    elif "*" in for_calculating:
        return multiplication()
    elif "/" in for_calculating:
        return dividing()
    else:
        print("Что-то не так с введенными данными, проверь!")


def summation():
    pass


def substraction():
    pass


def multiplication():
    pass


def dividing():
    elements = string.split()
    num1 = float(elements[0])
    operator = elements[1]
    num2 = float(elements[2])
    if num2 == 0:
        return "Ошибка: деление на ноль."
    return num1 / num2


string = input("Введите математическую операцию: ")
print(main(string))
