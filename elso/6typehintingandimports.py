from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)

print(list_avg([1,2,3,4,5]))

class Book:
    pass

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __repr__(self) -> str:
        return f"Bookshelf with {len(self.books)} books"


print("\nIMPORTS\n")

def divide(dividend,divisor):
    return dividend/divisor

print(f"mymodule.py: {__name__}")

print("\nRELATIVE IMPORTS\n")


