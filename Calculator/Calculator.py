import re

print("Calculator")

previous = 0


# A simple calculator function.
def perform_math():
    global previous
    equation = ""

    if previous == 0:
        equation = input("\nEnter Equation: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        quit("Thanks! bye.")
    else:
        equation = re.sub('[A-Za-z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while True:
    perform_math()
