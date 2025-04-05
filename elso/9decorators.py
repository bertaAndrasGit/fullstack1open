import functools

user = {"username": "andrew","access_level": "admin"}


def secure_get_admin():
    if user["access_level"] == "admin":
        return 12345

#decoratorban így nézne ki
def make_secure(func):
    #ez a decorator nélkül a print(get_admin_password.__name__) a secure_function()-t adná vissza
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function



@make_secure
def get_admin_password():
    return "12345"


print(get_admin_password())
print(get_admin_password.__name__)

print("\n")

def make_secure2(func):
    #ez a decorator nélkül a print(get_admin_password.__name__) a secure_function()-t adná vissza
    @functools.wraps(func)
    #*args **kwargs okat rakonk ide, hogy ha az eredeti function ba is lehetne írni paramétert akkor a decorator is elfogadja
    def secure_function2(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args,**kwargs)

    return secure_function2

@make_secure2
def get_password(panel):
    if panel == "admin":
        return "12345"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))


print("\n")

def decorator(access_level):
    def make_secure3(func):
        #ez a decorator nélkül a print(get_admin_password.__name__) a secure_function()-t adná vissza
        @functools.wraps(func)
        #*args **kwargs okat rakonk ide, hogy ha az eredeti function ba is lehetne írni paramétert akkor a decorator is elfogadja
        def secure_function3(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args,**kwargs)

        return secure_function3

    return make_secure3


@decorator("admin")
def get_admin_password2():
    return "admin: 12345"

@decorator("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password2())
print(get_dashboard_password())