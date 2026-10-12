# try to stop errors (dividing by zero, wrong input etc)
##factorials
#list constants as results of equations: eg e*e=e^2
##log and exponent functions
##memory function
##keep track of all calculations and print them if user types "history"

# Notes
# started on 26/10/25
# first step is to write out introduction and options menu, then draw decision tree
# did the basic calculations, and learned how to use while loops to make the calculator continuous
# just added capability to use π and e
# did the nth root section
# did trig stuff

#tasks for tmrw: 1) logx stuff, 2)stop errors, 3)list constants, 4)factorials, 5)memory, 6)history function

import math

print("Hello, and welcome to Python Calculator, your one stop shop for all calculations you could need")
print("")
print("as this is still under construction, you can only do operations with 2 numbers (SOZ)")
print("")
name = input("What is your name?:  ")
print("")
print(f"Hello, {name}!")
print("")
user_response = input(f" do you want to calculate {name}? (Yes/No): ")
user_response = user_response.lower()
while user_response == "yes":
    calculation_type = int(input("""What type of calculation do you want? the options include; 

    1) addition
    2) subtraction
    3) multiplication
    4) division
    5) indices
    6) percentages
    7) nth root
    8) trig

    input the number beside your desired calculation type:    """))
    print("")
    print(
        """**Note, if you need to make use of (π) or Euler's Constant (e), type "e" or "pi" when asked for number input""")
    print("")

    if calculation_type == 1:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        addition = number_1 + number_2
        addition = round(addition, 3)
        print(f" {number_1} + {number_2} = {addition} (3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()


    elif calculation_type == 2:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        subtraction = number_1 - number_2
        subtraction = round(subtraction, 3)
        print(f" {number_1} - {number_2} = {subtraction} (3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()


    elif calculation_type == 3:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        multiplication = number_1 * number_2
        multiplication = round(multiplication, 3)
        print(f" {number_1} * {number_2} = {multiplication} (3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()


    elif calculation_type == 4:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        division = number_1 / number_2
        division = round(division, 3)
        print(f" {number_1} / {number_2} = {division} (3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()


    elif calculation_type == 5:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        print("result is x^y where x is first number and y is second number")
        print("")
        indices = pow(number_1, number_2)
        indices = round(indices, 3)
        print(f" {number_1} ^ {number_2} : {indices}(3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()

    elif calculation_type == 6:
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        print("result is (x/y)*100 where x is first number and y is second number")
        print("")
        percentage = (number_1 / number_2) * 100
        percentage = round(percentage, 2)
        print(f" {number_1} / {number_2} as a percentage is : {percentage}% (2.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()


    if calculation_type == 7:
        print("nth root calculates n√(x) where n is the second number and x is the first number")
        number_1 = input("first number : ")
        if number_1 == "pi":
            number_1 = math.pi
        elif number_1 == "-pi":
            number_1 = -math.pi
        elif number_1 == "e":
            number_1 = math.e
        elif number_1 == "-e":
            number_1 = -math.e
        else:
            number_1 = float(number_1)
        print("")

        number_2 = input("second number : ")
        if number_2 == "pi":
            number_2 = math.pi
        elif number_2 == "-pi":
            number_2 = -math.pi
        elif number_2 == "e":
            number_2 = math.e
        elif number_2 == "-e":
            number_2 = -math.e
        else:
            number_2 = float(number_2)
        print("")

        nth_root = number_1 ** (1 / number_2)
        nth_root = round(nth_root, 3)
        if number_2 == 2:
            root_word = "square"
        elif number_2 == 3:
            root_word = "cube"
        else:
            root_word = f"{number_2}th"
        print(f"The {root_word} root of {number_1} = {nth_root} (3.d.p)")
        user_response = input("do you want to continue? (Yes/No): ")
        if user_response == "no":
            print(F"thanks {name} for using python calculator, come back next time for new features")
            exit()

    if calculation_type == 8:
        function_type = input("Direct or Inverse Function?: ")
        function_type = function_type.lower()
        print("")
        if function_type == "direct":
            print("this function calculates ratios and returns the answer in radians")
            print("")
            function_choice = input("Sine, Cosine, or Tangential? (please type out full name): ")
            function_choice = function_choice.lower()
            print("")

            if function_choice == "sine":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")

                print("result is sin(x/y) where x is first number and y is second number")
                print("")
                sine = math.sin(number_1 / number_2)
                sine = round(sine, 3)
                print(f" sin({number_1}/{number_2}) is : {sine} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()

            elif function_choice == "cosine":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")
                print("result is cos(x/y) where x is first number and y is second number")
                print("")
                cos = math.cos(number_1 / number_2)
                cos = round(cos, 3)
                print(f" cos({number_1} / {number_2}) is : {cos} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()

            elif function_choice == "tangential":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")
                print("result is tan(x/y) where x is first number and y is second number")
                print("")
                tan = math.tan(number_1 / number_2)
                tan = round(tan, 3)
                print(f" tan({number_1}/{number_2}) is : {tan} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()

        if function_type == "inverse":
            print("this function calculates ratios and returns the answer in radians")
            function_choice = input("arcsin, arccos, or arctan? (please type out full name): ")
            function_choice = function_choice.lower()
            print("")
            if function_choice == "arcsin":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")

                print("result is arcsin(x/y) where x is first number and y is second number")
                print("")
                arcsine = math.asin(number_1 / number_2)
                arcsine = round(arcsine, 3)
                print(f" arcsin({number_1}/{number_2}) is : {arcsine} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()

            if function_choice == "arccos":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")

                print("result is arccos(x/y) where x is first number and y is second number")
                print("")
                arccosine = math.acos(number_1 / number_2)
                arccosine = round(arccosine, 3)
                print(f" arccos({number_1}/{number_2}) is : {arccosine} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()
            if function_choice == "arctan":
                number_1 = input("first number:")
                if number_1 == "pi":
                    number_1 = math.pi
                elif number_1 == "-pi":
                    number_1 = -math.pi
                elif number_1 == "e":
                    number_1 = math.e
                elif number_1 == "-e":
                    number_1 = -math.e
                else:
                    number_1 = float(number_1)
                print("")

                number_2 = input("second number:")
                if number_2 == "pi":
                    number_2 = math.pi
                elif number_2 == "-pi":
                    number_2 = -math.pi
                elif number_2 == "e":
                    number_2 = math.e
                elif number_2 == "-e":
                    number_2 = -math.e
                else:
                    number_2 = float(number_2)
                print("")

                print("result is arctan(x/y) where x is first number and y is second number")
                print("")
                arctangenttial = math.atan2(number_1 / number_2)
                arctangenttial = round(arctangenttial, 3)
                print(f" arctan({number_1}/{number_2}) is : {arctangenttial} (3.d.p)")
                user_response = input("do you want to continue? (Yes/No): ")
                if user_response == "no":
                    print(F"thanks {name} for using python calculator, come back next time for new features")
                    exit()


    else:
        print("")
        print("you have to pick from 1-8 only, try again next time")
        exit()

else:
    print("")
    print("okay! come back when you're ready")
    exit()
