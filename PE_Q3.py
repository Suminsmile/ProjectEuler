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
if __name__=="__main__":
    for i in range(2,20):
        if is_prime(i):
            print(i,end=" ")