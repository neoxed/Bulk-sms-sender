import os
import requests
import time


print('1 : send a single message')
print('2 : send bulk message')
print('')
numList = open("num.txt", "r")
lines = numList.readlines()
num = int(input("choice "))
os.system("cls")
cout = 0
if num == 1:
    time.sleep(2)
    tosend = input("send to : ")
    time.sleep(1)
    message = input("mesage : ")
    x = requests.get('http://172.20.10.2:8090/SendSMS?username=test&password=1234&phone='+tosend+'&message='+message)
    time.sleep(1)
    os.system("cls")
    print('Message sent to '+tosend)
elif num == 2:
    time.sleep(2)
    message = input("mesage : ")
    os.system("cls")
    for line in lines:
        cout += 1
        line = line.replace("\n", "").replace("\r", "")
        phone = line
        x = requests.get('http://172.20.10.2:8090/SendSMS?username=test&password=1234&phone='+phone+'&message='+message)
        print('Message sent to '+phone)
        time.sleep(1)
os.system("cls")
print('send finished')