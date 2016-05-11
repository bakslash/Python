#!/usr/bin/python
import webbrowser
import time

num=1

print("This program has started"+time.ctime())
while(num<5):
    
    time.sleep(60*60)
    webbrowser.open("http://www.youtube.com")
    num = num + 1
