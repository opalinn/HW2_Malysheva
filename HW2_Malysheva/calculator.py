def main(string):
  for_calculating = string.split()
  if '+' in for_calculating:
    return summation(for_calculating)
  elif '-' in for_calculating:
    return subtraction(for_calculating)
  elif '*' in for_calculating:
    return multiplication()
  elif '/' in for_calculating:
    return dividing()
  else:
    print('Что-то не так с введенными данными, проверь!')

def summation(for_calculating):
    ans=float(for_calculating[0])+float(for_calculating[2])
    return ans
  
def is_float(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False
      
def summation():
  pass

def subtraction(for_calculating):
  numbers = []
  for i in for_calculating:
    if i.isnumeric() or is_float(i):
        numbers.append(float(i))
  return(numbers[0] - numbers[1])

def multiplication():
  pass

def dividing():
  pass

string = input('Введите математическую операцию: ')
print(main(string))
