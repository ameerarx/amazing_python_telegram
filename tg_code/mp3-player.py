from pygame import mixer

mixer.init() # Запустить mixer
# в случае ошибки,запустите через системный терминал или сменить config 

mixer.music.load("song.mp3") # загрузить музыку
# в случае ошибки при чтение следует сменить формат файла
mixer.music.set_volume(0.7) # установить громкость
mixer.music.play() # play  

while True:
    print("нажмите на 'p', чтобы приостановить на 'r', чтобы возобновить")
    print("нажмите на 'e' для выхода из программы")
    query = input(">>>")
 
    if query == 'p':
        mixer.music.pause()  # пауза 
    elif query == 'r':
        mixer.music.unpause()  # возобновить
    elif query == 'e':
        mixer.music.stop() # стоп и выход
        break        