N = int(input())
result = 0
'''
a >= b+2
c%2 !=0
a>0, b>0, c>0
'''

for A in range(N+1):
    for B in range(N+1):
        for C in range(N+1):
            if A+B+C == N:
                if A>=B+2:
                    if A!=0 and B !=0 and C !=0:
                        if C %2 ==0:
                            result+=1
print(result)