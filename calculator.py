a = int(input("Write first number: " + "\n"))
b = int(input("Write second number: " + "\n"))

c = input("What do you want to do -, +, *, /,: ")

if c == "-":
    d = a - b 
    print(d)
elif c == "+":
    d = a + b
    print(d)
elif c == "/":
    d = a / b
    print(d)
elif c == "*":
    d = a * b
    print(d)
else:
     print("i cant do this")


