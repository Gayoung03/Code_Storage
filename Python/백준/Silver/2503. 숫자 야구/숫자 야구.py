from itertools import permutations
candidates = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))


N=int(input())

for _ in range(N):
    num,st,b = map(int,input().split(" "))
    passlist=[]
    numstr = str(num)

    for candidate in candidates:
        tst = 0
        tb=0
        

        for i in range(3):
            if numstr[i] == candidate[i]:
                tst +=1
            elif numstr[i] in candidate:
                tb+=1
        
        if tst == st and tb == b:
            passlist.append(candidate)

    candidates = passlist
        
print(len(candidates))

