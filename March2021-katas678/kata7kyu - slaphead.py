s = '------/-/----'

def bald(s):
    hairdic = {0:'Clean!',1:'Unicorn!',2:'Homer!',3:'Careless!',4:'Careless!',5:'Careless!'}
    
    if s.count('/') > 5:
        return [s.replace('/','-',),'Hobo!']
    else:
        return [s.replace('/','-'),hairdic[s.count('/')]]

print(bald(s))

""" def bald(s):
    count = 0 
    lis = list()
    for hair in s:
        if hair == '/':
            count += 1
            s = s.replace(hair,'-',1)
    if count == 0:
        remark = 'Clean!'
    elif count == 1:
        remark = 'Unicorn!'
    elif count == 2:
        remark = 'Homer!'
    elif count >= 3 and count <=5:
        remark = 'Careless!'
    elif count > 5:
        remark = 'Hobo!'
    lis.append(s)
    lis.append(remark)
    return lis
print(bald(s)) """