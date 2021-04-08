arr = ([-52,56,30,29,-54,0,-110])
def minimum(arr):
    x = None
    for i in arr:
        if x == None:
            x = i
        elif x > i:
            x = i
    return x

def maximum (arr):
    y = None
    for j in arr:
        if y == None:
            y=j
        elif y < j:
            y = j
    return y

print(maximum(arr))
print(minimum(arr))
