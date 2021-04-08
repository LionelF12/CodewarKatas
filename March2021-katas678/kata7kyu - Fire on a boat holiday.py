s = "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast"

def fire_fight(s):
    newlist = []
    words = s.split()
    for word in words:
        if word != 'Fire':
            newlist.append(word)
        else:
            word = word.translate(word.maketrans('Fire','~~  ')).strip()
            newlist.append(word)
    s = ' '.join(newlist)
    return s

print(fire_fight(s))

#def fire_fight(s):
#    return s.replace('Fire','~~')