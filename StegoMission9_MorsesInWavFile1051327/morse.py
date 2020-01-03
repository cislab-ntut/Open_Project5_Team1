import numpy as np
import random, string
import time
from morseTable import forwardTable, DOT, DASH, DASH_WIDTH, CHAR_SPACE, WORD_SPACE

def stringToMorse(string1):
  cipher = '' 
  for letter in string1:
    if letter == '\n':
      pass
    elif letter != ' ': 
        cipher += forwardTable[letter] + ' '
    else: 
        cipher += ' '
  return cipher 

def morseSampleDuration(code, sps, wpm, fs=None):
  dps = wpmToDps(wpm)  
  baseSampleCount = sps/dps
  samplesPerDot = int(round(baseSampleCount))
  samplesPerDash = int(round(baseSampleCount * DASH_WIDTH))
  samplesBetweenElements = int(round(baseSampleCount))
  farnsworthScale = farnsworthScaleFactor(wpm, fs)
  samplesBetweenLetters = int(round(baseSampleCount * CHAR_SPACE * farnsworthScale))
  samplesBetweenWords = int(round(baseSampleCount * WORD_SPACE * farnsworthScale))

  dotArr = np.ones(samplesPerDot, dtype=np.bool)
  dashArr = np.ones(samplesPerDash, dtype=np.bool)
  eGapArr = np.zeros(samplesBetweenElements, dtype=np.bool)
  cGapArr = np.zeros(samplesBetweenLetters, dtype=np.bool)
  wGapArr = np.zeros(samplesBetweenWords, dtype=np.bool)

  duration = 0
  prevSpaces = 0
  prevWasElement = False
  for c in code:
    if (c == DOT or c == DASH) and prevWasElement:
      duration += samplesBetweenElements
    if c == DOT:
      duration += samplesPerDot
      prevSpaces, prevWasElement = 0, True
    elif c == DASH:
      duration += samplesPerDash
      prevSpaces, prevWasElement = 0, True
    else:  
      if prevSpaces == 1:
        duration += samplesBetweenWords-samplesBetweenLetters
      elif prevSpaces == 0:
        duration += samplesBetweenLetters
      prevSpaces += 1
      prevWasElement = False

  return duration

def morseToBoolArr(code, sps, wpm, fs=None):
  dps = wpmToDps(wpm)  
  baseSampleCount = sps/dps
  samplesPerDot = int(round(baseSampleCount))
  samplesPerDash = int(round(baseSampleCount * DASH_WIDTH))
  samplesBetweenElements = int(round(baseSampleCount))
  farnsworthScale = farnsworthScaleFactor(wpm, fs)
  samplesBetweenLetters = int(round(baseSampleCount * CHAR_SPACE * farnsworthScale))
  samplesBetweenWords = int(round(baseSampleCount * WORD_SPACE * farnsworthScale))

  dotArr = np.ones(samplesPerDot, dtype=np.bool)
  dashArr = np.ones(samplesPerDash, dtype=np.bool)
  eGapArr = np.zeros(samplesBetweenElements, dtype=np.bool)
  cGapArr = np.zeros(samplesBetweenLetters, dtype=np.bool)
  wGapArr = np.zeros(samplesBetweenWords, dtype=np.bool)

  pieces = []
  prevWasSpace = False
  prevWasElement = False
  for c in code:
    if (c == DOT or c == DASH) and prevWasElement:
      pieces.append(eGapArr)
    if c == DOT:
      pieces.append(dotArr)
      prevWasSpace, prevWasElement = False, True
    elif c == DASH:
      pieces.append(dashArr)
      prevWasSpace, prevWasElement = False, True
    else:  
      if prevWasSpace:
        pieces[-1] = wGapArr
      else:
        pieces.append(cGapArr)
      prevWasSpace, prevWasElement = True, False

  return np.concatenate(pieces)

def wpmToDps(wpm): 
  return wpm*50/60.0
def farnsworthScaleFactor(wpm, fs=None): 
  if fs is None:
    return 1  
  slowWordInterval = 1.0/fs 
  standardWordInterval = 1.0/wpm
  extraSpace = slowWordInterval-standardWordInterval
  extraSpaceDots = (extraSpace/standardWordInterval) * (9+10+4*DASH_WIDTH+4*CHAR_SPACE+WORD_SPACE)
  standardSpaceDots = 4*CHAR_SPACE + WORD_SPACE  
  totalSpaceDots = standardSpaceDots + extraSpaceDots
  scaleFactor = totalSpaceDots / standardSpaceDots
  if scaleFactor < 1:
    return 1
  return scaleFactor

def main():
  message = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(11))
  result = stringToMorse(message.upper()) 
  print (result)

if __name__ == '__main__':
    main()