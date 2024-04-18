from collections import Counter
def factors_count(n):
    factors=[]
    i=2
    while n>1:
        while n%i==0:
            factors.append(i)
            n//=i
        i+=1
    return len(set(factors))
def Q69_v1():
    max_factors=0
    result=0
    for i in range(2,10**6+1):
        coun=factors_count(i)
        if coun>max_factors:
            max_factors=coun
            result=i
    return result
print("가장 많은 소인수를 갖는 수:", Q69_v1())
from sympy import factorint
def Q69_v2():
    max_coun=0
    res=0   
    for i in range(2,10**6):
        fact=factorint(i)
        if len(fact)>max_coun:
            max_coun=len(fact)
            res=i
    return res
print(Q69_v2())