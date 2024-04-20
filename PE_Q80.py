import math
from decimal import Decimal,localcontext
def digits(n):
    return sum(int(i) for i in str(n))
def is_square(n):
    return int(n**0.5)**2==n
def isqrt(n):
    x=n
    y=(x+1)//2
    #두 추정치가 수렴할 때까지 반복
    while y<x:
        x=y
        y=(x+n//x)//2
    return x #수렴한 값 반환, Newton-Raphson Method

def Q80_v1():
    result=0
    for i in range(2,100):
        if not is_square(i):
            result+=digits(isqrt(i*(10**198)))
    return result
print(Q80_v1())
def Q80_v2():
    return sum(digits(int(math.sqrt(i)*(10**99))) for i in range(2,100) if not is_square(i))
print(Q80_v2())       
def Q80_v3():
    res=0
    for i in range(1,100):
        with localcontext() as ctx:
            ctx.prec=105 #소수점 이하 정밀도 105로 설정
            if len(str(Decimal(i).sqrt()))==1:
                res+=0
            else:
                a=sum([int(j) for j in str(Decimal(i).sqrt())[2:101]]) 
                b=int(str(Decimal(i).sqrt())[0])
                res+=a+b
    return res
print(Q80_v3())