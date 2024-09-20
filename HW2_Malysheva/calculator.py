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


def divide(for_calculating):
    operand1 = float(for_calculating[0])
    operand2 = float(for_calculating[1])
    if operand2 == 0:
        return "Ошибка: Деление на ноль"
    result = operand1 / operand2
    return result

string = input("Введите математическую операцию: ")
print(main(string))
