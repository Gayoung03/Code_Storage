def solution(x):
    answer = True
    list1 = []
    
    for i in str(x):
        list1.append(int(i))
    
    l = sum(list1)
    
    if x%l==0:
        return True
    else:
        return False
    
    
    return answer