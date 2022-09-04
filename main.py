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
    s.say('Diga Algo')
    s.runAndWait()
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language='pt-BR')
    print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não consegui entender o audio")
except sr.RequestError as e:
    print("Não pôde requerir os serviços do Google Speech Recognition; {0}".format(e))


file_path = 'teste.txt'

if texto == 'limpar':
    s.say('Você disse' + texto)
    s.runAndWait()
    with open(file_path, "w") as f:
        pass

elif texto == 'deletar':
    s.say('Você disse' + texto)
    s.say('Escolha o número da linha')
    s.runAndWait()

    with sr.Microphone() as source:
        print()
        print("Escolha o número da linha")
        print()
        audio = r.listen(source)

    texto2 = r.recognize_google(audio, language='pt-BR')
    numLinha = int(texto2)
    try:
        with open('teste.txt', 'r') as fr:
            linhas = fr.readlines()

            ptr = 1

            with open('teste.txt', 'w') as fw:
                for linha in linhas:
                    if ptr != numLinha:
                        fw.write(linha)
                    ptr += 1
        print("Linha " + texto2 + " deletada")
        s.say('Linha' + texto2 + 'deletada')
        s.runAndWait()
    except:
        print("Algo deu errado!")
else:
    sys.stdout = open(file_path, "a")
    print(texto)
    s.say('Adicionando' + texto)
    s.runAndWait()