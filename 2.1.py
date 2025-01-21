def ls():
  a = int(input("enter the first number:"))
  b = int(input("enter the second number:"))
  if a>b:
    print("largest",a)
    print("smallest",b)
  elif a<b:
    print("largest",b)
    print("smallest",a)
  else:
    print("the numbers are equal")
ls()
