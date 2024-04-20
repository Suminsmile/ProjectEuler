def phi(n):
    res=n
    p=2
    while p**2<n:
        if n%p==0:
            while n%p==0:
                n//=p
            res-=res//p
        p+=1
    if n>1:
        res-=res//n
    return res
def Q72_v1():
    s=0
    for i in range(2,10**6+1):
        s+=phi(i)
    return s
print(Q72_v1())

def Q72_v2(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return sum(phi) - 1

print(Q72_v2(10 ** 6))
