def solution(absolutes, signs):
    result = 0
    num = 0
    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[num]
        else:
            result += (absolutes[num]*-1)
        num+=1
        print(result)
    
    return result