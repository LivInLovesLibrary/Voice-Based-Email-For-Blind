from simplegmail import Gmail
from text_speech import *

gmail = Gmail()


def mail_maker():
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
    return modified_mail


def send_message():
    text_to_speech('say the E-Mail address of the receiver')
    to = mail_maker()
    text_to_speech("If You want to Add a CC then Say it Otherwise Say No")
    cc = mail_maker()
    if cc == 'no' or cc == 'no' or cc == 'nop':
        final_cc = ""
    else:
        final_cc = cc

    text_to_speech("If You want to Add a B C C then Say it Otherwise Say No")
    bcc = mail_maker()
    if bcc == 'no' or bcc == 'no' or bcc == 'nop':
        final_bcc = ""
    else:
        final_bcc = bcc

    text_to_speech('Say the subject of the Mail')
    subject = speech_to_text()
    text_to_speech('Say the message you want to send !')
    message_text = speech_to_text()
    text_to_speech("Do you Add you Signature in you Mail?")
    signAsk = speech_to_text()
    if signAsk == 'Yes' or signAsk == 'yes' or signAsk == 'Yup' or signAsk == 'Yo':
        sign = True
    else:
        sign = False

    params = {
        "to": to,
        "sender": "soumalya9862@gmail.com",
        "cc": [final_cc],
        "bcc": [final_bcc],
        "subject": subject,
        "msg_html": "",
        "msg_plain": message_text,
        "attachments": [],
        "signature": sign  # use my account signature
    }
    # equivalent to send_message(to="you@youremail.com", sender=...)
    message = gmail.send_message(**params)

    print('You Mail has Been sent')
    text_to_speech('You Mail has Been sent')
