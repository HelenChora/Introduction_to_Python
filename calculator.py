print("1. Addition (+)")
print("2. subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

op = input("Enter your option,1/2/3/4:")

a= float(input("Enter the first number:"))
b= float(input("Enter the second number:"))

if op == "1":
    print("Result", a+b)

elif op == "2":
    print("Result", a-b)

elif op == "3":
    print("Result", a*b) 

elif op == "4":
    if b==0:
        print("Error: division by zero")
    else:
        ("Result", a/b)  

else:
    print("Unknown operator:",op)             