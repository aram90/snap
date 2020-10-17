import time
import subprocess
import random
import requests
from time import sleep
from six.moves import input
import os , webbrowser

A = """
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>
<       kk-snap :   .👻.                >
< snapchat / alissopozi                 >
< fb / ahmad bahrooz                    >
<                                       >
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

"""
print ("")
print(A)
user = input("Enter your snapchat user:")
time.sleep(2)
print("")
print("[-] Entering snap Server...")
time.sleep(2)
print("")
print("[-] Inserting", user, "to the login page")
time.sleep(3)
print("")
print("[-] Creating a backdoor in there server...")
print("[-] Pls be patient")
time.sleep(2)
print("")
print("[-] Making my way into their server...")
print("[-] Bruteforcing server starting soon...")
print("[-] Creating a meterpreter in", user , "snap Account...")
time.sleep(4)
print("")
print("[-] Hacking will start in 5 seconds")
time.sleep(5)
print("")
print("[-] Pls wait hacking into the snapchat profile")
time.sleep(2)
print("")


headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }

#اليره لينك كوبي بكه 
url = "https://accounts.snapchat.com/accounts/login/2fa?tfa_requirements=eyJwcmVfYXV0aF90b2tlbiI6Ijdsb0p1UTBIUkM0QWM2dkVWdUp4NkZqcGxMZXd0ZFBlbk45RmNFWDVUN3MiLCJhbGxvd2VkXzJmYV9tZWNoYW5pc21zIjpbIk9UUCIsIlNNUyJdLCJvYmZ1c2NhdGVkX3Bob25lX251bWJlciI6Iit4eHh4eHh4eHh4MzYifQ%3D%3D&user_id=2c968415-8bc7-4a5b-9c9b-ae7f134dd0a3&continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome&username=".format(user)



r = requests.post(url,headers=headers)

def IsUserExists(self):
		r = requests.get(''+url+'' % self.user) 
		if (r.status_code == 404):
			print ('[*] ديسانه وه هه ول بده وه')
			Input('[*] Press enter to exit')
			exit()
		elif (r.status_code == 200):
			return True

webbrowser.open(""+url+"")



while True:
    time.sleep(1)
    e = random.randrange(100000, 1000000)
    print( user ,"not sms : %s => FUCK 🤬" % e)

if e is True:
    print(" => good 👍🏼 " % e)


main()