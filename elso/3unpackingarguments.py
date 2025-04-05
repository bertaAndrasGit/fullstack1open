def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1,2))
print(multiply(1,2,3,4,5))


def add(x,y):
    return x + y

nums = {"x": 5, "y":5}
#a ** kiszedi az értékeket a dict-ből
print(add(**nums))


def apply(*args,operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        print("no other options outside * or +")

print("")
print(apply(1,2,3,4,5,operator="*"))