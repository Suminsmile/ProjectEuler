#Square root convergents
def Q57_v1(): #2의 제곱근을 연속 분수로 표현 시, (분자의 자릿수)>(분모의 자릿수)인 분수의 개수
    ans=0
    d,n=2,3
    ans=0
    for i in range(1000):
        if len(str(n))>len(str(d)):
            ans+=1
        d,n=d+n,2*d+n
    return ans
print (Q57_v1())