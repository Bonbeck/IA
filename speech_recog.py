import speech_recognition as speech

r = speech.Recognizer()
audio = speech.AudioFile("gravacao.wav")

with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_rec = r.record(source)
result = r.recognize_google(audio_rec)

with open("trascricao.txt", mode='w') as file:
    file.write("recognized text:")
    file.write("\n")
    file.write(result)
print("tudo pronto")