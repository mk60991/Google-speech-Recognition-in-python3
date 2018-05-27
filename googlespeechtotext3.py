# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:30:12 2018

@author: hp
"""

import speech_recognition as sr
import webbrowser as wb
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r=sr.Recognizer()
with sr.Microphone() as source:
    print('say somethoing')
    audio=r.listen(source)
    print('done')
    
    

try:
    text=r.recognize_google(audio)
    print('google think you said:\n'+ text)
    f_text='https://www.google.co.in/search?q=' + text
    wb.get(chrome_path).open(f_text)

except Exception as e:
    print(e)
        