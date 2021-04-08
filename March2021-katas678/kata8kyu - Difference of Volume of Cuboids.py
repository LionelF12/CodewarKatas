def find_difference(a, b):
    vol1 = a[0]*a[1]*a[2]
    vol2 = b[0]*b[1]*b[2]
    if vol1 > vol2:
        result = vol1-vol2
    else:
        result = vol2-vol1
    return result


#def find_difference(a, b):
#    return abs((a[0]*a[1]*a[2])-b[0]*b[1]*b[2])