def count_sheep(n):
    try:
        int(n)
    except: 
        return 'enter a number pls'
        
    result = ''
    i = 1
    while i <= int(n):
        result = result + (str(i)+' '+ 'sheep...')
        i = i + 1
    return result


sheepnumb = input('Enter how many sheeps you would like to dream off tonight: ')

print(count_sheep(sheepnumb))