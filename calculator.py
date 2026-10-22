def calculator ():
    print("Calculator")
    print("Choose an option:")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")

    option = input("Enter an option (1/2/3/4):")

    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))

    if option == "1":
        print("Result:", a + b)

    elif option =="2" :
        print("Result:", a - b)
    elif option == "3":
        print("Result:", a * b)

    elif option == "4":
        print("Result:", a / b)
        

    else :
        print("Error")


   




calculator()        
          



