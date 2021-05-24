from simplegmail import Gmail, message
from simplegmail.query import construct_query
from text_speech import *

gmail = Gmail()

messages = []
len_messege = 0

i = 0


def read_uread():

    # Unread messages in your inbox
    messages = gmail.get_unread_inbox()
    len_messege = len(messages)
    read_mails(messages)


def read_starred():

    # Starred messages
    messages = gmail.get_starred_messages()
    len_messege = len(messages)
    read_mails(messages)


def search_mail():
    text_to_speech("From Last How Many days you want me search you Mail")
    daysAsk = speech_to_text()
    text_to_speech("Do you want me to read only unread messages")
    readAsk = speech_to_text()
    if readAsk == 'Yes' or readAsk == 'yes' or readAsk == 'Yup' or readAsk == 'Yo':
        read = True
    else:
        read = False
    # text_to_speech("")
    query_params = {
        "newer_than": (daysAsk, "day"),
        "unread": read,
    }
    messages = gmail.get_messages(query=construct_query(query_params))
    len_messege = len(messages)
    read_mails(messages)


def twodays_mail():
    text_to_speech("From Last How Many days you want me search you Mail")
    daysAsk = speech_to_text()
    text_to_speech("Do you want me to read only unread messages")
    readAsk = speech_to_text()
    if readAsk == 'Yes' or readAsk == 'yes' or readAsk == 'Yup' or readAsk == 'Yo':
        read = True
    else:
        read = False
    # text_to_speech("")
    query_params = {
        "newer_than": (2, "day"),
        "unread": False,
    }
    messages = gmail.get_messages(query=construct_query(query_params))
    read_mails(messages)


def read_mails(messages):
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Mail Body: " + message.plain)  # or message.html

        text_to_speech(message.sender + "has sent you a mail about " + message.subject +
                       " on " + message.date + ". the mail says " + message.plain)  # or message.html
        i = i+1
        text_to_speech(
            "Say 1 to Reply this mail \nSay 2 to Forword the mail \nSay 3 to Chnage it's Label \n Say 4 to Read Next mail")
        read_mails_response = speech_to_text()
        if read_mails_response == '1' or read_mails_response == 'one' or read_mails_response == 'One':
            text_to_speech("Whom Do You Want to Send")
            replyMessage = speech_to_text()
            params = {
                "to": message.sender,
                "sender": message.recipient,
                "subject": "Re: " + message.subject,
                "msg_html": " ",
                "msg_plain": str(replyMessage),
                "signature": True  # use my account signature
            }
            message1 = gmail.send_message(**params)
            print("Email has Been Sucsesfully Replied")
        elif read_mails_response == '2' or read_mails_response == 'tu' or read_mails_response == 'two' or read_mails_response == 'Tu' or read_mails_response == 'to' or read_mails_response == 'To':
            text_to_speech('say the E-Mail address of the receiver')
            email = speech_to_text()
            words = email.split()
            modified_mail = str()
            for word in words:
                if word == 'underscore':
                    modified_mail = modified_mail+'_'
                elif word == 'dot':
                    modified_mail = modified_mail+'.'
                else:
                    modified_mail = modified_mail+word

            modified_mail = modified_mail.lower()
            print(modified_mail)
            sendingto = modified_mail
            params = {
                "to": sendingto,
                "sender": "",
                "subject": "Fwd: " + message.subject,
                "msg_plain": message.plain,
                "signature": False  # use my account signature
            }
            # equivalent to send_message(to="you@youremail.com", sender=...)
            message2 = gmail.send_message(**params)
            print("Email has Been Sucsesfully Forworded")
        else:

            if(len_messege == i):
                print("Sorry You have Heared All the Mail Loded")
                text_to_speech("Sorry You have Heared All the Mail Loded")
            else:
                print("Reading Next Mail")
                text_to_speech("Reading Next Mail")
