import math
def is_square(n):
    s=int(math.sqrt(n))
    return s**2==n
def min_x(D):
    """주어진 D에 대해 x^2-Dy^2=1 의 최소 해 x"""
    if is_square(D):
        return None
    m,d,a=0,1,int(math.sqrt(D))
    num1,num,den1,den=1,a,0,1
    while num**2-D*den**2 != 1:
        m=d*a-m
        d=(D-m**2)//d
        a=(int(math.sqrt(D))+m)//d
        num2=num1
        num1=num
        den2=den1
        den1=den
        num=a*num1+num2
        den=a*den1+den2
    return num
def Q66_v1():
    max_x=0 
    result=0 #가장 큰 x를 갖는 D 값
    for D in range(2,1001):
        x=min_x(D)
        if x is not None and x>max_x:
            max_x=x
            result=D
    return result
print(Q66_v1())