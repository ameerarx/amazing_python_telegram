from gtts import gTTS
from playsound import playsound

audio = 'seech.mp3'
language = 'ru'
sp =  gTTS(text = "Введите ваш текст который ты хочешь конвертировать в аудио файл",
            lang = language,slow = False)
sp.save(audio)
playsound(audio)            
