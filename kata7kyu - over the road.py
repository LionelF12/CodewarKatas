def over_the_road(address, n):
    left = []
    right = []
    for i in range(1,n+1):
        left.append(str(2*i-1))
        right.append(str(2*i))
    right.reverse()
    print(left)
    print(right)
    if str(address) in left:
        addressloc = left.index(str(address))
        result = right[addressloc]
    else: 
        addressloc = right.index(str(address))
        result = left[addressloc]
    return result

print(over_the_road(6,10))


#def over_the_road(address, n):
#    address = int(address)
#    n = int(n)
#    if address%2 == 0: #if even
#        return 2*n - address + 1
#    else: 
#        return -(address+1) + (2*n+2)
#print(over_the_road(6,10))


