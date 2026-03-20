N = int(input())
result = 0
'''
a,b,c에 들어갈 수 있는 숫자는 각각 0부터 6임(조건을 무시하고)
그래서 일단 반복문으로 다 연결함

각각의 조건을 나열함
이걸 만족한다면? 그 다음에 이것도 만족한다면? 또 이것도 만족한다면? -> 원하는 조합이다!!
result의 갯수 올리기
'''
for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a+b+c == N:
                if a >= b+2:
                    if a !=0 and b!=0 and c!=0:
                        if c%2 ==0:
                            result+=1

print(result)