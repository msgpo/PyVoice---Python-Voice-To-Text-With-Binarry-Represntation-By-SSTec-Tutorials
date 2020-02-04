#This Project is develop by mehedi shakeel
print("##########################################################################")
print("Project : Bangla & English Voice To Text using Python")
print("Name    : Md Mehedi Hasan")
print("ID      : 16201073")
print("##########################################################################")
print("")
import os
import time
from playsound import playsound
import speech_recognition as sr
import binascii
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


#Bangla Voice To Text Code using Python With Google Cloud Speech API

r = sr.Recognizer()
voice = 'audio.wav'
with sr.AudioFile(voice) as source:
    print("Listening the Bengali audio file....")
    playsound('audio.wav')
    audio = r.listen(source)
    text = r.recognize_google(audio, language = 'bn-BD')
    print (text)
    shakeel = (text)
    print("")
    print("Binarry Represntation : ")
    print("")
    print(' '.join(format(ord(x), 'b') for x in shakeel))
print("##########################################################################")

#Bangla Voice To Text Code using Python With Google Cloud Speech API

voice = 'audio2.wav'
with sr.AudioFile(voice) as source:
    print("Listening the English audio file....")
    playsound('audio2.wav')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print (text)
    shakeel = (text)
    print("")
    print("Binarry Represntation :")
    print("")
    print(' '.join(format(ord(x), 'b') for x in shakeel))

print("##########################################################################")

#SHOW WAVE FORM OF AUDIO 1
spf = wave.open('audio.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

plt.figure(1)
plt.title('Bangla Voice Analog Wave...')
plt.plot(signal)




#SHOW WAVE FORM OF AUDIO 2
spf = wave.open('audio2.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

plt.figure(2)
plt.title('English Audio Analog Wave...')
plt.plot(signal)
time.sleep(3)
plt.show()













