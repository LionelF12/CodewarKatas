#def super_size(n):
#    spl = list(str(n)
#    spl.sort(reverse=True)
#    for i in spl:
#        final += i
#    return int(final)


def super_size(n):
    spl = list(str(n))
    spl.sort(reverse=True)
    final = (''.join(spl))
    return int(final)