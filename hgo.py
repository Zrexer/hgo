#!/usr/bin/env python3
"""
hgo
~~~~~

Nothing

Dev: Host1let 

```
Bye
```
"""

#----[ Libraries ]----
import sys
import socket
import os
import time

#----[ Its Make Possible To see the Colors for Powershell/CMD Users ]----
os.system("")

#----[ Call Downloader in Terminal ]----
if "--download-requirements" in sys.argv:
    try:
        file = open('./dl.hgo').read()
        exec(file)
        pass
    except Exception as efile:
        print(efile)
        exit("Usage Requirements Downloader: {} --download-requirements".format(sys.argv[0]))

#----[ Classes of Colors ]----
class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'


#----[ Box Classes ]----
class BoxCreator(object):
    """
    For Make Message Boxs
    Type of Messages: 'info', 'error', 'warning', 'workingInBackGround'
    
    you can copy it if you like
    """
    
    def __init__(self, message, typeOfMessage):
        self.msg = message
        self.tom = typeOfMessage
    
    @property
    def makeBox(self):
        assert self.tom in ("info", "error", "warning", 
                            "workingInBackGround"), "Type of %r its not in 'info', 'error', 'warning', 'workingInBackGround'" %(self.tom,)
        
        if self.tom == "info":
            return "{}[{}{}{}] [{}{}{}] {}".format(colors.white, colors.yellow, time.strftime("%H:%M:%S"), colors.white, colors.green, "info", colors.white, self.msg)
        
        elif self.tom == "error":
            return "{}[{}{}{}] [{}{}{}] {}".format(colors.white, colors.yellow, time.strftime("%H:%M:%S"), colors.white, colors.red, "Error", colors.white, self.msg)
        
        elif self.tom == "warning":
            return "{}[{}{}{}] [{}{}{}] {}".format(colors.white, colors.yellow, time.strftime("%H:%M:%S"), colors.white, colors.underline+colors.yellow, f"WARNING{colors.white}", colors.white, self.msg)
        
        elif self.tom == "workingInBackGround":
            return "{}[{}{}{}] [{}{}{}] {}".format(colors.white, colors.yellow, time.strftime("%H:%M:%S"), colors.white, colors.darkblue, "BackGround Work", colors.white, self.msg)


def banner() -> str: 
    s = "/"
    l = "\\"
    b = "{"
    d = "}"
    dash = "-"
    return f"""{colors.red}
       '||'  '||'                
        ||    ||    ... .  {s}{l}{l}  
        ||''''||   || ||  || || 
        ||    ||    |''   || || 
       .||.  .||.  '||||. || || 
                .|....' || || 
                            {l}{l} {s}
    {colors.white}{b}{colors.yellow}{dash*9}{colors.cyan}{b}{colors.white}Host1let{colors.cyan}{d}{colors.yellow}{dash*9}{colors.white}{d}
"""

def guider() -> str:
    print(f"\n{colors.red}┌──{colors.white}{colors.yellow}({colors.underline}{colors.red}{os.getcwd()}{colors.yellow})".replace('/', f"{colors.yellow}/{colors.white}").replace('\\', f"{colors.yellow}\\{colors.white}"))
    user = str(input(f"{colors.red}└──{colors.yellow}{colors.underline}Hg0{colors.white} > "))
    return user

#----[ Console Function ]----
def ConsoleHandler():
    """
    Console Handler is Desing for Terminal Controll
    """
    print(banner())
    while 1:
        user = guider()
        text = user.split()
        
        if "socket-connect" in text:
            ip = text[text.index('socket-connect')+1]
            print(BoxCreator(f"Try To Connect {ip}", 'workingInBackGround').makeBox)
            try:
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(ip)
                print(BoxCreator(f"Connected to {ip}", 'info').makeBox)
            except Exception as e:
                print(BoxCreator(e, 'error').makeBox)
                pass
    
if __name__ == "__main__":
    ConsoleHandler()
