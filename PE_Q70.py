from sympy import totient
from collections import Counter
def is_permutation(a,b):
    return Counter(str(a))==Counter(str(b))
def is_prime(n):
    if n==2:
        return True
    elif not n%2 or n==1:
        return False
    for div in range(3,int(n**0.5)+1,2):
        if not n%div:
            return False
    return True
def Q70_v1():
    m=float('inf')
    res=0
    for i in range(2,10**7):
        if is_prime(i):
            phi=i-1 #Euler's phi(totient) func
        else:
            phi=totient(i)
        if is_permutation(i,phi):
            ratio=i/phi
            if ratio<m:
                m=ratio
                res=i
    return res
print(Q70_v1())

from sympy import primerange, totient
def Q70_v2(n):
    min_ratio = float('inf')
    result = 0
    for n in primerange(2, n):
        phi = totient(n)
        if sorted(str(n)) == sorted(str(phi)):
            ratio = n / phi
            if ratio < min_ratio:
                min_ratio = ratio
                result = n
    return result
print(Q70_v2(10**7))
                
