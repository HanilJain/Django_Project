import os
import subprocess
from subprocess import check_call
import sys, traceback

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

print(color.RED+color.BOLD+"="*80+color.END)
print('''

.##......##.####.########.####.........########..########..##.....##.########.########.########.
.##..##..##..##..##........##..........##.....##.##.....##.##.....##....##....##.......##.....##
.##..##..##..##..##........##..........##.....##.##.....##.##.....##....##....##.......##.....##
.##..##..##..##..######....##..#######.########..########..##.....##....##....######...########.
.##..##..##..##..##........##..........##.....##.##...##...##.....##....##....##.......##...##..
.##..##..##..##..##........##..........##.....##.##....##..##.....##....##....##.......##....##.
..###..###..####.##.......####.........########..##.....##..#######.....##....########.##.....##
'''+color.END)

print(color.RED+color.BOLD+"="*80+color.END)
print("")
print(color.PURPLE+color.BOLD+" [1] => WIFI-BRUTER FOR TERMUX"+color.END)
print("")
print(color.lightblue+color.BOLD+"="*80+color.END)
print("")
print(color.YELLOW+color.BOLD+" [2] => WIFI-BRUTER FOR KALI"+color.END)
print("")
print(color.lightblue+color.BOLD+"="*80+color.END)
print("")


ans_wifi = input(color.lightblue+color.BOLD+" Select your attact = "+color.END)
if '1' in ans_wifi:
    cmd = os.system("python3 Wifi.py")
elif '2' in ans_w:
	cmd = os.system("python3 WIFI-BRUTER-Kali.py")

else:
	print("INVALID OPTION")

