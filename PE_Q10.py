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
def Q10_v1(n):
    """n 미만인 모든 소수의 합"""
    ans=2
    i=3
    while i<n:
        if is_prime(i):
            ans+=i
        i+=2
    return ans

def Q10_v2(n):
    """에라토스테네스 체"""
    if n<3:
        return 0
    ans=2
    sieve=[1]*n
    sieve[0],sieve[1]=0,0
    for mul in range(4,n,2):
        sieve[mul]=0
    for div in range(3,int(n**0.5)+1,2):
        if sieve[div]:
            ans+=div
            for mul in range(div*2,n,div):
                sieve[mul]=0
    for i in range(int(n**0.5)+1,n):
        if sieve[i]:
            ans+=i
    return ans
if __name__=="__main__":
    print(Q10_v2(12))
