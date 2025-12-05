def Longestword(s):
    LongWord = s[0]
    for i in range(len(s)):
        if len(s[i]) > len(LongWord):
            LongWord = s[i]
    return LongWord

n = list(map(str, input().split()))
print(Longestword(n))