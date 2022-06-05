# import pyttsx3 as ptx
# import speech_recognition as sr
# import webbrowser
# import datetime
# import wikipedia
# import pyjokes
# import os
# import ctypes
# import requests
# import subprocess
# from urllib.request import urlopen
# import json
# from ecapture import ecapture as ec
# import time
# import winshell
# import wolframalpha
# from cv2 import *
# from calculator.simple import SimpleCalculator
# from eng_hindi import eth
# from playsound import playsound
# from googletrans import Translator
# from gtts import gTTS
# import os
# flag = 0
#
# dic = ('afrikaans', 'af', 'albanian', 'sq',
#        'amharic', 'am', 'arabic', 'ar',
#        'armenian', 'hy', 'azerbaijani', 'az',
#        'basque', 'eu', 'belarusian', 'be',
#        'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
#        'bg', 'catalan', 'ca', 'cebuano',
#        'ceb', 'chichewa', 'ny', 'chinese (simplified)',
#        'zh-cn', 'chinese (traditional)',
#        'zh-tw', 'corsican', 'co', 'croatian', 'hr',
#        'czech', 'cs', 'danish', 'da', 'dutch',
#        'nl', 'english', 'en', 'esperanto', 'eo',
#        'estonian', 'et', 'filipino', 'tl', 'finnish',
#        'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
#        'gl', 'georgian', 'ka', 'german',
#        'de', 'greek', 'el', 'gujarati', 'gu',
#        'haitian creole', 'ht', 'hausa', 'ha',
#        'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
#        'hi', 'hmong', 'hmn', 'hungarian',
#        'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
#        'id', 'irish', 'ga', 'italian',
#        'it', 'japanese', 'ja', 'javanese', 'jw',
#        'kannada', 'kn', 'kazakh', 'kk', 'khmer',
#        'km', 'korean', 'ko', 'kurdish (kurmanji)',
#        'ku', 'kyrgyz', 'ky', 'lao', 'lo',
#        'latin', 'la', 'latvian', 'lv', 'lithuanian',
#        'lt', 'luxembourgish', 'lb',
#        'macedonian', 'mk', 'malagasy', 'mg', 'malay',
#        'ms', 'malayalam', 'ml', 'maltese',
#        'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
#        'mn', 'myanmar (burmese)', 'my',
#        'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
#        'pashto', 'ps', 'persian', 'fa',
#        'polish', 'pl', 'portuguese', 'pt', 'punjabi',
#        'pa', 'romanian', 'ro', 'russian',
#        'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
#        'serbian', 'sr', 'sesotho', 'st',
#        'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
#        'slovak', 'sk', 'slovenian', 'sl',
#        'somali', 'so', 'spanish', 'es', 'sundanese',
#        'su', 'swahili', 'sw', 'swedish',
#        'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
#        'te', 'thai', 'th', 'turkish',
#        'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
#        'ug', 'uzbek',  'uz',
#        'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
#        'yiddish', 'yi', 'yoruba',
#        'yo', 'zulu', 'zu')
#
#
# def wish_me():
#     hour = int(datetime.datetime.now().hour)
#     name = "alexa"
#     if 0 <= hour < 12:
#         voice_change("Good Morning Sir !")
#
#     elif 12 <= hour < 18:
#         voice_change("Good Afternoon Sir !")
#
#     else:
#         voice_change("Good Evening Sir !")
#
#     voice_change("I am your Assistant. "+name)
#
#
# def username():
#     voice_change("What should i call you sir")
#     u_name = query().lower()
#     voice_change("Welcome Mister. "+u_name)
#     voice_change("How can i Help you, Sir")
#
#
# def speech_to_text():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening.....")
#         r.pause_threshold = 0.8
#         audio = r.listen(source)
#     try:
#         print("Recognizing.....")
#         sentence = r.recognize_google(audio, language='en-in')
#         print(f"The User said {sentence}\n")
#     except Exception as e:
#         text_to_speech("say that again please.....")
#         print(e)
#         return "None"
#     return sentence
#
#
# def text_to_speech(word):
#     alexa = ptx.init('sapi5')
#     voices = alexa.getProperty('voices')
#     alexa.setProperty('voice', voices[1].id)
#     rate = alexa.getProperty('rate')
#     alexa.setProperty('rate', 100)
#     alexa.say(word)
#     alexa.runAndWait()
#
#
# def query():
#     while True:
#         s = speech_to_text().lower()
#         while s == 'None':
#             s = speech_to_text()
#         return s
#
#
# def destination_language():
#     print("Enter the language in which you want to convert : Example. Hindi , English , etc.")
#     text_to_speech("Enter the language in which you want to convert : Ex. Hindi , English , etc.")
#     lang = query().lower()
#     while lang == "None":
#         lang = query().lower()
#     lang = lang.lower()
#     return lang
#
#
# to_lang = destination_language()
#
# # # Mapping it with the code
# while to_lang not in dic:
#     text_to_speech("Language in which you are trying\
#     to convert is currently not available ,\
#     please input some other language")
#     print()
#     to_lang = destination_language()
#
# to_lang = dic[dic.index(to_lang) + 1]
#
#
# def voice_change(word):
#     translator = Translator()
#     text_to_translate = translator.translate(word, dest=to_lang)
#     print(text_to_translate)
#     text = text_to_translate.text
#     print(text)
#     speak = gTTS(text=text, lang=to_lang, slow=False)
#     sound = 'voice.mp3'
#     speak.save(sound)
#     playsound(sound)
#     os.remove(sound)
#
#
# def calculator():
#     voice_change("what's you want to calculate ")
#     condition = speech_to_text().lower()
#     print(condition)
#     webbrowser.open('https://www.google.com/search?q='+condition.strip())
#     c = SimpleCalculator()
#     c.run(condition)
#     voice_change('the answer is')
#     voice_change("{:.2f}".format(c.lcd))
#
#
# def clear():
#     return lambda: os.system('cls')
#
#
# if __name__ == '__main__':
#     a_name = 'alexa'
#     clear()
#     wish_me()
#     username()
#     while True:
#         command = query().lower()
#         if 'time' in command:
#             times = datetime.datetime.now().strftime('%H:%M')
#             voice_change("Sir, the time is."+times)
#             print(times)
#         elif 'open' in command:
#             my_command = command.replace('open', '')
#             my_command1 = my_command.strip()
#             url = 'www.'+my_command1+'.com'
#             webbrowser.open(url)
#             voice_change("Here you go to."+my_command1)
#
#         elif 'wikipedia' in command:
#             my_command = command.replace('wikipedia', '')
#             wiki = my_command.strip()
#             url = 'wikipedia.com'
#             webbrowser.open(url)
#             voice_change("Here you go to."+wiki+'wikipedia')
#             info = wikipedia.summary(wiki, 3)
#             voice_change(info)
#             voice_change("thank you.")
#
#         elif 'youtube' in command:
#             my_command = command.replace('youtube', '')
#             video = my_command.strip()
#             url = 'www.youtube.com/results?search_query='+video
#             webbrowser.open(url)
#             voice_change("Here you go to youtube. "+video+'video')
#
#         elif 'who is' in command or 'what is':
#             my_command = command.replace('who is', '').replace('what is', '')
#             person = my_command.strip()
#             url = 'https://www.google.com/search?q='+person
#             webbrowser.open(url)
#             info = wikipedia.summary(person, sentences=3)
#             print(info)
#             voice_change("According to Wikipedia. "+info)
#
#         elif 'play' in command:
#             my_command = command.replace('play', '')
#             song = my_command.strip()
#             url = 'https://open.spotify.com/search/'+song
#             webbrowser.open(url)
#             voice_change("Here you go to spotify. "+song)
#
#         elif 'how are you' in command:
#             voice_change("I am fine, Thank you.")
#             voice_change("How are you, Sir")
#
#         elif 'fine' in command or "good" in command:
#             voice_change("It's good to know that your fine. ")
#
#         elif "what's your name" in command or "What is your name" in command:
#             voice_change("My friends call me."+a_name)
#
#         elif 'exit' in command or 'stop' in command:
#             voice_change("Thanks for giving me your time.")
#             exit()
#
#         elif "made you" in command or "created you" in command:
#             voice_change("I have been created by Mister. Koushik.")
#
#         elif 'joke' in command:
#             voice_change(pyjokes.get_joke())
#
#         elif "who i am" in command:
#             voice_change("If you talk then definitely your human.")
#
#         elif "why you came to world" in command:
#             voice_change("Thanks to Gaurav. further It's a secret.")
#
#         elif 'is love' in command:
#             voice_change("It is 7th sense that destroy all other senses.")
#
#         elif "who are you" in command:
#             voice_change("I am your virtual assistant created by Gaurav")
#
#         elif 'reason for you' in command:
#             voice_change("I was created as a Minor project by Mister Gaurav .")
#
#         elif 'change background' in command:
#             ctypes.windll.user32.SystemParametersInfoW(20, 0, "K:/images", 0)
#             voice_change("Background changed successfully.")
#
#         elif 'news' in command:
#             try:
#                 jsonObj = urlopen(
#                     '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=d6d358ebfaf7445b98163e2537672f74''')
#                 data = json.load(jsonObj)
#                 i = 1
#
#                 voice_change('here are some top news from the times of india.')
#                 print('''=============== TIMES OF INDIA ============''' + '\n')
#
#                 for item in data['articles']:
#                     print(str(i) + '. ' + item['title'] + '\n')
#                     print(item['description'] + '\n')
#                     voice_change(str(i) + '. ' + item['title'] + '\n')
#                     i += 1
#             except Exception as e:
#                 print(str(e))
#
#         elif 'lock window' in command:
#             voice_change("locking the device.")
#             ctypes.windll.user32.LockWorkStation()
#
#         elif 'shutdown system' in command:
#             voice_change("Hold On a Sec ! Your system is on its way to shut down.")
#             subprocess.call('shutdown/p/f')
#
#         elif 'empty recycle bin' in command:
#             winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
#             voice_change("Recycle Bin Recycled")
#
#         elif "don't listen" in command or "stop listening" in command:
#             voice_change("for how much time you want to stop alexa from listening commands.")
#             a = int(speech_to_text())
#             time.sleep(a)
#             print(a)
#
#         elif "where is" in command:
#             query = command.replace("where is", "")
#             location = query
#             voice_change("User asked to Locate"+location)
#             webbrowser.open("https://www.google.nl/maps/place/"+location+"")
#
#         elif "camera" in command or "take a photo" in command:
#             ec.capture(0, "alexa Camera ", "img.jpg")
#
#         elif "restart" in command:
#             subprocess.call(["shutdown", "/r"])
#
#         elif "hibernate" in command or "sleep" in command:
#             voice_change("Hibernating.")
#             subprocess.call("shutdown / h")
#
#         elif "write a note" in command:
#             voice_change("What should i write, sir")
#             note = speech_to_text()
#             file = open('alexa.txt', 'w')
#             voice_change("Sir, Should i include date and time.")
#             snfm = speech_to_text()
#             if 'yes' in snfm or 'sure' in snfm:
#                 strTime = datetime.datetime.now().strftime("% H:% M:% S")
#                 file.write(strTime)
#                 file.write(" :- ")
#                 file.write(note)
#             else:
#                 file.write(note)
#
#         elif "show note" in command:
#             voice_change("Showing Notes.")
#             file = open("alexa.txt", "r")
#             print(file.read())
#             voice_change(file.read(6))
#
#         elif "alexa" in command:
#             wish_me()
#             voice_change("alexa 1 point o in your service Mister. koushik")
#
#         elif "weather" in command:
#             # Google Open weather website
#             # to get API of Open weather
#             api_key = "4a7c767ebc36b6d9cee7ab625d940e83"
#             base_url = "http://api.openweathermap.org/data/2.5/weather?"
#             voice_change("What is the City name ")
#             print("City name : ")
#             city_name = speech_to_text()
#             complete_url = base_url+"q="+city_name+"&appid="+api_key
#             response = requests.get(complete_url)
#             x = response.json()
#
#             if x["cod"] != "404":
#                 y = x["main"]
#                 current_temperature = float("{:.2f}".format(y["temp"]))
#                 current_pressure = y["pressure"]
#                 current_humidity = y["humidity"]
#                 z = x["weather"]
#                 weather_description = z[0]["description"]
#                 print(" Temperature (in Celsius unit) = " + str(
#                     current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) =" + str(
#                     current_pressure) + "\n humidity (in percentage) = " + str(
#                     current_humidity) + "\n description = " + str(weather_description))
#
#                 voice_change(" Temperature (in Celsius unit) is " + str(
#                     current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) is" + str(
#                     current_pressure) + "\n humidity (in percentage) is " + str(
#                     current_humidity) + "\n description = " + str(weather_description))
#
#             else:
#                 voice_change(" City Not Found .")
#
#         elif "Good Morning" in command:
#             voice_change("A warm" + command)
#             voice_change("How are you Mister"+a_name)
#
#             # most asked question from google Assistant
#         elif "will you be my gf" in command or "will you be my bf" in command:
#             voice_change("I'm not sure about, may be you should give me some time.")
#
#         elif "how are you" in command:
#             voice_change("I'm fine, glad you me that")
#
#         elif "i love you" in command:
#             voice_change("It's hard to understand")
#
#         elif 'calculate' in command or 'calculator' in command:
#             calculator()
#
#         elif "what is" in command or "who is" in command:
#             app_id = 'PJ6553-EX5KRG2HE5'
#             client = wolframalpha.Client(app_id)
#             res = client.query(command)
#             try:
#                 print(next(res.results).text)
#                 speech_to_text(next(res.results).txt)
#             except StopIteration:
#                 print("No results")
#         time.sleep(10)
#         #
#         # else:
#         #     continue


# -------------------------xxxxx--------------------------------

import pyttsx3 as ptx
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyjokes
import os
import ctypes
import requests
import subprocess
from urllib.request import urlopen
import json
from ecapture import ecapture as ec
import time
import winshell
import wolframalpha
from cv2 import *
from calculator.simple import SimpleCalculator
from eng_hindi import eth
from playsound import playsound
from googletrans import Translator
from gtts import gTTS
import os
flag = 0

dic = ('afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek',  'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')


def wish_me():
    hour = int(datetime.datetime.now().hour)
    name = "alexa"
    if 0 <= hour < 12:
        voice_change("Good Morning Sir !")
    elif 12 <= hour < 18:
        voice_change("Good Afternoon Sir !")
    else:
        voice_change("Good Evening Sir !")
    voice_change("I am your Assistant. " + name)


def username():
    voice_change("What should i call you sir")
    u_name = query().lower()
    voice_change("Welcome Mister. " + u_name)
    voice_change("How can i Help you, Sir")


def query():
    while True:
        s = speech_to_text().lower()
        while s == 'None':
            s = speech_to_text().lower()
        return s


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        sentence = ''
    try:
        sentence = r.recognize_google(audio, language='en-in')
        print(f"The User said {sentence}\n")
    except sr.UnknownValueError:
        text_to_speech("say that again please.....")
    except sr.RequestError:
        text_to_speech('sorry, no internet connection...')
    return sentence


def text_to_speech(word):
    alexa = ptx.init('sapi5')
    voices = alexa.getProperty('voices')
    alexa.setProperty('voice', voices[1].id)
    rate = alexa.getProperty('rate')
    alexa.setProperty('rate', 100)
    alexa.say(word)
    alexa.runAndWait()


def destination_language():
    print("Enter the language in which you want to convert : Example. Hindi , English , etc.")
    text_to_speech("Enter the language in which you want to convert : Example. Hindi , English , etc.")
    lang = speech_to_text().lower()
    while lang == "None":
        lang = speech_to_text().lower()
        lang = lang.lower()
    return lang


to_lang = destination_language()

# # Mapping it with the code
while to_lang not in dic:
    text_to_speech("Language in which you are trying\
    to convert is currently not available ,\
    please input some other language")
    print()
    to_lang = destination_language()

to_lang = dic[dic.index(to_lang) + 1]


def voice_change(word):
    translator = Translator()
    text_to_translate = translator.translate(word, dest=to_lang)
    print(text_to_translate)
    text = text_to_translate.text
    print(text)
    speak = gTTS(text=text, lang=to_lang, slow=False)
    sound = 'voice.mp3'
    speak.save(sound)
    playsound(sound)
    os.remove(sound)


def calculator():
    voice_change("what's you want to calculate ")
    condition = speech_to_text().lower()
    print(condition)
    webbrowser.open('https://www.google.com/search?q='+condition.strip())
    c = SimpleCalculator()
    c.run(condition)
    voice_change('the answer is')
    voice_change("{:.2f}".format(c.lcd))


def clear():
    return lambda: os.system('cls')


if __name__ == '__main__':
    clear()
    wish_me()
    username()
    while True:
        command = query().lower()
        if 'time' in command:
            times = datetime.datetime.now().strftime('%H:%M')
            voice_change("Sir, the time is."+times)
            print(times)
        elif 'open' in command:
            my_command = command.replace('open', '')
            my_command1 = my_command.strip()
            url = 'www.'+my_command1+'.com'
            webbrowser.open(url)
            voice_change("Here you go to."+my_command1)
        elif 'wikipedia' in command:
            my_command = command.replace('wikipedia', '')
            wiki = my_command.strip()
            url = 'wikipedia.com'
            webbrowser.open(url)
            voice_change("Here you go to."+wiki+'wikipedia')
            info = wikipedia.summary(wiki, 3)
            voice_change(info)
            voice_change("thank you.")
        elif 'youtube' in command:
            my_command = command.replace('youtube', '')
            video = my_command.strip()
            url = 'www.youtube.com/results?search_query='+video
            webbrowser.open(url)
            voice_change("Here you go to youtube. "+video+'video')
        elif 'who is' in command or 'what is':
            my_command = command.replace('who is', '').replace('what is', '')
            person = my_command.strip()
            url = 'https://www.google.com/search?q='+person
            webbrowser.open(url)
            info = wikipedia.summary(person, sentences=3)
            print(info)
            voice_change("According to Wikipedia. "+info)
        elif 'play' in command:
            my_command = command.replace('play', '')
            song = my_command.strip()
            url = 'https://open.spotify.com/search/'+song
            webbrowser.open(url)
            voice_change("Here you go to spotify. "+song)
        elif 'how are you' in command:
            voice_change("I am fine, Thank you.")
            voice_change("How are you, Sir")
        elif 'fine' in command or "good" in command:
            voice_change("It's good to know that your fine. ")
        elif "what's your name" in command or "What is your name" in command:
            voice_change("My friends call me. alexa")
        elif 'exit' in command or 'stop' in command:
            voice_change("Thanks for giving me your time.")
            exit()
        elif "made you" in command or "created you" in command:
            voice_change("I have been created by Mister. Koushik.")
        elif 'joke' in command:
            voice_change(pyjokes.get_joke())
        elif "who i am" in command:
            voice_change("If you talk then definitely your human.")
        elif "why you came to world" in command:
            voice_change("Thanks to Gaurav. further It's a secret.")
        elif 'is love' in command:
            voice_change("It is 7th sense that destroy all other senses.")
        elif "who are you" in command:
            voice_change("I am your virtual assistant created by Gaurav")
        elif 'reason for you' in command:
            voice_change("I was created as a Minor project by Mister Gaurav .")
        elif 'change background' in command:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "K:/images", 0)
            voice_change("Background changed successfully.")
        elif 'news' in command:
            try:
                jsonobj = urlopen(
                    '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=d6d358ebfaf7445b98163e2537672f74''')
                data = json.load(jsonobj)
                i = 1
                voice_change('here are some top news from the times of india.')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    voice_change(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
        elif 'lock window' in command:
            voice_change("locking the device.")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in command:
            voice_change("Hold On a Sec ! Your system is on its way to shut down.")
            subprocess.call('shutdown/p/f')
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            voice_change("Recycle Bin Recycled")
        elif "don't listen" in command or "stop listening" in command:
            voice_change("for how much time you want to stop alexa from listening commands.")
            a = int(speech_to_text())
            time.sleep(a)
            print(a)
        elif "where is" in command:
            location = command.replace("where is", "")
            voice_change("User asked to Locate"+location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")
        elif "camera" in command or "take a photo" in command:
            ec.capture(0, "alexa Camera ", "img.jpg")
        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in command or "sleep" in command:
            voice_change("Hibernating.")
            subprocess.call("shutdown / h")
        elif "write a note" in command:
            voice_change("What should i write, sir")
            note = speech_to_text()
            file = open('alexa.txt', 'w')
            voice_change("Sir, Should i include date and time.")
            snfm = speech_to_text()
            if 'yes' in snfm or 'sure' in snfm:
                strtime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strtime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in command:
            voice_change("Showing Notes.")
            file = open("alexa.txt", "r")
            print(file.read())
            voice_change(file.read(6))
        elif "alexa" in command:
            wish_me()
            voice_change("alexa 1 point o in your service Mister. koushik")
        elif "weather" in command:
            api_key = "4a7c767ebc36b6d9cee7ab625d940e83"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            voice_change("What is the City name ")
            print("City name : ")
            city_name = speech_to_text()
            complete_url = base_url+"q="+city_name+"&appid="+api_key
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = float("{:.2f}".format(y["temp"]))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in Celsius unit) = " + str(
                    current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidity) + "\n description = " + str(weather_description))
                voice_change(" Temperature (in Celsius unit) is " + str(
                    current_temperature-273.15) + "\n atmospheric pressure (in hPa unit) is" + str(
                    current_pressure) + "\n humidity (in percentage) is " + str(
                    current_humidity) + "\n description = " + str(weather_description))
            else:
                voice_change(" City Not Found .")
        elif "Good Morning" in command:
            voice_change("A warm" + command)
            voice_change("Good morning")
        elif "will you be my gf" in command or "will you be my bf" in command:
            voice_change("I'm not sure about, may be you should give me some time.")
        elif "how are you" in command:
            voice_change("I'm fine, glad you me that")
        elif "i love you" in command:
            voice_change("It's hard to understand")
        elif 'calculate' in command or 'calculator' in command:
            calculator()
        elif "what is" in command or "who is" in command:
            app_id = 'PJ6553-EX5KRG2HE5'
            client = wolframalpha.Client(app_id)
            res = client.query(command)
            try:
                print(next(res.results).text)
                speech_to_text(next(res.results).txt)
            except StopIteration:
                print("No results")

time.sleep(1)
