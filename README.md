# Speech Recognition
Necessário ter um arquivo `gravacao.wav` para executar o algoritmo `speech_recog`.
Caso você queira colocar um arquivo de extenção `.wav` com nome diferente, você pode alterar o nome 
```audio = speech.AudioFile("gravacao.wav")```
no campo `AudioFile()` substituindo `gravacao.wav` pelo nome do seu arquivo.

Todo arquivo reconhecido gera um arquivo `.txt`
```with open("trascricao.txt", mode='w') as file:```
com a trascrição do seu áudio.