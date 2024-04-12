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
def Q7_v1(n):
    """n번 항의 소수"""
    if n==1:
        return 2
    count,num=1,3
    while True:
        if is_prime(num):
            count+=1
            if count==n:
                return num
        num+=2
if __name__=="__main__":
    for i in range(1,11):
        print(f"{i:2}번 항의 소수: {Q7_v1(i):3}")
    print(Q7_v1(10001))