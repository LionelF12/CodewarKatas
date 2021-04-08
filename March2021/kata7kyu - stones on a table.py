stones = 'RRRRGGGGBBBB'
def solution(stones):
    pos = 0 
    count = 0 
    for x in range(len(stones)):
        try:
            if stones[pos] == stones[pos+1]:
                count += 1
        except:
            continue
        pos += 1
    return(count)

print(solution(stones))