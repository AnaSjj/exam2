# Class: Book
# Objective: Create a `Book` class that has two attributes: `title` and `author`.
# The class should also have two methods:
# - `get_title()`: Returns "Title: " followed by the instance title.
# - `get_author()`: Returns "Author: " followed by the instance author.

class Book:
    pass

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

# Examples of attributes and methods:
print(PP.title)  # Expected: "Pride and Prejudice"
print(PP.author)  # Expected: "Jane Austen"
print(PP.get_title())  # Expected: "Title: Pride and Prejudice"
print(PP.get_author())  # Expected: "Author: Jane Austen"

print(H.title)  # Expected: "Hamlet"
print(H.author)  # Expected: "William Shakespeare"
print(H.get_title())  # Expected: "Title: Hamlet"
print(H.get_author())  # Expected: "Author: William Shakespeare"

print(WP.title)  # Expected: "War and Peace"
print(WP.author)  # Expected: "Leo Tolstoy"
print(WP.get_title())  # Expected: "Title: War and Peace"
print(WP.get_author())  # Expected: "Author: Leo Tolstoy"