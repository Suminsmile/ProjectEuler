#Prime_pair_sets
def sieve(n):
    sie=[1 for i in range(n)]
    sie[0],sie[1]=0,0
    i=4
    while i<n:
        sie[i]=0
        i+=2
    for i in range(3,int(n**0.5)+1,2):
        if sie[i]==1:
            multi=2
            while (m:=i*multi)<n:
                sie[m]=0
                multi+=1
    return sie
sie=sieve(1000000)
def is_prime(n):
    if n<1000000:
        return sie[n]==1
    if n%2==0 or n%3==0:
        return False
    for div in range(5,int(n**0.5)+1,2):
        if n%div==0:
            return False
    return True
def prime_pair(p1_list,p2):
    p2_str=str(p2)
    for p1 in p1_list:
        p1_str=str(p1)
        pair1=int(p1_str+p2_str)
        pair2=int(p2_str+p1_str)
        if not is_prime(pair1) or not is_prime(pair2):
            return False
    return True
def Q60_v1():
    """임의의 두 소수 연결, 다른 소수 만들 수 있는 소수 다섯 개의 집합 중 가장 작은 합"""
    primes=[3,7]
    for i in range(11,10000,2):
        if sie[i]==1:
            primes.append(i)
    l=len(primes)
    i=0
    while True:
        p1=primes[i]
        for j in range(i+1,l-3):
            p2=primes[j]
            if not prime_pair([p1],p2):
                continue
            for k in range(j+1,l-2):
                p3=primes[k]
                if not prime_pair([p1,p2],p3):
                    continue
                for m in range(k+1,l-1):
                    p4=primes[m]
                    if not prime_pair([p1,p2,p3],p4):
                        continue
                    for n in range(m+1,l):
                        p5=primes[n]
                        if prime_pair([p1,p2,p3,p4],p5):
                            return (p1,p2,p3,p4,p5)
        i+=1
    return
print(Q60_v1())