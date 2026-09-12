from typing import List

def read_integers() -> List[int]:
    emptlst = []
    Input = input()
    splitinput = Input.split(",")
    for inpts in splitinput:
        innie = int(inpts)
        emptlst.append(innie)
    return emptlst

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
