# Voice-Based-Email-For-Blind

This is a Python Application which allows its users to send, receive E-Mails through voice.

Complete the steps described in the rest of this page, and in about five minutes you'll have a simple Python command-line application that makes requests to the Gmail API.

## Prerequisites:-

Python 2.6 or greater.
The pip package management tool.
Access to the internet and a web browser.
A Google account with Gmail enabled.
Use the link given to create client_secret.json https://developers.google.com/gmail/api/quickstart/python

###### Get The Gmail API file (client_secret.json)

a)Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to   credentials.
b)On the Add credentials to your project page, click the Cancel button.
c)At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the    Save button.
d)Select the Credentials tab, click the Create credentials button and select OAuth client ID.
e)Select the application type Other, enter the name "Gmail API Quickstart", and click the Create button.
f)Click OK to dismiss the resulting dialog.
g)Click the file_download (Download JSON) button to the right of the client ID.
h)Move this file to your working directory and rename it client_secret.json.


## Modul Being Used
1. pyttsx
2. SpeechRecognition
3. PyAudio
4. simplegmail

To Run this Project:
```
pip install requirment.txt
python voice_project.py
```
