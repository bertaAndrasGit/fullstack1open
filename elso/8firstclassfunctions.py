def divide(dividend,divisor):
    if divisor ==0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values,operator):
    return operator(*values)

#a function-t argumentként is átadhatom csak () nélkül kell tenni azt
result = calculate(20,4, operator=divide)