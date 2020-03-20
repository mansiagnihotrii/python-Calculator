import re

previous=0
run=True


def calculator():
    global run,previous
    if previous == 0:
        equation = input("Enter the equation:  ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye")
        run = False
        return
    else:
        equation = re.sub('[a-zA-Z,.:()" "]',' ',equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous)+equation)



while(run):
    calculator()
