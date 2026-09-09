from typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:
    t1 = (name, age)
    t2 = tuple(t1)
    return t2

# do not modify code below this line
print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))
