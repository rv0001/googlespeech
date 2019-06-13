import speech_recognition as sr
import webbrowser as wb
chrome_path='google-chrome'
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio=r.listen(source)
    print("done")

try:
    text=r.recognize_google(audio)
    print("rishabh thinks yu said:\n"+text)
    wb.get(chrome_path).open(text)

except Exception as e:
    print(e)
