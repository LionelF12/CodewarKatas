string = 'helloooooo hi hi'
def find_longest(string):
    spl = string.split(" ")
    longest = ' '
    
    for i in spl:
        if (len(i) >= len(longest)): 
            longest = i
    return len(longest)

print(find_longest(string))