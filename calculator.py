def format_number(num):
  return int(num) if num.is_integer() else num
x = float(input("X: "))
y = float(input("Y: "))
operation = input("What operation? ")
if operation == "+":
    result = x+y
elif operation == "-":
    result = x-y
elif operation == "*":
    result = x*y
elif operation == "**":
    result = x**y
elif operation == "%":
    result = x%y
elif operation == "/":
    if y != 0:
        result = x/y
    else:
        result = "Error, division by zero"
else:
    result = "Invalid equation"

if isinstance(result , float) and result.is_integer() and x.is_integer() and y.is_integer():
    result = int(result)
print(f"{format_number(x)} {operation} {format_number(y)} = {result}")