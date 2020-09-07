import os
import subprocess
from subprocess import check_call

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




print("\nInstalling all important tools ====> ")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
cmd  = os.system("sleep 3 && clear")



print(color.PURPLE+color.BOLD+'''
.##......##.####.########.####.........########..########..##.....##.########.########.########.
.##..##..##..##..##........##..........##.....##.##.....##.##.....##....##....##.......##.....##
.##..##..##..##..##........##..........##.....##.##.....##.##.....##....##....##.......##.....##
.##..##..##..##..######....##..#######.########..########..##.....##....##....######...########.
.##..##..##..##..##........##..........##.....##.##...##...##.....##....##....##.......##...##..
.##..##..##..##..##........##..........##.....##.##....##..##.....##....##....##.......##....##.
..###..###..####.##.......####.........########..##.....##..#######.....##....########.##.....##
'''+color.END)

print(color.lightred+color.BOLD+"""
------------------------------------------------------------------------------------
  
(1) ====> Crack Handshake with wordlist    (Handshake needed And Wordlist needed)

(2) ====> Crack Handshake without wordlist (Handshake,essid needed)

(3) ====> Create wordlist                                     

(00) ====> Exit

-------------------------------------------------------------------------------------
"""+color.END)

opt = input("WHAT YOU WANT TO DO =")

if '1' in opt:
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()

elif '2' in opt:
        print("\nEnter the essid of the network ?(Be careful when you type it and use 'the name of the network') ")
        essid = str(input(""))
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("""
---------------------------------------------------------------------------------------
(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
(7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
(9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
(10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Words and numbers
-----------------------------------------------------------------------------------------
""")
        print("\nEnter your choise here : ?")
        set = str(input(""))
        if set == "1":
            test = str("abcdefghijklmnopqrstuvwxyz")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "2":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "3":
            test = str("0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "4":
            test = str("!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "5":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "6":
            test = str("abcdefghijklmnopqrstuvwxyz0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "7":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "8":
            test = str("!#$%/=?{}[]-*:;0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "9":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "10":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "11":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "12":
            print("Enter you Own Words and numbers")
            test  = str(input(""))
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        else:
            print("\nNot Found")
            
        print("Copy the Password and Close the tool")
        cmd5 = os.system("sleep 3d")

elif '3' in opt:
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("\nEnter the path of the output file?")
        path = str(input(""))
        print("\nEnter what you want the password contain ?")
        password = str(input(""))
        order = ("crunch {} {} {} -o {}").format(mini,max,password,path)
        geny = os.system(order)
        a = ("The wordlist in >>>>> {} Named as SRART").format(path)
        print(a)
