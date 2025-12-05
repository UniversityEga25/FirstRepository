import random
def task(s):
    maxs = s[0] + s[1]
    maxn = 0
    for i in range(len(s) - 1):
        if maxs <= s[i] + s[i + 1]:
            maxs = s[i] + s[i + 1]
            maxn = i + 1
    return [maxn, maxn + 1]

def classic():
    n = int(input())
    a, b = map(int, input().split())
    s = n * [0]
    for i in range(n):
       s[i] = random.randint(a, b)
    print("Изначальный список:", s)
    print(task(s))

def test():
    s = list(map(int, input().split()))
    print(task(s))

def autotest():
    s = [1, 2, 3]
    res = [2, 3]
    n = (task(s))
    print("Список:", s, "    Полученный результат", n, "    Необходимый результат", res, "    Тест:", res == n)
    if res != n:
        return
    s = [10, 10, 10]
    res = [2, 3]
    n = (task(s))
    print("Список:", s, "    Полученный результат", n, "    Необходимый результат", res, "    Тест:", res == n)
    if res != n:
        return
    s = [-1, -2, -3]
    res = [1, 2]
    n = (task(s))
    print("Список:", s, "    Полученный результат", n, "    Необходимый результат", res, "    Тест:", res == n)
    if res != n:
        return
    s = [-1, 2, 0, 1, -2]
    res = [2, 3]
    n = (task(s))
    print("Список:", s, "    Полученный результат", n, "    Необходимый результат", res, "    Тест:", res == n)
    if res != n:
        return

a = int(input("1 - Классический(Рандом), 2 - Ручной тест, 3 - Автотест: "))
if a == 1:
    classic()
if a == 2:
    test()
if a == 3:
    autotest()