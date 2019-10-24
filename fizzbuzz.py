#fizzbuzz Sample

x = 1
while x < 101:
  if x % 3==0 and x % 5 == 0:
    print("number is:" +str(x))
    print("fizzbuzz")
    x= x+1
  elif x % 3 == 0:
    print("number is:" +str(x))
    print("fizz")
    x= x+1
  elif x % 5== 0:
    print("number is:" +str(x))
    print("buzz")
    x= x+1
  else:
    x= x+1
