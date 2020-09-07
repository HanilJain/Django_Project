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
 ::::::::  :::     ::: :::::::::: :::::::::               :::::::::   ::::::::   ::::::::  
:+:    :+: :+:     :+: :+:        :+:    :+:              :+:    :+: :+:    :+: :+:    :+: 
+:+    +:+ +:+     +:+ +:+        +:+    +:+              +:+    +:+ +:+    +:+ +:+        
+#+    +:+ +#+     +:+ +#++:++#   +#++:++#: +#++:++#++:++ +#+    +:+ +#+    +:+ +#++:++#++ 
+#+    +#+  +#+   +#+  +#+        +#+    +#+              +#+    +#+ +#+    +#+        +#+ 
#+#    #+#   #+#+#+#   #+#        #+#    #+#              #+#    #+# #+#    #+# #+#    #+# 
 ########      ###     ########## ###    ###              #########   ########   ########  
	''')
print(color.RED+color.BOLD+"="*80+color.END)
print("")
print(color.PURPLE+color.BOLD+" [1] => Port-Scanner"+color.END)
print("")
print(color.lightblue+color.BOLD+"="*80+color.END)
print("")
print(color.YELLOW+color.BOLD+" [2] => UDP Tide"+color.END)
print("")
print(color.lightblue+color.BOLD+"="*80+color.END)
print("")
print(color.CYAN+color.BOLD+" [3] => Syn Tide"+color.END)
print("")
print(color.lightblue+color.BOLD+"="*80+color.END)
print("")

ans_dos = input(color.lightblue+color.BOLD+" Select your attact = "+color.END)
if '1' in ans_dos:
    cmd = os.system("python3 port-scanner.py")
elif '2' in ans_dos:
	cmd = os.system("python3 UDP_Tide.py")
elif '3' in ans_dos:
	cmd = os.system("python3 syn_Tide.p")
else:
	print("INVALID OPTION")

