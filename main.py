import os
import subprocess
from subprocess import check_call
import sys, traceback
from banner import xe_header
 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   Orange='\033[33m'
   lightblue='\033[94m'
   lightcyan='\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   pink='\033[95m'
   lightgreen='\033[92m'
   lightred='\033[91m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   os.system("clear")


def banner():
  print(color.RED+color.BOLD+"="*80+color.END)
  print("")
  print ((color.GREEN+color.BOLD+  xe_header()+color.END))
  print("")
  print(color.RED+color.BOLD+"="*80+color.END)


def menu():
  print("")
  print(color.PURPLE+color.BOLD+" [1] => OPEN Social Engineer Toolkit (SET) "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.YELLOW+color.BOLD+" [2] => OPEN TooLTX ( For installing all the pentesting tools )"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.CYAN+color.BOLD+" [3] => OPEN WIFI-BRUTER ( For Cracking wireless network )"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.GREEN+color.BOLD+" [4] => OPEN SQLEET ( For testing sql injections over a website )"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.YELLOW+color.BOLD+" [5] => OPEN OVER-DDOS ( For Dos/DDos Attacks "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.Orange+color.BOLD+" [6] CLOSE !"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")



def restart():
	 print("DO YOU WANT To start this script again?")
     

while True:

      cmd = os.system("clear")
      banner()
      print("")
      menu()
      print("")
      option = input(color.lightred+color.BOLD+" [+] What you want to select = "+color.END)

      if '1' in option:
        cmd = os.system("sudo ./setoolkit")

      elif '2' in option: 
        cmd = os.system("python3 TOOLTX.py")

      elif '3' in option:
        cmd = os.system("python3 WIFI-MENU.py")

      elif '4' in option:
        cmd = os.system("python3 sqleet.py")

      elif '6' in option:
        cmd = os.system("clear")
        sys.exit()

      elif '5' in option:
        cmd = os.system("python3 OVER-DOS.py")
  



