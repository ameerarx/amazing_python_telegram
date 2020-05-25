# @pythonamazing(Telegram)
import time 
import winsound # Для linux можно использовать pygame.mixer.music
def myAlarm():
    try:
        myTime = list(map(int,input("Введите время в ч м с\n").split()))
        if len(myTime) == 3:
            total_seconds = myTime[0]*60*60+myTime[1]*60 + myTime[2]
            time.sleep(total_seconds)
            frequency = 2500 # установить частоту до 2500 герц
            duration = 1000  # установить длительность 1000 мс == 1 секунда
            winsound.Beep(frequency,duration)
        else:
            print("пожалуйста, введите время в правильном формате, как указано\n")
            myAlarm()  
    except Exception as e:
        print("Это исключение\n",e,"Пожалуйста, введите правильные данные") 
        myAlarm()
myAlarm()  
               