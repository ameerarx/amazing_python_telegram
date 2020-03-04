from zipfile import ZipFile 

file_path = "zipfile.zip"

with ZipFile(file_path,'r') as zip_:
  # Принтить всё содержимое 
  zip_.printdir()
  
  # Извлечь zip
  zip_.extractall()
