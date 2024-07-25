def add(n1, n2):
    """ Addieren die beiden Nummer"""
    return n1 + n2


def subtract(n1, n2):
    """subtrahieren die beiden Nummer"""
    return n1 - n2


def multiply(n1, n2):
    """multipilzieren die beiden Nummer"""
    return n1 * n2


def divide(n1, n2):
    """dividieren die beiden Nummer"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("Geben Sie die erste Nummer ein: "))

for operation in operations:
    print(operation)
operation_symbol = input("Wählen Sie ein Operator aus: ")

num2 = int(input("Geben Sie die zweite Nummer ein: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")