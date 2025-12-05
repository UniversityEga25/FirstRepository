def CursedSum(a, b):
    if b == 0:
        return a
    return CursedSum(a + 1, b - 1)

a = int(input())
b = int(input())
print(CursedSum(a, b))