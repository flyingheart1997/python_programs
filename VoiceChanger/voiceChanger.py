# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import pyttsx3 as ptx
flag = 0

# A tuple containing all the language and
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
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')


# Capture Voice
# takes command through microphone

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        sentence = r.recognize_google(audio, language='en-in')
        print(f"The User said {sentence}\n")
    except Exception as e:
        text_to_speech("say that again please.....")
        print(e)
        return "None"
    return sentence


# # Input from user
# # Make input to lowercase

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
    lang = take_command().lower()
    while lang == "None":
        lang = take_command().lower()
    lang = lang.lower()
    return lang


to_lang = destination_language()

# # Mapping it with the code
while to_lang not in dic:
    text_to_speech("Language in which you are trying\
    to convert is currently not available ,\
    please input some other language")
    to_lang = destination_language()

to_lang = dic[dic.index(to_lang) + 1]


def query():
    while True:
        s = take_command().lower()
        while s == 'None':
            s = take_command().lower()
        return s


def change_voice(word):
    translator = Translator()
    text_to_translate = translator.translate(word, dest=to_lang)
    print(text_to_translate)
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow=False)
    sound = 'voice.mp3'
    speak.save(sound)
    playsound(sound)
    os.remove(sound)


while True:
    ssd = query().lower()
    if 'exit' in ssd or 'stop' in ssd:
        change_voice('Thank you')
        break
    change_voice(ssd)
