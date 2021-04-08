army_letters = 'dhnkfu'
army_numbers = '18386' #answer is 'dcc'

def battle_codes(army_letters, army_numbers):
    army_letters = list(army_letters)
    army_numbers = list(army_numbers)

    if len(army_letters) == 0 or len(army_numbers) == 0:
        return 'Peace'
    #create letter power catalogue#
    letdict = dict()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in alphabet:
        pos = alphabet.index(letter)
        letdict[letter] = letdict.get(letter,pos)+1
    ###print(letdict)
    while len(army_numbers) > 0 and len(army_letters) > 0:
        #define attacking letters and numbers, & defending letters
        attletter = army_letters[-1]               
        attletpow = letdict[attletter]
        deflet = army_letters[-2:]                  
        print('attletter',attletter,'attletpow',attletpow,'deflet',deflet)
        attnum = army_numbers[0]
        attnumpow = int(attnum)
        print('attnum',attnum,'attnumpow',attnumpow)         

        #resolve letter attacking number 
        remnumhp = attnumpow - attletpow
        print('attletpow: ',attletpow)
        if remnumhp <= 0:
            army_numbers.remove(attnum)
        else:
            army_numbers[0] = remnumhp
        print('armynumbersleft: ',army_numbers)

        #resolve number attacking letter
        index = -2
        print('deflet: ',deflet)
        for letter in deflet:        
            defletpow = letdict[letter]             #h = 8
            remlethp = defletpow - attnumpow         #attack = 8
            print('defletpow',defletpow,'remlethp',remlethp)
            if remlethp <= 0:
                army_letters.reverse()
                army_letters.remove(letter)
                army_letters.reverse()
                index += 1
                print('armylettersEND',army_letters)
            else:
                for a,b in letdict.items(): 
                    if remlethp == b:
                        newletter = a
                if len(army_letters) < 2:
                    army_letters[index+1] = newletter
                    index += 1
                else:
                    army_letters[index] = newletter
                    index += 1
                print('armylettersINTERIM: ',army_letters)
        index = -2
        print('armynumbersINTERIM: ',army_numbers)
        print('------ROUNDEND-----')
                

    #convert numbers list from int to str#
    zdex = 0               
    for i in army_numbers:
        army_numbers[zdex] = str(i)
        zdex += 1

    if len(army_letters) == 0 and len(army_numbers) == 0:
        return 'Draw'
    elif len(army_letters) == 0:
        return ''.join(army_numbers)
    else:
        return ''.join(army_letters)


print(battle_codes(army_letters,army_numbers))