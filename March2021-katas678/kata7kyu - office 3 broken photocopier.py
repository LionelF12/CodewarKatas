inp = '001111110011001110101111101001'
def broken(inp):
    return inp.replace('0','2').replace('1','0').replace('2','1')

print(broken(inp))