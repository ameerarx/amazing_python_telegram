# @pythonamazing(Telegram)
import fbchat 
from getpass import getpass
username = str(input("Username: "))
client =fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = client.getUsers(name)
    # return a list of name 
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.send(friend.uid,msg)
    if sent:
        print("Message sent seccessful")