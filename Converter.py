BASE = {
  "I":1,
  "V":5,
  "X":10,
  "L":50,
  "C":100,
  "M":1000
}

rim_value = tuple(input('Введите римскую цифру: '))

def transliter(rim_value):
  x = []
  for i in rim_value:
    y = BASE[i] 
    x.append(y)
    arab_value = tuple(x)
  return arab_value

print(transliter(rim_value))
res = transliter(rim_value)

def calc(res):
  try:
    sum = 0
    for i in range(len(res)):
      if res[i] >= res[i+1]:
        sum += res[i] 
      else:
        sum += res[i+1] - res[i]
    
  except IndexError:
    if res[i] > res[i-1]:
      pass
    else:
      sum += res[-1]
  return sum  
print(calc(res))
