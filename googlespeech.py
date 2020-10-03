import speech_recognition as sr //google library to read voice
import webbrowser as wb
chrome_path='google-chrome'         //read googlechrome patth to search voice command
r=sr.Recognizer()
with sr.Microphone() as source:         //listens to microphones
    print("say something")
    audio=r.listen(source)
    print("done")

try:
    text=r.recognize_google(audio)                  //converting audio to text
    print("rishabh thinks yu said:\n"+text)
    wb.get(chrome_path).open(text)

except Exception as e:                                //prints the output
    print(e)
