def eratos(n):
    """에라토스테네스의 체, n 미만 소수 리스트 반환"""
    sieve=[1]*n
    sieve[0],sieve[1]=0,0
    for i in range(4,n,2):
        sieve[i]=0
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]==1:
            for j in range(i*2,n,i):
                sieve[j]=0
    return sieve
def circular(n):
    """n 각 숫자 좌측으로 한 칸씩 이동, 원형 수"""
    cir_num=[]
    s=str(n)
    for i in range(len(s)-1):
        s=s[1:]+s[0]
        cir_num.append(int(s))
    return cir_num
def Q35_v1(n):
    primes=eratos(n)
    for i in range(2,n):
        if not primes[i]:
            continue
        cir_num=circular(i)
        if not cir_num:
            continue
        for j in cir_num:
            if primes[j]==0:
                primes[i]=0
    return sum(primes)

if __name__=="__main__":
    print(f"{100} 미만의 원형 소수 개수: {Q35_v1(100)}")
