# MyCalculatorAPP +_-
username = str(input("Enter UserName : "))
print(f"WELCOME TO MY CALCULATOR {username} ")

def add(num1, num2):
    print("Addition -->")
    print(num1+num2)
def sub(num1, num2):
    print("Subtraction -->")
    print(num1-num2)
def mul(num1, num2):
    print("Multiplication -->")
    print(num1*num2)
def exp(num1, num2):
    print("Exponentation -->")
    print(num1**num2)
def div(num1, num2):
    print("Division -->")
    print(num1/num2)
def fdiv(num1, num2):
    print("FloorDivision -->")
    print(num1//num2)
def mod(num1, num2):
    print("Modulus -->")
    print(num1%num2)

print(" ENTER 1 FOR Addition....! \n ENTER 2 FOR Subtraction....! \n ENTER 3 FOR Multiplication....! \n ENTER 4 FOR Exponentation....! \n ENTER 5 FOR Division....! \n ENTER 6 FOR FloorDivision: - \n ENTER 7 FOR Modulus....!")

operation = int(input("Enter your desired Choice of Operation: "))
num1 = int(input("Enter the First Number: "))
num2 = int (input("Enter the Second Number: "))

if operation==1:
    add(num1, num2) 
elif operation==2:
    sub(num1, num2) 
elif operation==3:
    mul(num1, num2)
elif operation==4:
    exp(num1, num2)
elif operation==5:
    div(num1, num2)
elif operation==6:
    fdiv(num1, num2)
elif operation==7:
    mod(num1, num2)
else:
    print("Entered value is Invalid!")
    print("plz Recheck the Numbers and again Enter them")   
