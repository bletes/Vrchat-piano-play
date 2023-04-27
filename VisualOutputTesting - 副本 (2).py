from MidiParser import MidiParser
from MidiData import MidiData
from Util import Util
from MidiEventDecoder import MidiEventDecoder
import matplotlib.pyplot as plt
import pyautogui
#pyautogui.PAUSE=0.001 #window vk
#pyautogui.KEYBOARD_KEYS
import pydirectinput
pydirectinput.PAUSE=0.0001 #direct exe
import time
import random
import pandas as pd
##import keyboard
##import time
##keyboard.start_recording()
##time.sleep(2)
##ww=keyboard.stop_recording()



def printHex(_bytes):
    temp = ""
    for i in range(len(_bytes)):
        temp = temp + " " + str(hex(_bytes[i]))
    print(temp)


def printRawFile():
    print("-----------------raw file-----------------------")
    with open(midi_file, 'rb') as file:
        printHex(file.read())
    file.close()
    print()
    print()


def testMidiParser():
    midiParser = MidiParser(midi_file)
    print("---------------Testing MidiParser--------------")
    print("Header def and size: " + str(midiParser.readNextData()))
    headerBody = midiParser.readNextData()
    print("Body of header chunk: " + str(headerBody) + " number of tracks: " +
          str(int.from_bytes(headerBody[2:4], "big")))
    while midiParser.hasMoreData():
        trackDef = midiParser.readNextData()
        print("Track def and size: " + str(trackDef) + " track size: "
              + str(int.from_bytes(trackDef[4:8], "big")))
        while midiParser.bytesLeftInChunk > 0:
            print(str(midiParser.readNextData()) + " size left: " +
                  str(midiParser.bytesLeftInChunk))
        print()
    midiParser.close()


def testEventDecoder():
    print("-----Testing MidiEventDecoder---------")
    # testing MidiEventDecoder
    eventDecoder = MidiEventDecoder(midi_file)  # testMidiFile.mid
    print(eventDecoder.headerData())
    # eventData = eventDecoder.nextEvent().midiData
    # print(int.from_bytes(eventData[0:1],"big"))
    # print(Util.msbIsOne(eventData))
    # print(type(eventData))
    while eventDecoder.hasMoreEvents():
        event = eventDecoder.nextEvent()
        print(event)
    eventDecoder.close()
    print()


def testMidiData():
    print("-----Testing MidiData---------")
    midiData = MidiData(midi_file)
    for i in range(midiData.getNumTracks()):
        track = midiData.getTrack(i)
        print(track.name)
        for note in track.notes:
            print(note)
        print()
    print()
    print("Note F4 329.04s to 339.32s Channel: 11 <-- expected last note (TestMidiFile2.mid)")
    # print("Note A4 12.50s to 13.00s Channel: 1 <-- expected last note (testingrunningstatus.mid)")


# printRawFile()
# testMidiParser()
# testEventDecoder()

##testMidiData()

def plxy(bb):
    plx=[]
    ply=[]
    for i in bb:
        plx.append(i[1])
        ply.append(i[0])
    plt.scatter(plx,ply)
    plt.show()

##def comb():
##    bb1=[]
##    for i in range(len(bb)):
##        try:
##            if bb[i]+1
##
##def prep(i):
##    lis=[i for i,x in enumerate(bb3) if x== bb2[i]]
##    for x in lis:
##        pre(bb[x][0])
##    pre(bb[i][0])
##    try:
##        if bb[i+1][1]==bb[i][1]:
##            pre(bb[i+1][0])
##        if bb[i+2][1]==bb[i][1]:
##            pre(bb[i+2][0])
##        if bb[i+3][1]==bb[i][1]:
##            pre(bb[i+3][0])
##        if bb[i+4][1]==bb[i][1]:
##            pre(bb[i+4][0])
##        if bb[i+5][1]==bb[i][1]:
##            pre(bb[i+5][0])
##    except:
##        pass



##def play(bb,spe):
##    bb=[[x[0],x[1]*spe,x[2]] for x in bb]
##    bb1=[x[0] for x in bb]##按键轴
##    bb3=[x[1]/1000 for x in bb] ##时间轴
##    bb2=[]#非重复的时间轴
##
##    for i in bb3:
##        if i not in bb2:
##            bb2.append(i)
##    llis=[]
##    for i in range(len(bb2)):
##        lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##        llis.append(lis)
##    tt=time.time()
##
##    for i in range(len(bb2)):
##
##        for x in llis[i]:
##            pre(bb1[x])
####            time.sleep(0.0001)
##
##        
##        if i<(len(bb2)-1):
##            if bb2[i+1]>(time.time()-tt):
##                time.sleep((bb2[i+1]-(time.time()-tt))/1.1)
##            if bb2[i+1]<(time.time()-tt):
##                time.sleep(0.01)
####            try:
####                time.sleep((bb2[i+1]-(time.time()-tt))/1.1)
####            except:
####                pass

def play(bb,spe):#bb=data[note,time,spendtime] spe=speed
    bb=[[x[0],x[1]*spe,x[2]] for x in bb]
    start_set=0#start point
    bb_new=[]
    for i in bb:
        if i[1]>start_set:
            bb_new.append(i)#zaichuang bb
    print(bb_new)
    bb1=[x[0] for x in bb_new]##按键轴
    bb3=[x[1]/1000 for x in bb_new] ##时间轴
    bb2=[]#非重复的时间轴
    for i in bb3:
        if i not in bb2:
            bb2.append(i)
    llis=[]
    for i in range(len(bb2)):
        lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
        llis.append(lis)
    tt=time.time()
    for i in range(len(bb2)):
##        if bb2[i]>(start_set/1000):
        for x in llis[i]:
            pre(bb1[x])
        if i<(len(bb2)-1):
            if bb2[i+1]>(time.time()-tt):#yiguo time
                time.sleep((bb2[i+1]-(time.time()-tt))/1.1)
            if bb2[i+1]<(time.time()-tt):
                time.sleep(0.01)
def play(bb,spe):
    bb['1']=bb['1']/1000*spe
    #cc=set(bb['1'])#神奇不排序
    dd=bb.groupby(['1'])['0'].apply(list).to_frame()
    tt=time.time()
    for i in dd.index:
        for kk in dd['0'][i]:
            pre(kk)
       # if i<(len(dd)-1):
        if i>(time.time()-tt):#yiguo time
            time.sleep((i-(time.time()-tt))/1.1)
        if i<(time.time()-tt):
            time.sleep(0.01)
            
##    for i in cc.index:
##        pre(cc['0'][i])
##    for i in range(len(cc)):
##        for i in bb[bb['1']==cc.pop()]['0']:
##            pre(i)
        
    pass

##def playcut(bbt,spe,bbt0,bbt1):
##    bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
##    bb1=[x[0] for x in bb]##按键轴
##    bb3=[x[1]/1000 for x in bb] ##时间轴
##    bb2=[]#非重复的时间轴
##
##    for i in bb3:
##        if i not in bb2:
##            bb2.append(i)
##    llis=[]
##    for i in range(len(bb2)):
##        lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##        llis.append(lis)
##    tt=time.time()
##    cut=0
##    clen=int(input('long'))
##    time.sleep(1)
##    for i in range(len(bb2)):
##        if cut>clen:
##            clen=int(input('long'))
##            if clen==0:#change spe
##                clen=55
##                spe=int(input('spe'))*0.01
##                
##                bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
##                bb1=[x[0] for x in bb]##按键轴
##                bb3=[x[1]/1000 for x in bb] ##时间轴
##                bb2=[]#非重复的时间轴
##                for i in bb3:
##                    if i not in bb2:
##                        bb2.append(i)
##                llis=[]
##                for i in range(len(bb2)):
##                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##                    llis.append(lis)
##            if clen==1:
##                clen=55
##
##                bb=[]
##                for x in bbt:
##                    if x in bbt0:
##                        bb.append(x)
##                    else:
##                        bb.append([0,x[1],x[2]])
##                bb1=[x[0] for x in bb]##按键轴
##                bb3=[x[1]/1000 for x in bb] ##时间轴
##                bb2=[]#非重复的时间轴
##                for i in bb3:
##                    if i not in bb2:
##                        bb2.append(i)
##                llis=[]
##                for i in range(len(bb2)):
##                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##                    llis.append(lis)
##            if clen==2:#change spe
##                clen=55
##                
##                
##                bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
##                bb1=[x[0] for x in bb]##按键轴
##                bb3=[x[1]/1000 for x in bb] ##时间轴
##                bb2=[]#非重复的时间轴
##                for i in bb3:
##                    if i not in bb2:
##                        bb2.append(i)
##                llis=[]
##                for i in range(len(bb2)):
##                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##                    llis.append(lis)
##            if clen==3:
##                clen=55222
##
##                bb=[]
##                for x in bbt:
##                    if x in bbt1:
##                        bb.append(x)
##                    else:
##                        bb.append([0,x[1],x[2]])
##                bb1=[x[0] for x in bb]##按键轴
##                bb3=[x[1]/1000 for x in bb] ##时间轴
##                bb2=[]#非重复的时间轴
##                for i in bb3:
##                    if i not in bb2:
##                        bb2.append(i)
##                llis=[]
##                for i in range(len(bb2)):
##                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##                    llis.append(lis)
##        
##            time.sleep(1)
##            cut=0
##        cut+=1
##
##        for x in llis[i]:
##            pre(bb1[x])
####            time.sleep(0.0001)
##        if i<(len(bb2)-1):#if not end
##            time.sleep(bb2[i+1]-bb2[i])


def playcut(bbt,spe,bbt0,bbt1):#bbt means bb,bbt0 means track0,bbt0 means track1
    bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
    start_set=50000#start point 0.01s unit
    bb_new=[]
    for i in bb:
        if i[1]>start_set:
            bb_new.append(i)
    print(bb_new)
    bb1=[x[0] for x in bb_new]##按键轴#103+24=127#127-
##    bb1.reverse()
    bb3=[x[1]/1000 for x in bb_new] ##时间轴
    bb2=[]#非重复的时间轴

    for i in bb3:
        if i not in bb2:
            bb2.append(i)
    llis=[]
    for i in range(len(bb2)):
        lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
        llis.append(lis)
    tt=time.time()
    cut=0
    #ge=[1,1,311,2,2222]
    ge=[55555,1]
    gen=(x for x in ge)
    clen=int(next(gen))
##    time.sleep(1)
    for i in range(len(bb2)):
        if cut>clen:
            clen=int(next(gen))
            if clen==0:#change spe
                clen=55
                spe=int(input('spe'))*0.01
                
                bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
                bb1=[x[0] for x in bb]##按键轴
                bb3=[x[1]/1000 for x in bb] ##时间轴
                bb2=[]#非重复的时间轴
                for i in bb3:
                    if i not in bb2:
                        bb2.append(i)
                llis=[]
                for i in range(len(bb2)):
                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
                    llis.append(lis)
            if clen==1:
                clen=55

                bb=[]
                for x in bbt:
                    if x in bbt0:
                        bb.append(x)
                    else:
                        bb.append([0,x[1],x[2]])
                bb1=[x[0] for x in bb]##按键轴
                bb3=[x[1]/1000 for x in bb] ##时间轴
                bb2=[]#非重复的时间轴
                for i in bb3:
                    if i not in bb2:
                        bb2.append(i)
                llis=[]
                for i in range(len(bb2)):
                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
                    llis.append(lis)
            if clen==2:#change spe
                clen=55
                
                
                bb=[[x[0],x[1]*spe,x[2]] for x in bbt]
                bb1=[x[0] for x in bb]##按键轴
                bb3=[x[1]/1000 for x in bb] ##时间轴
                bb2=[]#非重复的时间轴
                for i in bb3:
                    if i not in bb2:
                        bb2.append(i)
                llis=[]
                for i in range(len(bb2)):
                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
                    llis.append(lis)
            if clen==3:
                clen=55222

                bb=[]
                for x in bbt:
                    if x in bbt1:
                        bb.append(x)
                    else:
                        bb.append([0,x[1],x[2]])
                bb1=[x[0] for x in bb]##按键轴
                bb3=[x[1]/1000 for x in bb] ##时间轴
                bb2=[]#非重复的时间轴
                for i in bb3:
                    if i not in bb2:
                        bb2.append(i)
                llis=[]
                for i in range(len(bb2)):
                    lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
                    llis.append(lis)
        
##            time.sleep(1)
            cut=0
        cut+=1

        for x in llis[i]:
            pre(bb1[x])
##            time.sleep(0.0001)
        if i<(len(bb2)-1):#if not end
            time.sleep(bb2[i+1]-bb2[i])

            
##            if bb2[i+1]>(time.time()-tt):#pass time-)delta time
##                time.sleep((bb2[i+1]-(time.time()-tt))/1.1)
##            if bb2[i+1]<(time.time()-tt):
##                time.sleep(0.01)

##def play(bb,spe):
##    bb=[[x[0],x[1]*spe,x[2]] for x in bb]
##    bb1=[x[0] for x in bb]##按键轴
##    bb3=[x[1]/1000 for x in bb] ##时间轴
##    bb2=[]#非重复的时间轴
##
##    for i in bb3:
##        if i not in bb2:
##            bb2.append(i)
##    bb2m=[bb2[0]]#minutes
##    for i in range(len(bb2)):
##        if i>0:
##            bb2m.append(bb2[i]-bb2[i-1])
##    llis=[]#某个时间的所有按键
##    for i in range(len(bb2)):
##        lis=[y for y,x in enumerate(bb3) if x== bb2[i]]#bb2表示未重复，是时间轴，寻找在重复的里的index，然后弹
##        llis.append(lis)
##    tt=time.time()
##    spt=0
##    k=0
##    for i in range(len(bb2)):
##        if k%333==0:
##            spt=random.randint(6,15)*0.1
##
##        for x in llis[i]:
##            pre(bb1[x])
##            time.sleep(0.0001)
##
##        
##        if i<(len(bb2)-1):
##            try:
##                time.sleep((bb2m[i+1])*spt)
##            except:
##                pass
##     eieu   k=k+1


spe=1.03
midi_file ='mer'+'.mid'
#pas gol gur shi pla gmin fli sum fan 12v nor kim thi hai 12265 fant moon3 sen
#beli und2 kil mos eva thec des mag1 lov shin end madw lav ath belie
#ima myw mari mii2 pia aut com nev ton summ por yan wal2 inte Merry Christmas Mr. Lawrence

#myh1 myh mer vit gior guil myde hav wei yug sup ato old dra pea cit park bio
#req thep flo por sig schi youra yoa dis bli 200a gas ren2 imb atow
# ham mou chi senb n922 joh ylg masa sev lib your vog yeye dej val ani
#Merry Christmas Mr. Lawrence
print(midi_file) 
 
def tur(aa):
    aa=aa.replace('55','q').replace('56','w').replace('57','e').replace('58','r').replace('5','t').replace('6','y').replace('7','u').replace('8','i')
rdb=random.sample([10,0,0,0,0,0,0,0,0,0,0,0,0,10],1)[0]#random b

##def pre(aa):#ff14
##    b=bl#min max+36    91-36=55
##    if bh-bl>40:
##        b=bh-36
##    b=55-(91-91)#55-(91-x)
##    b=bh-36+1
####        b=45
##    if aa==b+0:
##        pyautogui.press('z')
##    if aa==b+1:
##        pyautogui.press('1')#1
##    if aa==b+2:
##        pyautogui.press('x')
##    if aa==b+3:
##        pyautogui.press('4')#4y
##    if aa==b+4:
##        pyautogui.press('c')  
##    if aa==b+5:
##        pyautogui.press('v')
##    if aa==b+6:
##        pyautogui.press('8')#8
##    if aa==b+7:
##        pyautogui.press('b')
##    if aa==b+8:
##        pyautogui.press('9')#9
##    if aa==b+9:
##        pyautogui.press('n')
##    if aa==b+10:
##        pyautogui.press('0')#0
##    if aa==b+11:
##        pyautogui.press('m')
##    if aa==b+12:
##        pyautogui.press('q')
##    if aa==b+13:
##        pyautogui.press('2')
##    if aa==b+14:
##        pyautogui.press('w')
##    if aa==b+15:
##        pyautogui.press('3')
##    if aa==b+16:
##        pyautogui.press('e')
##    if aa==b+17:
##        pyautogui.press('r')
##    if aa==b+18:
##        pyautogui.press('5')
##    if aa==b+19:
##        pyautogui.press('t')
##    if aa==b+20:
##        pyautogui.press('6')
##    if aa==b+21:
##        pyautogui.press('y')
##    if aa==b+22:
##        pyautogui.press('7')
##    if aa==b+23:
##        pyautogui.press('u')
##    if aa==b+24:
##        pyautogui.press('a')
##    if aa==b+25:
##        pyautogui.press('i') #i
##    if aa==b+26:
##        pyautogui.press('s')
##    if aa==b+27:
##        pyautogui.press('o') #o
##    if aa==b+28:
##        pyautogui.press('d')
##    if aa==b+29:
##        pyautogui.press('f')
##    if aa==b+30:
##        pyautogui.press('p') #p
##    if aa==b+31:
##        pyautogui.press('g')
##    if aa==b+32:
##        pyautogui.press('[') #[
##    if aa==b+33:
##        pyautogui.press('h')
##    if aa==b+34:
##        pyautogui.press(']') #]
##    if aa==b+35:
##        pyautogui.press('j')
##    if aa==b+36:
##        pyautogui.press('k') 


def pre(aa): #vr zhongwenba
    b=bl#min max+36
    b=32+rdb
    if bh>91 and (bh-bl)<60:
        #b=bh-50
        b=bh-60
    b=29
##        b=55
##        b=45
    if aa==b+0:
        pydirectinput.press('z')
    if aa==b+1:
        pydirectinput.press(',')
    if aa==b+2:
        pydirectinput.press('x')
    if aa==b+3:
        pydirectinput.press('.')
    if aa==b+4:
        pydirectinput.press('c')  
    if aa==b+5:
        pydirectinput.press('v')
    if aa==b+6:
        pydirectinput.press('/')
    if aa==b+7:
        pydirectinput.press('b')
    if aa==b+8:
        pyautogui.press('num0')
    if aa==b+9:
        pydirectinput.press('n')
    if aa==b+10:
        pyautogui.press('decimal')
    if aa==b+11:
        pydirectinput.press('m')
    if aa==b+12:
        pydirectinput.press('a')
    if aa==b+13:
        pydirectinput.press('k')
    if aa==b+14:
        pydirectinput.press('s')
    if aa==b+15:
        pydirectinput.press('l')
    if aa==b+16:
        pydirectinput.press('d')
    if aa==b+17:
        pydirectinput.press('f')
    if aa==b+18:
        pydirectinput.press(';')
    if aa==b+19:
        pydirectinput.press('g')
    if aa==b+20:
        pyautogui.press('num2')
    if aa==b+21:
        pydirectinput.press('h')
    if aa==b+22:
        pyautogui.press('num3')
    if aa==b+23:
        pydirectinput.press('j')
    if aa==b+24:
        pydirectinput.press('q')
    if aa==b+25:
        pydirectinput.press('i')
    if aa==b+26:
        pydirectinput.press('w')
    if aa==b+27:
        pydirectinput.press('o')
    if aa==b+28:
        pydirectinput.press('e')
    if aa==b+29:
        pydirectinput.press('r')
    if aa==b+30:
        pydirectinput.press('p')
    if aa==b+31:
        pydirectinput.press('t')
    if aa==b+32:
        pyautogui.press('num5')
    if aa==b+33:
        pydirectinput.press('t')
    if aa==b+34:
        pyautogui.press('num6')
    if aa==b+35:
        pydirectinput.press('u')
    if aa==b+36:
        pydirectinput.press('1')
    if aa==b+37:
        pydirectinput.press('8')
    if aa==b+38:
        pydirectinput.press('2')
    if aa==b+39:
        pydirectinput.press('9')
    if aa==b+40:
        pydirectinput.press('3')
    if aa==b+41:
        pydirectinput.press('4')
    if aa==b+42:
        pydirectinput.press('0')
    if aa==b+43:
        pydirectinput.press('5')
    if aa==b+44:
        pyautogui.press('num8')
    if aa==b+45:
        pydirectinput.press('6')
    if aa==b+46:
        pyautogui.press('num9')
    if aa==b+47:
        pydirectinput.press('7')
    if aa==b+48:
        pydirectinput.press('f1')
    if aa==b+49:
        pydirectinput.press('f8')
    if aa==b+50:
        pydirectinput.press('f2')
    if aa==b+51:
        pydirectinput.press('f9')
    if aa==b+52:
        pydirectinput.press('f3')
    if aa==b+53:
        pydirectinput.press('f4')
    if aa==b+54:
        pydirectinput.press('f10')
    if aa==b+55:
        pydirectinput.press('f5')
    if aa==b+56:
        pyautogui.press('divide')
    if aa==b+57:
        pydirectinput.press('f6')
    if aa==b+58:
        pyautogui.press('multiply')
    if aa==b+59:
        pydirectinput.press('f7')

####b=bl#min max+36
##b=44#47 myh
##def pre(aa): #vrhotel

####    if bh-bl>40:
####        b=bh-36
####        b=55
####        b=45
##    if aa==b+0:
##        pydirectinput.press('1')
##    if aa==b+1:
##        pyautogui.hotkey('shift', '1',interval=0.02)
##    if aa==b+2:
##        pydirectinput.press('2')
##    if aa==b+3:
##        pyautogui.hotkey('shift', '2',interval=0.02)
##    if aa==b+4:
##        pydirectinput.press('3')
##    if aa==b+5:
##        pydirectinput.press('4')
##    if aa==b+6:
##        pyautogui.hotkey('shift', '4',interval=0.02)
##    if aa==b+7:
##        pydirectinput.press('5')
##    if aa==b+8:
##        pyautogui.hotkey('shift', '5',interval=0.02)
##    if aa==b+9:
##        pydirectinput.press('6')
##    if aa==b+10:
##        pyautogui.hotkey('shift', '6',interval=0.02)
##    if aa==b+11:
##        pydirectinput.press('7')
##    if aa==b+12:
##        pydirectinput.press('8')
##    if aa==b+13:
##        pyautogui.hotkey('shift', '8',interval=0.02)
##    if aa==b+14:
##        pyautogui.press('9')
##    if aa==b+15:
##        pyautogui.hotkey('shift', '9',interval=0.02)
##    if aa==b+16:
##        pydirectinput.press('0')
##    if aa==b+17:
##        pyautogui.press('q')
##    if aa==b+18:
##        pyautogui.hotkey('shift', 'q',interval=0.02)
##    if aa==b+19:
##        pydirectinput.press('w')
##    if aa==b+20:
##        pyautogui.hotkey('shift', 'w',interval=0.02)
##    if aa==b+21:
##        pydirectinput.press('e')
##    if aa==b+22:
##        pyautogui.hotkey('shift', 'e',interval=0.02)
##    if aa==b+23:
##        pydirectinput.press('r')
##    if aa==b+24:
##        pydirectinput.press('t')
##    if aa==b+25:
##        pyautogui.hotkey('shift', 't',interval=0.02)
##    if aa==b+26:
##        pydirectinput.press('y')
##    if aa==b+27:
##        pyautogui.hotkey('shift', 'y',interval=0.02)   
##    if aa==b+28:
##        pydirectinput.press('u')
##    if aa==b+29:
##        pydirectinput.press('i')
##    if aa==b+30:
##        pyautogui.hotkey('shift', 'i',interval=0.02)
##    if aa==b+31:
##        pydirectinput.press('o')
##    if aa==b+32:
##        pyautogui.hotkey('shift', 'o',interval=0.02)
##    if aa==b+33:
##        pydirectinput.press('p')
##    if aa==b+34:
##        pyautogui.hotkey('shift', 'p',interval=0.02)
##    if aa==b+35:
##        pyautogui.press('a')
##    if aa==b+36:
##        pydirectinput.press('s')
##    if aa==b+37:
##        pyautogui.hotkey('shift', 's',interval=0.02)
##    if aa==b+38:
##        pyautogui.press('d')
##    if aa==b+39:
##        pyautogui.hotkey('shift', 'd',interval=0.02)
##    if aa==b+40:
##        pydirectinput.press('f')
##    if aa==b+41:
##        pydirectinput.press('g')
##    if aa==b+42:
##        pyautogui.hotkey('shift', 'g',interval=0.02)
##    if aa==b+43:
##        pydirectinput.press('h')
##    if aa==b+44:
##        pyautogui.hotkey('shift', 'h',interval=0.02)
##    if aa==b+45:
##        pydirectinput.press('j')
##    if aa==b+46:
##        pyautogui.hotkey('shift', 'j',interval=0.02)
##    if aa==b+47:
##        pydirectinput.press('k')
##    if aa==b+48:
##        pydirectinput.press('l')
##    if aa==b+49:
##        pyautogui.hotkey('shift', 'l',interval=0.02)
##    if aa==b+50:
##        pydirectinput.press('z')
##    if aa==b+51:
##        pyautogui.hotkey('shift', 'z',interval=0.02)
##    if aa==b+52:
##        pydirectinput.press('x')
##    if aa==b+53:
##        pydirectinput.press('c')
##    if aa==b+54:
##        pyautogui.hotkey('shift', 'c',interval=0.02)
##    if aa==b+55:
##        pyautogui.press('v')
##    if aa==b+56:
##        pyautogui.hotkey('shift', 'v',interval=0.02)
##    if aa==b+57:
##        pydirectinput.press('b')
##    if aa==b+58:
##        pyautogui.hotkey('shift', 'b',interval=0.02)
##    if aa==b+59:
##        pyautogui.press('n')


##def pre(aa): #vr piano
##    b=bl#min max+36
##    b=33
####    if bh-bl>40:
####        b=bh-57
####        b=55
####        b=45
##    if aa==b+0:
##        pydirectinput.press('z')
##    if aa==b+1:
##        pydirectinput.press('s')
##    if aa==b+2:
##        pydirectinput.press('x')
##    if aa==b+3:
##        pydirectinput.press('d')
##    if aa==b+4:
##        pydirectinput.press('c')  
##    if aa==b+5:
##        pydirectinput.press('v')
##    if aa==b+6:
##        pydirectinput.press('g')
##    if aa==b+7:
##        pydirectinput.press('b')
##    if aa==b+8:
##        pydirectinput.press('h')
##    if aa==b+9:
##        pydirectinput.press('n')
##    if aa==b+10:
##        pydirectinput.press('j')
##    if aa==b+11:
##        pydirectinput.press('m')
##    if aa==b+12:
##        pydirectinput.press('tab')
##    if aa==b+13:
##        pydirectinput.press('1')
##    if aa==b+14:
##        pydirectinput.press('q')
##    if aa==b+15:
##        pydirectinput.press('2')
##    if aa==b+16:
##        pydirectinput.press('w')
##    if aa==b+17:
##        pydirectinput.press('e')
##    if aa==b+18:
##        pydirectinput.press('4')
##    if aa==b+19:
##        pydirectinput.press('r')
##    if aa==b+20:
##        pydirectinput.press('5')
##    if aa==b+21:
##        pydirectinput.press('t')
##    if aa==b+22:
##        pydirectinput.press('6')
##    if aa==b+23:
##        pydirectinput.press('y')
##    if aa==b+24:
##        pydirectinput.press('u')
##    if aa==b+25:
##        pydirectinput.press('8')
##    if aa==b+26:
##        pydirectinput.press('i')
##    if aa==b+27:
##        pydirectinput.press('9')
##    if aa==b+28:
##        pydirectinput.press('o')
##    if aa==b+29:
##        pydirectinput.press('p')
##    if aa==b+30:
##        pydirectinput.press('-')
##    if aa==b+31:
##        pydirectinput.press('[')
##    if aa==b+32:
##        pydirectinput.press('=')
##    if aa==b+33:
##        pyautogui.press(']')
##    if aa==b+34:
##        pyautogui.press('backspace')
##    if aa==b+35:
##        pyautogui.press('\\')
##    if aa==b+36:
##        pyautogui.press('delete')
##    if aa==b+37:
##        pyautogui.press('insert')
##    if aa==b+38:
##        pyautogui.press('end')
##    if aa==b+39:
##        pyautogui.press('home')
##    if aa==b+40:
##        pyautogui.press('pagedown')
##    if aa==b+41:
##        pyautogui.press('num7')
##    if aa==b+42:
##        pyautogui.press('divide')
##    if aa==b+43:
##        pyautogui.press('num8')
##    if aa==b+44:
##        pyautogui.press('multiply')
##    if aa==b+45:
##        pyautogui.press('num9')
##    if aa==b+46:
##        pyautogui.press('subtract')
##    if aa==b+47:
##        pyautogui.press('add')
##    if aa==b+48:
##        pyautogui.press(',')
##    if aa==b+49:
##        pyautogui.press('l')
##    if aa==b+50:
##        pyautogui.press('.')
##    if aa==b+51:
##        pyautogui.press(';')
##    if aa==b+52:
##        pyautogui.press('/')
####    if aa==b+53:
####        pyautogui.press('shiftright')#
##    if aa==b+53:
##        pyautogui.press('num4')
##    if aa==b+54:
##        pyautogui.press('num1')
##    if aa==b+55:
##        pyautogui.press('num5')
##    if aa==b+56:
##        pyautogui.press('num2')
##    if aa==b+57:
##        pyautogui.press('num6')
##    if aa==b+58:
##        pyautogui.press('num3')
####    if aa==b+60:
####        pyautogui.press('separator')#


##def pre(aa): #Everyonepiano
##    b=bl#min max+36    
##    if bh-bl>40:
##        b=bh-36
##
##
####        b=45
##    if aa==b+0:
##        pydirectinput.press('z')
##    if aa==b+1:
##        pydirectinput.press('x')
##    if aa==b+2:
##        pydirectinput.press('c')
##    if aa==b+3:
##        pydirectinput.press('v')
##    if aa==b+4:
##        pydirectinput.press('b')  
##    if aa==b+5:
##        pydirectinput.press('n')
##    if aa==b+6:
##        pydirectinput.press('m')
##    if aa==b+7:
##        pydirectinput.press('a')
##    if aa==b+8:
##        pydirectinput.press('s')
##    if aa==b+9:
##        pydirectinput.press('d')
##    if aa==b+10:
##        pydirectinput.press('f')
##    if aa==b+11:
##        pydirectinput.press('g')
##    if aa==b+12:
##        pydirectinput.press('h')
##    if aa==b+13:
##        pydirectinput.press('j')
##    if aa==b+14:
##        pydirectinput.press('q')
##    if aa==b+15:
##        pydirectinput.press('w')
##    if aa==b+16:
##        pydirectinput.press('e')
##    if aa==b+17:
##        pydirectinput.press('r')
##    if aa==b+18:
##        pydirectinput.press('t')
##    if aa==b+19:
##        pydirectinput.press('y')
##    if aa==b+20:
##        pydirectinput.press('u')
##    if aa==b+21:
##        pydirectinput.press('i')
##    if aa==b+22:
##        pydirectinput.press('1')
##    if aa==b+23:
##        pydirectinput.press('2')
##    if aa==b+24:
##        pydirectinput.press('3')
##    if aa==b+25:
##        pydirectinput.press('4')
##    if aa==b+26:
##        pydirectinput.press('5')
##    if aa==b+27:
##        pydirectinput.press('6')
##    if aa==b+28:
##        pydirectinput.press('7')
##    if aa==b+29:
##        pydirectinput.press('8')
##    if aa==b+30:
##        pydirectinput.press('9')
##    if aa==b+31:
##        pydirectinput.press('0')
##    if aa==b+32:
##        pydirectinput.press('-')
##    if aa==b+33:
##        pydirectinput.press('=')
##    if aa==b+34:
##        pydirectinput.press('')
##    if aa==b+35:
##        pydirectinput.press('')
##    if aa==b+36:
##        pydirectinput.press('')
        



bb=pd.DataFrame(columns=['0','1','2'])
midiData = MidiData(midi_file)
for i in range(midiData.getNumTracks()):
    track = midiData.getTrack(i)
    for note in track.notes:
        bb.loc[len(bb.index)]=[note.pitch,note.startTime,(note.endTime-note.startTime)]
bb.sort_values(['1'],inplace=True,ascending=True)
bl=min(bb['0'])
bh=max(bb['0'])
for i in range(111100):
    play(bb,spe*1.03**i)
ee
bbt0=[]#track 0    
track = midiData.getTrack(0)
for note in track.notes:
    bbt0.append([note.pitch,note.startTime,(note.endTime-note.startTime)])
try:
    bbt1=[]#track 1    
    track = midiData.getTrack(1)
    for note in track.notes:
        bbt1.append([note.pitch,note.startTime,(note.endTime-note.startTime)])
except:
    print('no3')
eee
##for i in bb:
##    if i[2]<200:
##        bb.remove(i)
from operator import itemgetter, attrgetter
plxy(bb)   
tt=time.time()
bb=sorted(bb, key=itemgetter(1))
ply=[]
for i in bb:
    ply.append(i[0])
bl=min(ply)
bh=max(ply)
time.sleep(1)


##spe=random.randint(5,15)*0.1
##
##play(bb,random.randint(5,15)*0.1)
##play(bb,random.randint(5,15)*0.1)
##play(bb,random.randint(5,15)*0.1)
##play(bb,random.randint(5,15)*0.1)
##play(bb,random.randint(5,15)*0.1)

spe=0.99
for i in range(111):
    #playcut(bb,spe,bbt0,bbt1)
    play(bb,spe)
##    play(bb,spe)
##play(bbt0,spe)
##play(bb,spe)
##play(bbt0,spe)
##play(bb,spe)
##for i in range(63):   
##    time.sleep(0.5)
##    pre(33)
##for i in range(len(bb)):
##    if (time.time()-tt)*1000-bb[i][1]<10:
##        pre(bb[i][0])
##        try:
##            if bb[i+1][1]==bb[i][1]:
##                pre(bb[i+1][0])
##            if bb[i+2][1]==bb[i][1]:
##                pre(bb[i+2][0])
##            if bb[i+3][1]==bb[i][1]:
##                pre(bb[i+3][0])
##            if bb[i+4][1]==bb[i][1]:
##                pre(bb[i+4][0])
##            if bb[i+5][1]==bb[i][1]:
##                pre(bb[i+5][0])
##        except:
##            pass
##        time.sleep(bb[i][2]/1000-(time.time()-tt-bb[i][1]/1000))
##        time.sleep(bb[i][2]/1000)
##plt.plot(pl)
##plt.show()
##plt.scatter(plx,ply)
