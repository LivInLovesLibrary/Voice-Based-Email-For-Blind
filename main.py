# Program to create a calculator

# Program to Show how to create a switch
# import kivy module

from send import *
from text_speech import *
from tkinter import *
from get import read_uread, twodays_mail,search_mail
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import kivy
import os
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App


# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

mydisplay = "Parmita Saha\nPromita Chakrabarty\nTrishita Ghosh\nSudeshna Panda"
welcometext = "Welcome to V MAil"
# for making multiple bttons to arranging
# them we are using this

# for the size of window

# Setting size to resizable
Config.set('graphics', 'resizable', 1)
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '400')


class p(FloatLayout):
    pass


# Creating Layout class
class CalcGridLayout(GridLayout):
    def mainfunction(self):
        while True:

            text_to_speech('say 1 to compose a mail!')
            text_to_speech('say 2 to check inbox!')
            text_to_speech('say 3 to close the application !')

            first_response = speech_to_text()

            if first_response == '1':
                send_message()

            elif first_response == '2' or first_response == 'tu' or first_response == 'two' or first_response == 'Tu' or first_response == 'to' or first_response == 'To':
                text_to_speech(
                    'Say 1 for Unread Mails\n Say 2 to listen mails from last two days\n  Say 3 to Search Mail via Days ')
                
                receive_response = speech_to_text()
                if receive_response == '1':
                    read_uread()
                elif receive_response == '2' or receive_response == 'Tu' or receive_response == 'tu' or receive_response == 'two' or receive_response == 'To' or receive_response == 'to':
                    twodays_mail()
                elif receive_response == '3' or receive_response == 'Three' or receive_response == 'three' or receive_response == 'tree':
                    search_mail()
            elif first_response == '3' or receive_response == 'three' or receive_response == 'Three':
                exit()
            else:
                text_to_speech('Sorry you were not clear with your vocals !')
                continue

    def aboutbtn(self):
        aboutPage()

    def update(self):
        self.ids.entry.text = str(mydisplay)

    def welcome(self):
        self.ids.entry.text = str(welcometext)

    def logoutbtn(self):

        if os.path.exists("gmail_token.json"):
            os.remove("gmail_token.json")
            self.ids.entry.text = "You have Sucsesfully Logged out"
            text_to_speech('You have Sucsesfully Logged out')
            exit()
        else:
            self.ids.entry.text = "You are already Logged out"
            text_to_speech('You are already Logged out')
            exit()


def aboutPage():
    show = p()

    popupWindow = Popup(title="About", content=show,
                        size_hint=(None, None), size=(400, 400))
    popupWindow.open()

# Creating App class


class VMailApp(App):
    mydisplay = "Welcome to V Mail"

    def build(self):
        return CalcGridLayout()


# creating object and running it
calcApp = VMailApp()
calcApp.run()
