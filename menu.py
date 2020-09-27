import speech_recognition as sr
import webbrowser
import pyttsx3 as pt

sys = pt.init()
sys.say("Hello User")
sys.runAndWait()
print("Hello User")

print('Welcome to my tools\n\n')

print("Enter your requirements ...\n 1. date \n 2. calender \n...... we are listening .......", end=' ')
# ch = input()
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Start saying...')
    audio = r.listen(source)
    print('I got it, please wait ....')

ch = r.recognize_google(audio)
if ('date' in ch ) and (("run" in ch) or ("execute" in ch)):
    webbrowser.open("http://192.168.1.21/cgi/iiec.py?x=date")   
elif 'calender' in ch:
    webbrowser.open('http://192.168.1.21/cgi/iiec.py?y=cal')
else:
    print("Not understood")        