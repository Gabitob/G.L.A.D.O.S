import speech_recognition as sr
import sys
import pyttsx3

s = pyttsx3.init()

# Captura áudio do microfone
r = sr.Recognizer()

with sr.Microphone() as source:
    print()
    print("Diga Algo!")
    print()
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language='pt-BR')
    print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não consegui entender o audio")
except sr.RequestError as e:
    print("Não pôde requerir os serviços do Google Speech Recognition; {0}".format(e))


s.say('Você disse' + texto)
s.runAndWait()

file_path = 'teste.txt'
sys.stdout = open(file_path, "a")
print(texto)
