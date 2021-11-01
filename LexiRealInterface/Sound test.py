import speech_recognition as sr
import requests
import time
import random
import webbrowser
import sys
from gtts import gTTS
import os
from playsound import playsound
from translate import Translator
import GoogleSearchEngine as gse

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
        

    try:
        result = r.recognize_google(audio, language = 'en-US')
        print(result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("uhh")
        
