import shutil
"""
Копировать,Удалять,Перемещать каталоги 
используя встроенный модуль shutil
"""
# Удалить все дерево каталогов
shutil.rmtree("D:\\path")

# Скопировать любое дерево каталогов
shutil.copytree("D:\\Source",
               "D:\\Destination")

# Переместить любой файл или каталог
shutil.move("D:\\Source",
               "D:\\Destination")