N = int(input())

for _ in range(N):
    s = int(input())

    for i in range(2,1000000+1):
        if s % i == 0:
            print("NO")
            break
        if i == 1000000: # i가 10^6까지 됐다는 건 그 전에 인수가 없었다는 거니까
            print("YES")
    