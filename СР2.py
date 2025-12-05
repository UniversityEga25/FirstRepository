n = list(map(int, input().split()))
a = []
b = []
c = []
for i in range(len(n)):
    if n[i] == 0:
        a.append(n[i])
    if n[i] > 0:
        b.append(n[i])
    if n[i] < 0:
        c.append(n[i])
n = []
for i in range(len(c)):
    n.append(c[i])
for i in range(len(a)):
    n.append(a[i])
for i in range(len(b)):
    n.append(b[i])
print(n)


