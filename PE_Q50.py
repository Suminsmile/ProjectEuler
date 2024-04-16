def sieve(n):
    sie=[1]*(n+1)
    sie[0],sie[1]=0,0
    for i in range(2,int(n**0.5)+1):
        if sie[i]==1:
            m=i*2
            while m<=n:
                sie[m]=0
                m+=i
    return sie
def primes(sie,n):
    """에라토스테네스의 체 이용, n 이하 소수 리스트"""
    pri=[]
    for i in range(2,n+1):
        if sie[i]==1:
            pri.append(i)
    return pri
def Q50_v1(n):
    """n 이하 소수, 가장 길게 더해서 얻을 수 있는 소수"""
    ans=(0,0)
    sie=sieve(n)
    pri=primes(sie,n//2)
    length=len(pri)
    for i in range(length-1):
        end=i
        total=pri[end]
        if total==2:
            end+=1
            total+=pri[end]
        while total<=n:
            count=end-i+1
            if sie[total]==1 and count>ans[1]:
                ans=(total,count)
            if (end+2)>=length:
                break
            total+=pri[end+1]+pri[end+2]
            end+=2
    return ans
print(Q50_v1(1000000))