# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:15:50 2018

@author: hp
"""

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('say somethiong')
    audio=r.listen(source)
    
try:
    print('google thinks you said:\n'+r.recognize_google(audio))
    
except:
    pass