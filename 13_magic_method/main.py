## Magic Methods: Dunder Methods (Double underscore) __init__, __str__, __eq__.
    ## They are automatically called by many Python built-in operations.
    ## They allow developers to define or customize the behaviours


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages}"
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        return f"Key {key} not found"

book1 = Book("Harry Potter", "J. K. Rowlings", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 240)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 240)


print(book1)
print(book2)
print(book3 == book2)
print(book3 == book1)
print(book1 < book2)
print(book2 > book3)
print(book1 + book2)

print("Hobbit" in book1)
print("Hobbit" in book2)

print(book1["num_pages"])
print(book2["director"])