# calculate pythagoras theorem hypotenus from two sides
# ask for lengths of  any two sides to calculate the other side
# use if statements to figure out what side is needed and calculate length of other 2 sides
# include question on if this triangle is right-angled
# pythagoras theorem -- a² + b² = c² (where c is the hypotenus)

import math

print("hello, this is a programme designed to calculate missing sides of triangles")
print("")
print("below, enter the details of the sides of the triangle you have")
print("")

side_a = input("what is the length of the first known side (x)?: ")
side_a = float(side_a)
print("")
side_b = input("what is the length of the second known side (y)?: ")
print("")
triangle_type = input("is it a right angled triangle?: ")
triangle_type = triangle_type.lower()
if triangle_type == "yes":
    side_a = float(side_a)
    side_b = float(side_b)
    print("")
    hypotenuse = input("is the missing side the hypotenuse?: ")
    hypotenuse = hypotenuse.lower()
    if hypotenuse == "yes":
        hypotenuse = side_a ** 2 + side_b ** 2
        hypotenuse = math.sqrt(hypotenuse)
        hypotenuse = float(hypotenuse)
        rounded_hypotenuse = round(hypotenuse, 2)

        print(f"then the hypotenuse is {rounded_hypotenuse} (2.d.p)")

    elif hypotenuse == "no":
        print("")
        print("""so the missing side is one of the other 2 sides (not hypotenuse). 
        this just got a bit more interesting""")
        print("")
        answer_2 = input("which side is the hypotenuse, x or y: ")
        answer_2 = answer_2.lower()

        if answer_2 == "x":
            missing_side = math.sqrt(side_a ** 2 - side_b ** 2)
            rounded_missing_side = round(missing_side, 2)
            print("")
            print(f"your missing side, then is {rounded_missing_side} (2.d.p) ")
        else:missing_side = (math.sqrt(side_b ** 2 - side_a ** 2))
        rounded_missing_side = round(missing_side, 2)
        print("")
        print(f"your missing side, then is {rounded_missing_side} (2.d.p) ")
        print("")
        print("thanks for using my programme")
        exit()
else:
    print("")
    print("sorry i cant help you until i learn how to do trig on python")
    exit()





