n = 111
k = 2

def strange_math(n, k):
    return sorted(range(0,n+1), key = str).index(k)

print(strange_math(n,k))