def add_two_numbers() -> int:
    z = []
    a = input()
    b = a.split(",")
    for bs in b:
        c = int(bs)
        z.append(c)
    
    return sum(z)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
