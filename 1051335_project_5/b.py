from wavreader import WAVFile as reader
from collections import Counter
from math import log
import time as t
import sys

fpath = "2.wav"
newname = "22.wav"
hmsg = "some sample test string to hide"

start_marker = "STARTINGTRANSMISSION"*4
end_marker = "ENDINGTRANSMISSION"*4
start_bit = 0

def hideBit(sampleNo, character, counter, higher_limit, flag=False):
    global bitcount
    global audiofile

    audiofile.Data[sampleNo] = ((audiofile.Data[sampleNo] >> 1) << 1) | (character >> bitcount) & 0x01 # Podmiana LSB na bit znaku wiadomosci
    if bitcount > 0 :
        bitcount = bitcount - 1
    elif counter < higher_limit:
        bitcount = 7
        counter = counter + 1
    else:
        counter = 0
        bitcount = 7
        flag = True
    return counter, flag

def entropyfast(s):
    return -sum(i/float(len(s)) * log(i/float(len(s)),2) for i in Counter(s).values())

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange

sys.stdout.flush()
audiofile = reader(fpath)
audiofile.Data.flags.writeable = True
#data = np.reshape(audiofile.Data, len(audiofile.Data)*audiofile.NumChannels)
print G+"\t[DONE]"+W

print O+"Calculating data..."+W,
sys.stdout.flush()
avail_bits = audiofile.Subchunk2Size
required_bits = (len(hmsg) + len(start_marker) + len(end_marker))*8
print G+"\t[DONE]"+W

if( required_bits > avail_bits/8):
    print R+"\nERROR! Message is too long!"+W
    print "Available BYTES:\t", avail_bits/8
    print "Required BYTES: \t", required_bits

else:
    print "\nUse entropy detection coding? y/n:\n"+R+"[WARNING]"+W+" This will significantly extend the execution time!"
    ent_answer = raw_input("Answer: ")
    ent_time = None
    if ent_answer == ("y" or "Y"):
        ent_time = t.clock()
        perc = 0
        ent = 0
        data_len = len(audiofile.Data)
        for sampleStart in xrange(0,data_len-required_bits):
            e = entropyfast(audiofile.Data[sampleStart:sampleStart+required_bits])
            p = 100*sampleStart/float(data_len)
            print "\r",
            if (p - perc >= 0.1) or perc == 0 or perc == 100:
                perc = p
                print O+"Calculating best place for message: "+G+format(perc,".1f")+O+"%"+W,
            if e > ent:
                ent = e
                start_bit = sampleStart

        print "\r",
        print O+"Calculating best place for message: "+G+100.0+O+"%"+W,
        print "\nBest place found at: "+str(start_bit)+" sample!"
    elif not ent_answer == ("n" or "N"):
        print R+"\nUnknown answer!"+W
        exit()
    # Flags:
    sm_done = False     #Starting Markers Done
    msg_done = False    #Message Done
    fn_done = False

    bitcount = 7
    charcount = 0
    markercount = 0

    print O+"\nHiding your message..."+W+"\t",
    sys.stdout.flush()
    before = t.clock()
    for sampleNo in xrange(start_bit, start_bit+required_bits):
        if not sm_done :
            markercount, sm_done = hideBit(sampleNo, ord(start_marker[markercount]), markercount, len(start_marker)-1)
        elif not msg_done:
            charcount, msg_done = hideBit(sampleNo, ord(hmsg[charcount]), charcount, len(hmsg)-1)
        elif not fn_done:
            markercount, fn_done = hideBit(sampleNo, ord(end_marker[markercount]), markercount, len(end_marker)-1)
    print G+"[DONE]"+W
    after = t.clock()

    print O+"Saving result..."+W+"\t",
    audiofile.SaveTo(newname)
    print G+"[DONE]"+W

    print G+"\nMessage hidden successfuly!"+W
    if not ent_time == None:
        print G+"Entropy calculation took: "+str(before-ent_time)+" seconds!"+W
    print G+"Hiding took "+ str(after-before) +" seconds!"+W