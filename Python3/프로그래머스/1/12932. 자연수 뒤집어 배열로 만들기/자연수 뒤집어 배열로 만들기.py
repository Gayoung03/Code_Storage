def solution(n):
    answer = []
    
    strn=str(n)
    restrn = strn[::-1]
    
    answer = list(map(int,restrn))
    return answer