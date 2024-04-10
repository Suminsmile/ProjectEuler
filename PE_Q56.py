#Powerful digit sum
def Q56_v1():
    ans=0
    for a in range(2,100):
        for b in range(2,100):
            if not a%10:
                break
            digit_sum=sum([int(n) for n in str(a**b)])
            ans=max(ans,digit_sum)
    return ans
print(Q56_v1())
    