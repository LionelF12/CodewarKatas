a = '20B'
def plane_seat(a):
    try:
        int(list(a)[1])
        num = int(list(a)[0]+list(a)[1])
        let = str(list(a)[2])
    except:
        num = int(list(a)[0])
        let = str(list(a)[1])

    if num >= 1 and num <= 20:
        section = 'Front'
    elif num > 20 and num <= 40:
        section = 'Middle'
    elif num > 40 and num <= 60:
        section = 'Back'
    else:
        print('No Seat!!')
        exit()

    if let in ['A','B','C']:
        row = 'Left'
    elif let in ['D','E','F']:
        row = 'Middle'
    elif let in ['G','H','K']:
        row = 'Right'
    else:
        print('No Seat!!')
        exit()
    
    return section+'-'+row

print(plane_seat(a))