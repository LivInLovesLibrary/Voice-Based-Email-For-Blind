import speech_recognition as sr
import pyttsx3  # To convert text to speech


def text_to_speech(sentence):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(sentence)
    engine.runAndWait()
    del engine


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        result = r.recognize_google(audio)
        print(type(result))
        print("You said: " + result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("No Result from Google Speech Recognition {0}".format(e))
    return str(r.recognize_google(audio))
