operations = {'addition': 1, 'subtraction': 2, 'multiplication': 3, 'division': 4}

def chomp_addition(num1, num2):
    return num1 + num2

def chomp_subtraction(num1, num2):
    return num1 - num2

welcome_message = \
        ("Welcome to the Chomp Calc App! \n "
         "Select which operation to perform: \n "
         "1. Addition \n "
         "2. Subtraction \n "
         "3. Multiplication \n "
         "4. Division")

print(welcome_message)

print("Operation: ")

try:
    operation_selected = int(input())
except ValueError:
    print("Wrong Value Type")
    exit()

if operation_selected in operations.values():
    pass
else:
    print ("error")

if operation_selected == 1:
    print ("Awesome Addition")
    print ("Enter number 1: ")
    try:
        num1 = float(input())
    except ValueError:
        print("Wrong Value Type")
        exit()
    print ("Enter number 2: ")
    try:
        num2 = float(input())
    except ValueError:
        print("Wrong Value Type")
        exit()
    result = chomp_addition(num1, num2)
    print (result)

if operation_selected == 2:
    print ("Sweet Subtraction")
    print ("Enter number 1: ")
    try:
        num1 = float(input())
    except ValueError:
        print("Wrong Value Type")
        exit()
    print ("Enter number 2: ")
    try:
        num2 = float(input())
    except ValueError:
        print("Wrong Value Type")
        exit()
    result = chomp_subtraction(num1, num2)
    print (result)