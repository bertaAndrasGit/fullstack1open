def named(**kwargs):
    print(kwargs)

#**kwargs collect named arguments ("or can strip dictionaries")
named(name="Bob",age=25)

details = {"name":"Alice","age":25}
named(**details)

print("")

def print_nicely(**kwargs):
    named(**kwargs)
    for arg,value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age = 25)


