def computePrefix(P):
    m = len(P)
    prefList = [0] * m
    i = 0
    for j in range(1, m):
        while i > 0 and P[i] != P[j]:
            i = prefList[i-1]
        if P[i] == P[j]:
             i = i+1
        # else:
        #     i = 0
        prefList[j] = i
    return prefList



def KMP(T,P, prefList):
    
    i = 0
    j = 0
    n = len(T)
    m = len(P)
    if n < m:
        return -1

    while i<n:
        if P[j] == T[i]:
            if j == m-1:
                return i-m+1
            i = i + 1 
            j = j + 1
        elif j>0:
            j = prefList[j-1]
        else:
            i = i+1
    return -1


pattern = "acacabacacabacacac"
text = "acacabacacabacacadaxswdacacacacabacacabacacac"
aaaa = computePrefix(pattern)
print(aaaa)
print(KMP(text,pattern,aaaa))
print(text[27:])




