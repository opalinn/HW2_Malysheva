def main(string):
  for_calculating = string.split()
  if '+' in for_calculating:
    return summation(for_calculating)
  elif '-' in for_calculating:
    return substraction()
  elif '*' in for_calculating:
    return multiplication()
  elif '/' in for_calculating:
    return dividing()
  else:
    print('Что-то не так с введенными данными, проверь!')
def summation(st):
    ans=float(st[0])+float(st[2])
    return ans
def substraction():
  pass
def multiplication():
  pass
def dividing():
  pass

string = input('Введите математическую операцию: ')
print(main(string))
