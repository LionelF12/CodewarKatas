rooms = ['X','X','X','X']
def meeting(rooms):
    if 'O' not in rooms:
        return 'None available!'
    else: 
        for index,value in enumerate(rooms):
            if value == 'O':
                return index

print(meeting(rooms))
