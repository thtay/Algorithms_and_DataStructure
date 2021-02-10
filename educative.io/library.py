# from abc import ABC
# from enum import Enum


# class Book:
#     def __init__(self, title, author, isbn):
#         self.tilte = title
#         self.author = author
#         self.isbn = isbn


# class Person(ABC):
#     def __init__(self, name, address, email, phone):
#         self.name = name
#         self.address = address
#         self.email = email
#         self.phone = phone


# class Address:
#     def __init__(self, street, name, phone):
#         self.street = street
#         self.name = name
#         self.phone = phone


# class BookStatus(Enum):
#     AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


from collections import namedtuple
from typing import NamedTuple


class Employee(NamedTuple):
    name: str
    id: int = 3


employee = Employee("Guido")
assert employee.id == 3