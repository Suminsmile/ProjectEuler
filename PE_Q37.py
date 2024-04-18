#Truncatable_primes
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
def make_primes(n,res):
    """n이 소수가 아닐 때까지 숫자 추가한 수의 목록"""
    if not is_prime(n):
        return
    if n>10:
        res.append(n)
    prefix=n*10
    for i in (prefix+i for i in (1,3,7,9)):
        make_primes(i,res)
    return res

def Q37_v1():
    """Truncatable prime 11개 찾고, 그의 합"""
    ans=[]
    for i in (2,3,5,7):
        ans+=make_primes(i,[])
    for i in ans[:]:
        div=10 
        while div<i:
            q,r=divmod(i,div)
            if not is_prime(q) or not is_prime(r):
                ans.remove(i)
                break
            div*=10
    return (ans,sum(ans))
if __name__=="__main__":
    print(Q37_v1())
        