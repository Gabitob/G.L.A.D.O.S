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


file_path = 'teste.txt'
s.say('Você disse' + texto)
s.runAndWait()

if texto == 'limpar':
    with open(file_path, "w") as f:
        pass
else:
    sys.stdout = open(file_path, "a")
    print(texto)