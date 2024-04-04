def Q34_v1():
    factorial=(1,1,2,6,24,120,720,5040,40320,362880)
    limits=((100,700),(1000,7200),(10000,90000),(1000000,2540160))
    answer=[]
    for low,high in limits:
        for num in range(low,high):
            digits=[int(d) for d in str(num)]
            if sum([factorial[d] for d in digits])==num:
                answer.append(num)
    return sum(answer)                