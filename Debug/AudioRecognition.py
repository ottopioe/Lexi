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

##Syllabus:
##Moods: 1=bad, 2=not great, 3=fine, 4=good,5=great

#Variables
answer = True
first = True
noAnswer = False
count = 0
previousResult= "....."
newResult = "....."
r = sr.Recognizer()

localtime = time.localtime()
hours = int(time.strftime("%H"))
minutes = int(time.strftime("%M"))
seconds = int(time.strftime("%S"))
mood = random.randint(1,5)


def searchList(string, array):
    n = 0
    while string != array[0]:
        n = n+1

    return n

def appData():
    f = open("AppData.txt", "r")
    for each in f:
        if each.find("close = True") > -1:
            close = True
            sys.exit()
    f.close()

def upload(content):
    cleared = True
    if cleared == True:
        f = open("AppData.txt", "w")
        f.write(content)
        f.close
        

def japanese(resultList):
    word=""
    translator = Translator(from_lang="english",to_lang="Japanese")
    for x in range (len(resultList)-3):
        word = word + resultList[x+1] + " "
    translation = translator.translate(word)
    tts = gTTS(translation, lang="ja")
    return translation

def korean(resultList):
    word=""
    translator = Translator(from_lang="english",to_lang="Korean")
    for x in range (len(resultList)-3):
        word = word + resultList[x+1] + " "
    translation = translator.translate(word)
    tts = gTTS(translation, lang="ko")
    return translation

def spanish(resultList):
    word=""
    translator = Translator(from_lang="english",to_lang="Spanish")
    for x in range (len(resultList)-3):
        word = word + resultList[x+1] + " "
    translation = translator.translate(word)
    tts = gTTS(translation, lang="es")
    return translation

def german(resultList):
    word=""
    translator = Translator(from_lang="english",to_lang="German")
    for x in range (len(resultList)-3):
        word = word + resultList[x+1] + " "
    translation = translator.translate(word)
    tts = gTTS(translation)
    return translation

def french(resultList):
    word=""
    translator = Translator(from_lang="english",to_lang="French")
    for x in range (len(resultList)-3):
        word = word + resultList[x+1] + " "
    translation = translator.translate(word)
    tts = gTTS(translation, lang="fr")
    return translation

f = open("AppData.txt", "w")
f.close()

print("[ RUNNING ... ] \n")
print('Please say the name "Lexi" for it to respond\n'
    'Then follow up with a question or a task\n'
     'Use the "Help" command to see what features Lexi has\n')

mic = sr.Microphone()
    
while answer==True:
    appData()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    if minutes > int(time.strftime("%M")) and hours < int(time.strftime("%H")):
       mood = random.randint(1,5)
    
    
    try:
        result = r.recognize_google(audio, language = 'en-US')
        print(result)
        if result.find("Lexi") > -1 or result.find("Alexi") > -1:
            count = count + 1
            tts = gTTS('yes?')
            tts.save('yes' + str(count) + '.mp3')
            playsound('yes' + str(count) + '.mp3')
            os.remove('yes' + str(count) + '.mp3')

            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)             

            try:
                result = r.recognize_google(audio, language = 'en-US')
                if result.find("how about now") > -1 or result.find("repeat") > -1 or result.find("again") > -1:
                    newResult = result
                    result = previousResult

                if result.startswith("translate") == True or result.startswith("Translate") == True:
                    resultList = result.split()
                    result = result.lower()
                    if result.find("japanese") > -1:
                        translation = japanese(resultList)
                        
                    if result.find("korean") > -1:
                        translation = korean(resultList)

                    if result.find("spanish") > -1:
                        translation = spanish(resultList)

                    if result.find("german") > -1:
                        translation = spanish(resultList)

                    if result.find("french") > -1:
                        translation = french(resultList)
                        
                    upload(translation)
                    
                elif result.find("how are you") > -1:
                    if mood == 5:
                        tts = gTTS("I am doing fantastic")
                        upload("I am doing fantastic\n")
                    elif mood == 4:
                        tts = gTTS("I'm good")
                        upload("I'm good\n")
                    elif mood == 3:
                        tts = gTTS("I'm doing alright")
                        upload("I'm doing alright\n")
                    elif mood == 2:
                        tts = gTTS("Could be doing better")
                        upload("Could be doing better\n")
                    elif mood == 1:
                        tts = gTTS("Unfortunately, I'm not feeling so great right now")
                        upload("Unfortunately, I'm not feeling so great right now\n")
                    
                elif result.find("hello") > -1 or result.find("hi") > -1 or result == "hey":
                    if random.randint(1,2) == 1:
                        tts = gTTS("Hello")
                        upload("Hello\n")
                    else:
                        tts = gTTS("Hey there!")
                        upload("Hey there!\n")
                        
                elif result == "music":
                    upload("I can play: \n"
                          "Classical\n"
                          "Gaming music\n"
                          "Pop music\n"
                          "Electronic music\n"
                          "Hip hop music\n")
                    tts = gTTS("I can play any of these")
                    
                elif result == "play music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/1MYLEOSjkbD0z7ib7kQmbj')
                    tts = gTTS("Playing anime music")
                elif result == "play classical music" or result == "play relaxing music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/37i9dQZF1DWXWpqXjufFrg')
                    tts = gTTS("Playing classical music")
                elif result == "play gaming music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/6QFfy4mF3bmsiatWwbQj6j')
                    tts = gTTS("Playing gaming music")
                elif result == "play pop music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/37i9dQZF1DXbYM3nMM0oPk')
                    tts = gTTS("Playing pop music")
                elif result == "play electronic music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO')
                    tts = gTTS("Playing electronic music")
                elif result == "play hip hop" or result == "play hip hop music":
                    webbrowser.open_new_tab('https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd')
                    tts = gTTS("Playing rap music")

                elif result.find("slap") > -1 or result.find("slab") > -1:
                    resultList = result.split()
                    tts = gTTS("slapping " + resultList[1])
                    upload("Slapping " + resultList[1] + "...")

                elif result.find("number") > -1 and result.find("between") > -1 and result.find("and"):
                    resultList = result.split()
                    number = resultList.index("and")
                    num = random.randint(int(resultList[number - 1]), int(resultList[number + 1]))
                    tts = gTTS(str(num))
                    upload("Your number is: " + str(num))

                elif result.find("time") > -1:
                    tts = gTTS("It's " + str(time.strftime("%H")) + ":" + str(time.strftime("%M")))
                    upload(str(time.strftime("%H")) + ":" + str(time.strftime("%M")) + "\n")

                elif result.find("divide") > -1 or result.find("add") > -1 or result.find("subtract") > -1 or result.find("multiply") > -1 or result.find("-") > -1:
                    resultList = result.split()
                    if result.find("divide") > -1:
                        x = resultList.index("by")
                        mathanswer = int(resultList[x-1]) / int(resultList[x+1])
                        upload(mathanswer)
                        
                    if result.find("times") > -1 or result.find("multiply") > -1:
                        x = resultList.index("times")
                        mathanswer = int(resultList[x-1]) * int(resultList[x+1])
                        upload(mathanswer)

                    if result.find("add") > -1:
                        x = resultList.index("and")
                        mathanswer = int(resultList[x-1]) + int(resultList[x+1])
                        upload(mathanswer)
    
                    if result.find("subtract") > -1:
                        x = resultList.index("from")
                        mathanswer = int(resultList[x+1]) - int(resultList[x-1])
                        upload(mathanswer)

                    if result.find("-") > -1:
                        x = resultList.index("-")
                        mathanswer = int(resultList[x-1]) - int(resultList[x+1])
                        upload(mathanswer)
                    tts = gTTS(str(mathanswer))

                elif result.find("maths") > -1:
                    upload("Divide ___ by ___ \n"
                          "Multiply ___ times ___ \n"
                          "Add ___ and ___ \n"
                          " ___ minus ___ \n")

                elif result.find("search") > -1 or result.find("what") > -1 or result.find("what's") > -1 or result.find("how") > -1:
                    ans = gse.func(result)
                    ans = ans[1]
                    upload(ans + ".\n")
                    ans = ans.split(".")
                    tts = gTTS(ans[0])
                        
                elif result == "help":
                    upload("Functions: \n"
                          "1. Hello \n"
                          "2. How are you \n"
                          "3. How about now/repeat \n"
                          "4. Play (type) music \n"
                          '5. Ask for anything online by saying "search..."\n'
                          "6. Time \n"
                          "7. Basic maths ('Maths' function for more info)\n"
                          "8. Translate (phrase) to (language) \n"
                          "9. A number between ___ and ___ \n")

                elif result == "exit" or result == "quit" or  result == "stop":
                    sys.exit()
                    
                else:
                    upload("No answer to:", result, "\n")
                    noAnswer = True

                if noAnswer == False:
                    tts.save('result' + str(count) + '.mp3')
                    playsound('result' + str(count) + '.mp3')
                    os.remove('result' + str(count) + '.mp3')

                noAnswer = False
                
                if first == True:
                    first = False
                    previousResult = result
                else:
                    previousResult = newResult
                    
            except sr.UnknownValueError:
                upload("Repeat that please \n")
            except sr.RequestError as e:
                continue
            

            
    except sr.UnknownValueError:
        error = True
    except sr.RequestError as e:
        continue

