items = [12, 14, 63, 72, 55, 24]

def inverse_slice(items, a, b):
    remove = items[a:b]
    print(remove)
    for item in remove:
        if item in items:
            items.remove(item)
    return items


#def inverse_slice(items, a, b):
#    del items[a:b]
#    return items
print(inverse_slice(items,2,4))

