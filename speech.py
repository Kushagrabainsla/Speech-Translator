import os
import sys
import speech_recognition as sr
from gtts import gTTS 
from googletrans import Translator
import googletrans
import pyttsx3

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_Dialog(QDialog):

    # Constructor
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("speech.ui", self)
        self.comboBox.addItems(['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'])
        self.comboBox_2.addItems(['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'])
        self.pushButton.clicked.connect(self.speechtotext)
        self.translator = Translator()
        self.r = sr.Recognizer()

    # For translating the text into the desired language.
    def translate(self, MyText, lang1, lang2):
        text_to_translate = self.translator.translate(MyText,  src= lang1, dest= lang2)
        return text_to_translate.text

    # For speaking the translated text out loud.
    def SpeakText(self, text, lang2):
        """
        There are some problems with google text to speech api right now, I'll update as soon as it works.
        speak = gTTS(text=text, lang=lang2, slow= False)  
        speak.save("captured_voice.mp3")      
        os.system("afplay captured_voice.mp3")
        """

        # For now, I'll be using pyttsx3 library for text to speech.
        # For languages like hindi, gujarati, etc. This library don't perform very well.
        print(text)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Getting the languages form the combo boxes and assigning them codes with the help of googletrans.LANGUAGES .
    def languages(self):
        language1 = self.comboBox.currentText() # Getting the language from the combo box that is feeded
        language2 = self.comboBox_2.currentText() # Getting the language from the combo box that is to be translated
        for i,j in googletrans.LANGUAGES.items():
            if j == language1:
                lang1 = i
            if j == language2:
                lang2 = i
        return lang1,lang2
    
    # For taking input from the microphone, when you click the button.
    def microphone_input(self):
        with sr.Microphone() as source: 
            self.r.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.r.listen(source)
            MyText = self.r.recognize_google(audio)
            MyText = MyText.lower()
        return MyText
    
    # For writing on label 5
    def instructions(self, text):
        self.label_5.setText(text)
        self.label_5.setStyleSheet("font-weight: bold")
        self.label_5.setAlignment(Qt.AlignCenter)

    # For writing on label 6
    def translated_text(self, text):
        self.label_6.setText(text)
        self.label_6.setStyleSheet("font-weight: bold")
        self.label_6.setAlignment(Qt.AlignCenter)

    def speechtotext(self):
        try:
            self.instructions("Speak")
            print("speak")

            MyText = self.microphone_input()
            self.instructions("You said: " + MyText) # Printing the speech to be translated in order to double check the message to be translated

            lang1,lang2 = self.languages() # getting the language code form selected languages
            text = self.translate(MyText, lang1, lang2) # translating the text into other language
            self.translated_text("Translated Into: " + str(text))
            self.SpeakText(text, lang2) # speaking the converted speech

        except sr.UnknownValueError:
        	self.instructions("Try Again !!")
           


