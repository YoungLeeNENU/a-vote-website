# -*- coding:utf-8 -*-
import random

win = 1.0
draw = 0.5
lose = 0.0
cache = 0

girls = {
    '1': {'Name' : "张", 'Excepted' : 60, 'Position': 0},
    '2': {'Name' : "李", 'Excepted' : 60, 'Position': 0},
    '3': {'Name' : "康", 'Excepted' : 60, 'Position': 0},
    '4': {'Name' : "林", 'Excepted' : 60, 'Position': 0},
    '5': {'Name' : "范", 'Excepted' : 60, 'Position': 0},
    '6': {'Name' : "唐", 'Excepted' : 60, 'Position': 0},
    '7': {'Name' : "赵", 'Excepted' : 60, 'Position': 0},
    '8': {'Name' : "周", 'Excepted' : 60, 'Position': 0},
    '9': {'Name' : "王", 'Excepted' : 60, 'Position': 0},
    '10': {'Name' : "杨", 'Excepted' : 60, 'Position': 0},
}

def Excepted(Ra, Rb):
    Ea = 1.0 / (1.0 + 10.0 ** ((Rb - Ra) / 100.0))
    Eb = 1.0 / (1.0 + 10.0 ** ((Ra - Rb) / 100.0))
    
    return Ea, Eb

def Update(Ra, Rb, Sa, Sb, Ea, Eb):
    New_Ra = Ra
    New_Rb = Rb
    if Sa != Ea:
        New_Ra = Ra + 16 * (Sa - Ea)
    if Sb != Eb:
        New_Rb = Rb + 16 * (Sb - Eb)
    return New_Ra, New_Rb

def Show():
    print "===* LEADING BOARD *==="
    i = 1
    for x in sorted(girls.iteritems(), key = lambda a: a[1], reverse = True):
        for y in girls.items():
            if y[1]['Name'] == x[1]['Name']:
                girls[x[0]]['Position'] = i
        i += 1
        print x[1]['Position'], x[1]['Name'], x[1]['Excepted']
    print "======================="

def Range():
    score_range = []
    for x in girls.items():
        score_range.append(x[1]['Position'])
    Min = min(score_range)
    Max = max(score_range)
    theta = Max - Min
    
    
if __name__ == '__main__':
    Range()
    while 1:
        if cache != 0:
            fir = cache
            sec = random.randrange(1, 11)
            while sec == fir:
                sec = random.randrange(1, 11)
                if sec != fir: break
        else:
            fir, sec = random.randrange(1, 11), random.randrange(1, 11)
            while sec == fir:
                sec = random.randrange(1, 11)
                if sec != fir: break
        fir = str(fir)
        sec = str(sec)

        print girls[fir]['Name'], "VS", girls[sec]['Name'], ":"
        
        Ra_fir = girls[fir]['Excepted']
        Ra_sec = girls[sec]['Excepted']
        Ea_fir = Excepted(Ra_fir, Ra_sec)[0]
        Ea_sec = Excepted(Ra_fir, Ra_sec)[1]
        
        choice = raw_input("Your choice is: \n")
        
        if choice.rstrip('\n') == girls[fir]['Name']:
            Sa_fir, Sa_sec = win, lose
            cache = int(fir)
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'] = result[0]
            girls[sec]['Excepted'] = result[1]
            Show()
        elif choice.rstrip('\n') == girls[sec]['Name']:
            Sa_fir, Sa_sec = lose, win
            cache = int(sec)
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'] = result[0]
            girls[sec]['Excepted'] = result[1]
            Show()
        else:
            Sa_fir = Sa_sec = draw
            cache = 0
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'] = result[0]
            girls[sec]['Excepted'] = result[1]
            Show()
