#           import            #
import os , sys , time , random
from login import username , password
from random import choice
#             var             #
banner=''' 
          wvwVWVWvwv
       vwvwVWVWVWVWvwvw
    vwVWVW          VWVWvw
   vwVW    /\    /\    VWvw
  wVW      \ \  / /      VWv
 wVW  /\    \ \/ /    /\  VWv
wVW  /  \    \__/    /  \  VWv
wVW  \_  \    __    /  _/  VWv
wVW   \_  \  /  \  /  _/   VWv
wVW    \_  \/    \/  _/    VWv
 wVW    \_    /\    _/    VWv
  wVWV   \_  /  \  _/   WVWv
   vwVWV  \_/    \_/  WVWvw
     vwVWV L A M A R WVWvw
       vwVWVWVWVWVWVWvw
'''
format_txt='.txt'
#            defs            #
def menu():
    print (''' 

-
-
[MENU]


1~ MK LIST = MAKE NEW LISTA :)


2~ cls = Clear the Screen :)


3~ get_web = start tools1.com :)


4~ exit :(


[END]
-
-    
    ''')
def create_mail(data):
    mas=''
    char='mohamedahmedyousseflamaromaruserpassword'
    for i in range(data):
        mas += choice(char)
    return mas
def MK_LIST():
    name=input('Enter Your List Name=')
    file=open(name +format_txt, 'a')
    mails=['@hotmail.com','@yahoo.com']
    for i in range(200):
        x=random.choice(mails)
        file.write('\n' +create_mail(6) +x)
def cls():
    os.system('clear')
def get_web():
    os.system('termux-open-url ' +'https://tools1s.com/')
#            main            #
os.system('clear')
user=input('User=')
pasw=input('Pass=')
if user == username and pasw == password:
  os.system('clear')
  print (banner)
  msg='Welcome. Please Enter "help" to show menu'
  msgc=msg.center(50, ' ')
  print (msgc)
  while True:
      main=input('Lamar@linux ~ ')
      if main == 'help':
          menu()
      elif main == 'MK LIST':
          MK_LIST()
      elif main == 'cls':
          cls()
      elif main == 'get_web':
          get_web()
      elif main == 'exit':
          sys.exit()
      else:
         print ("'" +main+ "' is not recognized as an internal or external command, operable program or batch file.")
else:
    print ('[!] Login failed')
    time.sleep(2)
    os.system('python lamar.py')
