def solution(name, yearning, photo):
    answer = []
    
    dic1 = dict(zip(name, yearning))
    
    for i in photo:
        total = 0 
        for j in i:
            if j in dic1:
                total+= dic1[j]
                
        answer.append(total)
    
    return answer