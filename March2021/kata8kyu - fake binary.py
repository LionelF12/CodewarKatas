def fake_bin(x):
    index = 0
    lis = list(x)
    for z in lis:
        if int(z) < 5:
            lis[index] = '0'
        else: 
            lis[index] = '1'
        index += 1
    return ''.join(lis)