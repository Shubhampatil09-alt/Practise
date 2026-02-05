# Write a simple calculator program.
import emoji
print("============== Start Calculation ============== ")
print("")
a =int(input("Enter value of A :\n "))
b =int(input("Enter value of B :\n "))

while True:
    print("============== Menu ==============")
    print("1. Addition, \n2. Substraction\n3. Multiplication \n4. Division")
    method_type  = input("Which operation do you want to execute :")
    if method_type == '1':
        print(f"Addition of {a} and {b} is : {a+b}")
    if method_type == '2':
        print(f"Substraction of {a} and {b} is : {a-b}")
    if method_type == '3':
        print(f"Multiplication of {a} and {b} is : {a*b}")
    if method_type == '4':
        print(f"Division of {a} and {b} is : {a/b}")
    
    cont = input("Do you want to continue (Y/N)").upper()
    if cont == 'Y':
        check = input(f"Do you want to continue with same numbers is {a} and {b} (Y/N)").upper()
        if check == 'N':
            a =int(input("Enter value of A : "))
            b =int(input("Enter value of B : "))
    else:
        print("Thank you share your exeperience with us.\n")
        print(emoji.emojize(":grinning_face_with_big_eyes:"))
        break

