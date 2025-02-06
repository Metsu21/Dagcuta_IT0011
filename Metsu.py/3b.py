num = 1
count = 1
while num <= 7:
    spaces = 1
    while spaces <= 7 - count:
        print(" ", end="")
        spaces += 1
    
    print(str(num) * (2 * count - 1))
    
    num += 2
    count += 1