# -*- coding:utf-8 -*-
import random

win = 1.0
draw = 0.5
lose = 0.0

girls = {
    '1': {'Name' : "a", 'Excepted' : 10, 'Position': 0},
    '2': {'Name' : "b", 'Excepted' : 10, 'Position': 0},
    '3': {'Name' : "c", 'Excepted' : 10, 'Position': 0},
    '4': {'Name' : "d", 'Excepted' : 10, 'Position': 0},
    '5': {'Name' : "e", 'Excepted' : 10, 'Position': 0},
    '6': {'Name' : "f", 'Excepted' : 10, 'Position': 0},
    '7': {'Name' : "g", 'Excepted' : 10, 'Position': 0},
    '8': {'Name' : "h", 'Excepted' : 10, 'Position': 0},
    '9': {'Name' : "i", 'Excepted' : 10, 'Position': 0},
    '10': {'Name' : "j", 'Excepted' : 10, 'Position': 0},
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

def Sort():
    done = []
    for x in girls:
        print x
    

def Show():
    print "=========="    
    for x in range(1, 11):
        print girls[str(x)]['Name'], girls[str(x)]['Excepted']
    print "=========="

if __name__ == '__main__':
    for i in range(random.randrange(1, 20)):
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
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'], girls[sec]['Excepted'] = result[0], result[1]
            '''
            i = 0
            for x in sorted(girls.iteritems(), key = lambda a: a[1], reverse = True):
                i += 1
                print x[1]['Name']
                print x, i
            '''
            Sort()
            Show()
        elif choice.rstrip('\n') == girls[sec]['Name']:
            Sa_fir, Sa_sec = lose, win
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'], girls[sec]['Excepted'] = result[0], result[1]
            print sorted(girls.iteritems(), key = lambda a: a[1], reverse = True)
            '''
            i = 0            
            for x in sorted(girls.iteritems(), key = lambda a: a[1], reverse = True):
                i += 1
                print x[1]['Name']
                print x, i
            '''
            Sort()            
            Show()
        else:
            Sa_fir = Sa_sec = draw
            result = Update(Ra_fir, Ra_sec, Sa_fir, Sa_sec, Ea_fir, Ea_sec)
            girls[fir]['Excepted'], girls[sec]['Excepted'] = result[0], result[1]
            print sorted(girls.iteritems(), key = lambda a: a[1], reverse = True)
            '''
            i = 0
            for x in sorted(girls.iteritems(), key = lambda a: a[1], reverse = True):
                i += 1
                print x[1]['Name']
                print x, i
            '''
            Sort()            
            Show()
