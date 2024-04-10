#Spiral primes
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def Q58_v1(): #소용돌이 수에서 대각선에 있는 소수와 홀수의 비율이 10% 미만인 변의 길이
    i,step=1,0
    odd,prime=1,0
    while True:
        odd+=4
        step+=2
        last=(step+1)**2
        for j in range(3):
            last-=step
            if is_prime(last):
                prime+=1
        if (prime/odd)<0.1:
            return step+1
        i+=1
print(Q58_v1())