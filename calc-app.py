operations = {'addition': 1, 'subtraction': 2, 'multiplication': 3, 'division': 4}

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
    print ("Great")
else:
    print ("error")