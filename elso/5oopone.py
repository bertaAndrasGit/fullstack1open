# a function inside a class is called a method!!
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = (100,90,89,85,95)

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old."

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def average_grade(self):
        return sum(self.grades)/len(self.grades)

class ClassTest:
    #instance methods needs an instance to call them
    def instance_method(self):
        print(f"Called instance_method of {self}")

    #classmethods don't need instance,you can just call ClassTest.class_method()
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    #it is a separate function that is in a class.
    def static_method():
        print("called static method")



student = Student("Bob",25)
print(student)
print(student.__repr__())
print(student.name)
print(student.average_grade())

print("\n")

test = ClassTest()
test.instance_method()
ClassTest.class_method()
ClassTest.static_method()

print("\n")


class Book:
    #if you place a variable in class it became class propertie
    TYPES = ("hardcover","paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book: {self.name}, type: {self.book_type}, weight: {self.weight}"

    @classmethod
    def hardcover(cls,name,page_weight) -> "Book": # <- ha azon belül a classon belül akarsz typehintelny egy ugyan olyan classra akkor használni kell a ""-möt
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls,name,page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Cats",100)
book1 = Book.paperback("Cats",100)
print(book)
print(book1)
print(book.name)
print(Book.TYPES)

print(f"\n{("inheritance").upper()}\n")

class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device({self.name},{self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}, {self.remaining_pages} pages remaining"

    def print(self,pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages. ")
        self   .remaining_pages -= pages


printer = Printer("MyPrinter","USB",500)
printer.print(50)
print(printer)

printer.disconnect()
printer.print(50)

print(f"\n{("composition").upper()}\n")

class BookShelf:
    def __init__(self,*books):
        self.books = books

    def __repr__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Book name: {self.name}"


book = Book("Cats")
book1 = Book("Cats2")
shelf = BookShelf(book,book1)

print(shelf)
print(shelf.books[0])