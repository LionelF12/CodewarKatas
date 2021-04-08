def pyramid(balls):
    ballsreq = []
    for x in range(1,999):
        if x == 1:
            ballsreq = [1]
        else:
            ballsreq.append(ballsreq[x-2]+x)
    
    count = 0   
    for y in ballsreq:
        count = count + 1
        if balls < y:
            ind = count - 1
            return ind

print(pyramid(6))