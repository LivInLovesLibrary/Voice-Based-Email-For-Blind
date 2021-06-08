# Voice-Based-Email-For-Blind

This is a Python Application which allows its users to send, receive E-Mails through voice.

Complete the steps described in the rest of this page, and in about five minutes you'll have a simple Python command-line application that makes requests to the Gmail API.

## Prerequisites:-

- Python 2.6 or greater.
- The pip package management tool.
- Access to the internet and a web browser.
- A Google account with Gmail enabled.
- Use the link given to create client_secret.json https://developers.google.com/gmail/api/quickstart/python

###### Get The Gmail API file (client_secret.json)

- Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to   credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the    Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Gmail API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it client_secret.json.


## Modul Being Used
1. pyttsx
2. SpeechRecognition
3. PyAudio
4. simplegmail
5. os
6. kivy
7. kivymd

To Run this Project:
```
cd <Project Directory>
pip install requirment.txt
python main.py
```


