def addition(num1, num2):
    return num1 + num2 

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1 , num2):
    return num1*num2

def division(num1 , num2):
    if num2!= 0:
        return num1/num2
    else:
        return "Invalid As divisionn by zero is not possible" 

choice = int(input("Enter the arthemetic operation"))
while True:
    if choice in("1","2","4","5"):
        num1 = int(input("Enter number 1"))
        num2 = int(input("Enter number 2"))

    if choice == '1':
        print(f"{num1} + {num2} = {addition(num1, num2)}")
    elif choice =='2':
        print(f"{num1} - {num2} = {substraction(num1, num2)}")
    elif choice =="3":
        print( f"{num1} * {num2} = {multiplication(num1, num2)}")
    elif choice == "4":
        print(f"{num1} / {num2} = {division(num1, num2)}")
    elif choice =="5":
        print("Exiting")
    else:
        print("invalid choice")

