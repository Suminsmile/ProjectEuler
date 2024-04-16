from itertools import permutations as permu
def is_prime(n):
    """n이 소수이면 True 반환"""
    if n==2:
        return True
    elif not n%2 or n==1:
        return False
    for div in range(3,int(n**0.5)+1,2):
        if not n%div:
            return False
    return True
def Q41_v1():
    """소수이면서 가장 큰 팬디지털 수"""
    digits="987654321"
    for i in range(9):
        pandigitals=permu(digits[i:])
        for pandi in pandigitals:
            if pandi[-1] in ("2","4","5","6","8"):
                continue
            num=int(''.join(pandi))
            if is_prime(num):
                return num
print(Q41_v1())