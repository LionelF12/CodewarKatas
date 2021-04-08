strg = ('02|15|59, 01|15|17, 01|22|34, 02|17|20, 11|15|59, 00|22|34, 11|22|00, 01|26|37, 02|32|34')
def stat(strg):
    import math

    print('original', strg)
    if strg == "":
        return ""
    strlist = strg.split(',')
    newlist = None
    for item in strlist:
        item = item.strip()
        values = item.split('|')
        index = 0
        for value in values:
            if len(value) == 1:
                values[index] = '0'+ value
            index += 1
        values = '|'.join(values)
        if newlist == None:
            newlist = values
        else:
            newlist += ',' + values
    strg = newlist.split(',')
    strg.sort()  
    # print('cleansed original: ', strg)    
    #average#
    totm = 0
    timings = strg
    numrunners = len(timings)
    index = 0 
    for time in timings:
        timings[index] = time.strip()
        h = time.split('|')[0]
        if h.startswith('0'):                 #changed from len(h) ==2 to use startswith.()
            h = h[1:]
        totm += int(h)*60
    
        m = time.split('|')[1]
        if m.startswith('0'):                 
            m = m[1:]
        totm += int(m)

        s = time.split('|')[2]
        if s.startswith('0'):                 
            s = s[1:]
        totm += int(s)/60
        index += 1
    avgm = totm/numrunners
    avghour = 0
    avgmin = 0
    avgsec = 0
    while avgm > 60:
        avgm -= 60
        avghour += 1
    
    avghour = str(avghour)
    if len(avghour) == 1:
        avghour = '0' + avghour
    avgmin = str(math.floor(avgm))
    if len(avgmin) == 1:
        avgmin = '0' + avgmin
    avgsec = str(math.trunc(round(((avgm - math.floor(avgm))*60),3)))       ##first mathtrunc to floor to round3+mathtrunc
    if len(avgsec) == 1:
        avgsec = '0' + avgsec
    Average = avghour +'|'+ avgmin + '|' + avgsec
    #print('Average: '+ Average)
    
    #range#
    timings.sort()
    print('rangetimingsstart: ', timings)
    #hour diff
    lasth = timings[-1:][0].split('|')[0]
    firsth = timings[0:1][0].split('|')[0]
    if firsth.startswith('0'):               #fix range logic as first h could be 10 or 11 not just 01, or 02. try .startswith()
        firsth = firsth[-1:][0]
    if lasth.startswith('0'):               #fix range logic as first h could be 10 or 11 not just 01, or 02. try .startswith()
        lasth = lasth[-1:][0] 
    hdiff = int(lasth)-int(firsth)
    #min diff
    lastm = timings[-1:][0].split('|')[1]
    firstm = timings[0:1][0].split('|')[1]
    if firstm.startswith('0'):          
        firstm = firstm[-1:][0]
    if lastm.startswith('0'):               
        lastm = lastm[-1:][0] 
    if int(lastm)-int(firstm) >= 0:
        mdiff = int(lastm)-int(firstm)
    else:
        mdiff = 60 - abs(int(lastm)-int(firstm))
        hdiff -= 1
    #secdiff
    lasts = timings[-1:][0].split('|')[2]
    firsts = timings[0:1][0].split('|')[2]
    if firsts.startswith('0'):          
        firsts = firsts[-1:][0]
    if lastm.startswith('0'):               
        lasts = lasts[-1:][0] 
    if int(lasts)-int(firsts) >= 0:
        sdiff = int(lasts)-int(firsts)
    else:
        sdiff = 60-abs(int(lasts)-int(firsts))
        if mdiff == 0:
            mdiff = 59
        else: mdiff -= 1
    hdiff = str(hdiff)
    mdiff = str(mdiff)
    sdiff = str(sdiff)
    if len(hdiff) == 1:
        hdiff = '0' + hdiff
    if len(mdiff) == 1:
        mdiff = '0' + mdiff 
    if len(sdiff) == 1:
        sdiff = '0' + sdiff 
    Range = hdiff +'|'+ mdiff + '|' + sdiff
    #print('Range: ', Range)

    #median#
    if len(timings) % 2 != 0:
        medpos = math.floor(len(timings)/2)
        timings2 = timings[medpos].split('|')
        index = 0
        for time in timings2:
            if len(time) == 1:
                timings2[index] = '0' + time
            index += 1
        Median = '|'.join(timings2)
    else:
        medposlow = int(len(timings)/2-1)
        medposhigh = int(len(timings)/2)
        medlow = timings[medposlow]
        medhigh = timings[medposhigh]
    
        #averaging for median#
        medlowlist = medlow.split('|')
        index = 0
        for meditem in medlowlist:
            if meditem.startswith('0'):
                medlowlist[index] = meditem[1:]
                index += 1
            else: 
                index += 1
        try:
            guard3 = int(medlowlist[2])/60
        except:
            guard3 = 0
        try:
            guard2 = int(medlowlist[1])
        except:
            guard2 = 0
        try:
            guard1 = int(medlowlist[0])*60 
        except:
            guard1 = 0        
        medlowtotm = guard1 + guard2 + guard3

        medhighlist = medhigh.split('|')
        index = 0
        for meditem in medhighlist:
            if meditem.startswith('0'):
                medhighlist[index] = meditem[1:]
                index += 1
            else: 
                index += 1
        try:
            guardx1 = int(medhighlist[0])*60
        except:
            guardx1 = 0
        try:
            guardx2 = int(medhighlist[1])
        except:
            guardx2 = 0
        try:
            guardx3 = int(medhighlist[2])/60
        except:
            guardx3 = 0           
        medhightotm = guardx1 + guardx2 + guardx3
        medavg = (medlowtotm + medhightotm)/2

        #median average h/m/s#
        medavgh = 0
        medavgm = 0
        medavgs = 0
        while medavg > 60:
            medavgh += 1
            medavg -=60
        medavgh = str(medavgh)
        if len(medavgh) == 1:
            medavgh = '0' + medavgh

        medavgm = str(math.floor(medavg))
        medavgs = str(math.trunc(round(((medavg - math.floor(medavg))*60),3)))   ##first mathtrunc to floor to round3+mathtrunc
        if len(medavgm) == 1:
            medavgm = '0' + medavgm
        if len(medavgs) == 1:
            medavgs = '0' + medavgs
        #final numbers#
        Median = medavgh +'|'+ medavgm + '|' + medavgs
    #print('Median: ',Median)

    return('Range: ' + Range +' ' + 'Average: ' + Average + ' ' + 'Median: ' + Median)
print(stat(strg))