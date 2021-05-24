from get import read_uread, twodays_mail
from text_speech import *
from send import *


while True:

    text_to_speech('say 1 to send a Mail !')
    text_to_speech('say 2 to read Mail !')
    text_to_speech('say 3 to close the application !')

    first_response = speech_to_text()

    if first_response == '1':
        send_message()
    elif first_response == '2' or first_response == 'tu' or first_response == 'two' or first_response == 'Tu' or first_response == 'to' or first_response == 'To':
        text_to_speech(
            "Say 1 for Unread Mails\n Say 2 to listen mails from last two days")
        receive_response = speech_to_text()
        if receive_response == '1':
            read_uread()
        elif receive_response == '2' or receive_response == 'Tu' or receive_response == 'tu' or receive_response == 'two' or receive_response == 'To' or receive_response == 'to':
            twodays_mail()
    elif first_response == '3' or receive_response == 'three' or receive_response == 'Three':
        exit()
    else:
        text_to_speech('Sorry you were not clear with your vocals !')
        continue
