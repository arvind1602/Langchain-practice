from typing import TypedDict,  Required

class Person(TypedDict) :
    name : Required[str]
    age : Required[int]

person : Person = {"name" : "arvind", "age" : 23} 

print(person["name"])