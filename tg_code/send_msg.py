import smtplib
from email.message import EmailMessage
EMAIL = "myemail@gmail.com"  # Ваш Email & пароль 
PASSWORD = 'mypassword'

msg = EmailMessage()

msg['Subject'] = 'Электронная почта с использованием Python' # subject
msg['From'] = EMAIL # Email оправителя
msg['To'] = ['my_friend@gmail.com']  # Email получателя

message =  "Это электронное письмо, созданное Python"
msg.set_content(message)

attachments =  [ # список прикрепленного 
                'C:\\Users\\Acer\\image.jpg' ]

for path in attachments:  # цикл по пути
    with open(path,'rb') as file: # открыть файл
        data = file.read() # читать содержимое 
        name = path.split("\\")[-1] 
    msg.add_attachment(data,maintype = 'application',
                    subtype = 'octet-stream',
                    filename = name) # добавить файл

with smtplib.SMTP_SSL('smtp.gamil.com',465) as smtp: 
    smtp.login(EMAIL,PASSWORD)
    smtp.send_message(msg)