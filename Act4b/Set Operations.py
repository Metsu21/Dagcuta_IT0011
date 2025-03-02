A = {'a', 'g', 'b', 'c', 'd', 'f'}
B = {'l', 'm', 'o', 'b', 'c', 'h', 'i', 'j'}
C = {'k', 'c', 'h', 'i', 'j', 'd', 'f'}

print("1(a):", len(A & B))
print("1(b):", len(B - (A | C)))
print("1(c)(i):", C - A)
print("1(c)(ii):", A & C)
print("1(c)(iii):", ((B & A) | (B & C)) - {'i','j'})
print("1(c)(iv):", (A & C) - B)
print("1(c)(v):", A & B & C)
print("1(c)(vi):", B - (A | C))
