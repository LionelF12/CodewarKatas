def add_length(str_):
    x = str_.split(' ')
    pos = 0
    newarr = []
    for i in x:
        count = str(len(i))
        newarr.insert(pos,i + " " + count)
        pos = pos + 1
    return newarr

print(add_length('apple ban'))