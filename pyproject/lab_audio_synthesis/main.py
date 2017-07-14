import ccircle
import time
import random
import util
from math import *

window = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()

def sawtooth(t, f):
    return 2.0 * ((t * f) % 1.0) - 1.0

def sine(t, f):
    return sin(2.0 * pi * t * f)

def signum(int):
    if int > 0: return 1
    elif int < 0: return -1
    elif int == 0: return 0
    else: return int

def square(t, f):
    return signum(sin(t * f * 2 * pi))

duration = 3

for i in range(44100 * duration):
    t = i / 44100
    if t < 0.36:
        mysound.addSample(square(t, 220))
    elif t < 0.72:
        mysound.addSample(square(t, 207.6523487900))
    elif t < 1.08:
        mysound.addSample(square(t, 195.9977179909))
    elif t < 3.0:
        mysound.addSample(square(t, 184.9972113558))

mysound.play()
time.sleep(duration)