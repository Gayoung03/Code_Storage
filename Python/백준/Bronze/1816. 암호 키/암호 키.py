S = int(input())

for _ in range(S):
    num = int(input())
    
    for j in range(2,1000000+1):
        if num % j == 0:
            print("NO")
            break
        if j == 1000000:
            print("YES")