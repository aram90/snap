from __future__ import absolute_import
import os
from requests import get
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import random
import time,sys
from queue import Queue
from threading import Thread
import timeit
from time import sleep
import webbrowser
from itertools import cycle


name_of_file = sys.argv[0]
working_proxies = []





print ('''
                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'
 [*] https://t.me/joinchat/AAAAAFc1xzOCe7dLxce0iQ
 [*] snapchat: alissopozi
 
بو ريپورت كردن ي انستا تكايه به كا ري مه هينه بو ازيت داني موسلمانان 🇹🇯

''')


def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')



print (' ')
ketik (" Hacker developer : ahmadbahrooz ")
sleep(0.5)


class Instagram:
    def __init__(self, username):
        self.username = str(username)


def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()

print('==========================================')
  
  
  

uIG = input('Username Spam : ')
url = get("https://theinstantstalker.com/instagram/" + uIG)


soup = BeautifulSoup(url.text, 'html.parser')
name = soup.find('h1',{'style':'margin-bottom: 0; font-size: 22px; font-weight: 600;'})
des = soup.find('p',{'style':'margin-top: 0; margin-bottom: 0; color: #212121;'})
info = soup.find('div',{'class':'profile-info'})
si = soup.find('a',{'id':'instagram-story-count'})
postingan = soup.find('p',{'style':'max-height: 137px; overflow: hidden;'})
try:
  nama = name.text.rstrip().lstrip()
  deskrip = des.text.rstrip().lstrip()
  inpo = info.text.rstrip().lstrip()
  story = si.text.rstrip().lstrip()
  id = comments.text.rstrip().lstrip()
  post = postingan.text.rstrip().lstrip()
except:
  print('Ada yang salah atau error')
print ('Username :',uIG)
print ('Link : https://www.instagram.com/'+uIG)

try:
  print ('Nama :'+nama)
  print ('Deskripsi :'+deskrip)

except:
  exit
  
dir_path = os.path.dirname(os.path.realpath(__file__))
#Connecting to a proxy with urllib3
print("Finding Working Proxies")
proxy_list = open(dir_path + "/proxy.txt", 'r+').readlines()
proxy_list = [item.replace("""\n""", "") for item in proxy_list]
proxy_pool = cycle(proxy_list)

url = "http://myexternalip.com/raw"
for i in range(len(proxy_list)-1):
    #Get a proxy from the pool
  proxy = next(proxy_pool)
try:
  response = requests.get(url,proxies={"http": proxy, "https": proxy})
  working_proxies.append(proxy)

except:
        pass;
print("Found working proxy")
lenght_of_proxy = len(working_proxies)

number_of_proxy_rand = random.randint(0,int(lenght_of_proxy-1))
print("Connecting to proxy (Might take a while)")
number_of_proxy_rand = number_of_proxy_rand
proxies = {
'http':  working_proxies[number_of_proxy_rand],
'https': working_proxies[number_of_proxy_rand],
}

os.environ['http_proxy'] = working_proxies[number_of_proxy_rand]
os.environ['HTTP_PROXY'] = working_proxies[number_of_proxy_rand]
os.environ['https_proxy'] = working_proxies[number_of_proxy_rand]
os.environ['HTTPS_PROXY'] = working_proxies[number_of_proxy_rand]

# Create the session and set the proxies.
l = requests.Session()
l.proxies = proxies

print("Checking Connection")
r = l.get("http://myexternalip.com/raw")
print("your connecting through: ", r.text)


print("ATTEMPTING BRUTEFORCE")  


MaGMA = 0
while MaGMA < 50 :
	time.sleep(5)
	webbrowser.open("https://www.instagram.com/users/"+ uIG +"/report/")
	MaGMA = MaGMA + 1

quit()
SC()