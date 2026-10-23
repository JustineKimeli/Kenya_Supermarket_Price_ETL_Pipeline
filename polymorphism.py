# ======================
# POLYMORPHISM
# ========================

# from abc import ABC, abstractmethod
# class AbstractShape(ABC):
#     @abstractmethod
#     def perimeter(self):
#         # this becomes a placeholder , any class that is built from the AbstractShape must provide its own perimeter method
#         pass
# class Circle2(AbstractShape):
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         return 2 * 3.142 * self.radius

# class Square2(AbstractShape):
#     def __init__(self, side):
#         self.side = side

#     def perimeter(self):
#         return self.side * 4

# shapes = [Circle2(radius = 8), Square2(20)]

# for shape in shapes:
#     print(f"{shape.perimeter()} cm")


# Duck typing 
class Animalia:
    alive = True

class Kitten(Animalia):
    def speak(self):
        print("Miaauuuu")

class Puppy(Animalia):
    def speak(self):
        print("Wuuuuuff")

class Car:
    alive = False
    
    def speak(self):
        print("Vruuuuuuuum")

animals = [Kitten(), Puppy(), Car()]

for animal in animals:
    animal.speak()


# magic methods ,,, dunder(double underscore) methods
# they start with a __
# python calls them under the hood
# they include everyday perators like +, ==, <, > , str() 
# common magic methods 
# __init__ runs when an object is created 
# __str__ runs when you print an object
# __eq__ runs when you use  == to compare something
# __lt__ / __gt__ runs when you use  > or <
# __add__ runs when you use +
# _contains_ runs when you use "in"

class Book:
    def __init__(self, author,title, num_pages):
        self.author = author
        self.title = title
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
         if key == "title":
              return self.title
         elif key == "author":
              return self.author
         elif key == "num_pages":
              return self.num_pages
         else:
              return f"Key {key} was not found."



book1 = Book(author = "Yano", title = "Think and grow rich", num_pages = 300)
book2 = Book(author = "Melly", title = "Be your own boss", num_pages = 214)

print(book1)
print(book1 == book2)
print(book1 > book2)
print(book1 + book2)
print("Think" in book1)
print(book1["author"])
print(book2["author"])

book = {"Things fall apart" : "Chinua Achebe"}
print(book.get("Things fall apart"))