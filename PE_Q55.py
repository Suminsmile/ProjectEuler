#Lychrel numberes
def is_lychrel(n): 
    """라이크렐 수: 수를 뒤집어서 더하는 과정을 통해 대칭수를 만들 수 없는 수"""
    for i in range(49):
        n+=int(str(n)[::-1])
        if str(n)==str(n)[::-1]:
            return False
    return True
def Q55_v1(): 
    """10,000 미만, 라이크렐 수 갯수"""
    ans=0
    for i in range(5,10000):
        if is_lychrel(i):
            ans+=1
    return ans
print(Q55_v1())