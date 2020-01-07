import numpy as np
import matplotlib.pyplot as plt
import os
import wave
 #
import sys
import time
import Image
import ImageGrab

path = "C://Users\Thomas\Desktop\網安project_5"
name = '2.wav'
filename = os.path.join(path, name)
 
f = wave.open(filename,'rb')

params = f.getparams()
nchannels, sampwidth, framerate,nframes = params[:4]


strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.short)

waveData = waveData * 1.0/max(abs(waveData))

waveData = np.reshape(waveData,[nframes,nchannels]).T 
f.close()

time = np.arange(0,nframes) * (1.0 / framerate)
time= np.reshape(time,[nframes,1]).T
plt.plot(time[0,:nframes],waveData[0,:nframes],c="b")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Original wave")
#plt.show() 頻譜圖
framelength = 10#時間軸取樣寬度
framesize = framelength*framerate 
 
nfftdict = {}
lists = [32,64,128,256,512,1024]
for i in lists:
    nfftdict[i] = abs(framesize - i)
sortlist = sorted(nfftdict.items(), key=lambda x: x[1])
framesize = int(sortlist[0][0])
 
NFFT = framesize
overlapSize = 1.0/3 * framesize
overlapSize = int(round(overlapSize))

spectrum,freqs,ts,fig = plt.specgram(waveData[0],NFFT = NFFT,Fs =framerate,window=np.hanning(M = framesize),noverlap=overlapSize,mode='default',scale_by_freq=True,sides='default',scale='dB',xextent=None)#绘制频谱图
          
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.title("Spectrogram")
plt.show() #時頻圖