print("Loading Modules...", end="\r")
import os
import re
os.system("") # <-- To make ANSI work
import decimal
decimal.getcontext().prec = 30
print("Loading Finished!", end="\r")

history = list()

def main(equation):
    if equation == "CLEAR":
        return "\033[2J"

    if equation == "HISTORY":
        rrr = "HISTORY:\n"
        for eq in history:
            rrr += eq + "\n"
        return rrr

    terms = equation.split()
    if len(terms) > 3 or len(terms) < 3: return "Please retype your problem :(. Error Type: Term Length." 

    if terms[1] == "+":
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) + decimal.Decimal(terms[2])}"

    if terms[1] == "-":
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) - decimal.Decimal(terms[2])}"

    if terms[1] == "*":
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) * decimal.Decimal(terms[2])}"

    if terms[1] == "/":
        if decimal.Decimal(terms[2]) == 0: return f"{equation.strip()} = undefined"
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) / decimal.Decimal(terms[2])}"

    if terms[1] == "^":
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) ** decimal.Decimal(terms[2])}"

    if terms[1] == "r":
        if decimal.Decimal(terms[0]) < 0: return f"{equation.strip()} = {equation.strip()}"
        return f"{equation.strip()} = {decimal.Decimal(terms[0]) **  (decimal.Decimal(1) / decimal.Decimal(terms[2]))}"

    return "Error: Please enter an Equation!"

if __name__ == "__main__":
    print("WELCOME TO THE ARITHEMIC CALCULATOR BY NOOB UNDONE!")
    counter = 1
    while True:
        inp = input("Input an Problem: ")
        if not inp: break
        history.append(inp)
        print('\033[1A', end="\033[2K")
        print(f"{counter}.) {main(inp)}")
        counter += 1
    print("THANK YOU FOR USING THE PROGRAM!")