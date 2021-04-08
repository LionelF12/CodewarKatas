def stringy(size):
    count = 0
    size = int(size)
    for i in range(size):
        count = count + 1
    if count == 1:
        z = '1'
    elif count%2 == 0:
        z = '10'*int(count/2)
    elif count%2 != 0:
        z = '1' + '01'*int((count/2))
    return str(z)

print(stringy(input('input: ')))
