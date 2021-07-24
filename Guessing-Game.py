#import modules
import os        # for interact with the Operating system 
import time
import random    #To shuffle guess numbers within a random pile
import colorama  #To produce colored terminal text 
from colorama import Fore, Back, Style
colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')    #For clean screen to Start
Empty = ""                                          #To prove if the input is empty
clean= int(0)  
print('\n[+]__Welcome to the Number Guessing game ,For exit Press \"Ctrl+Shift+C\"__[+]')  # To print("[+]__Wlecom to Guessing Game ,For exit Enter "Ctrl+Shift+C"__[+]") with colors
print(Fore.GREEN+'[+] GOOD LUCK [+]\n'+Fore.WHITE)                                         # To print("[+] GOOD LUCK [+]") with colors
try:
    while True:                                      #For iteration loop for inputs
        Number = random.randint(1, 10)               #For exit by random number
        guessing = input('Guess a number between 1 & 10: ')  #For check  if inputs between 1 & 10
        if guessing != Empty:                                   #If inputs not empty
            try:                  #to predict that the input is int
                guessing = int(guessing)                         #To convert the input to int
                if int(10)>=guessing>=int(1):                
                    if guessing != Number:                        #If an entry is not equal to a random number
                        print(Fore.RED +'Try again '+Fore.WHITE+'\nNumber was : '+Fore.GREEN,Number,Fore.WHITE)   # For print("Try again") with colors
                        print('Number was: '+Fore.GREEN +Number + Fore.WHITE)
                    elif guessing == Number:                                      #If an entry is  equal to a random number
                            os.system('cls' if os.name == 'nt' else 'clear')      #For clean screen for finish    
                            print(Fore.CYAN+'\nwow amigo you won !!!\n')          #For print("wow amigo you won !!!")
                            break                     # To break loop
                else:
                    n1 = Fore.YELLOW+' 1 '+Fore.WHITE                             # For print Number '1' with color 
                    n10 = Fore.YELLOW+' 10'+Fore.WHITE                            # For print Number '10' with color
                    print(Fore.RED+'\n[+] '+Fore.WHITE+'I said a number between'+n1+'and'+n10)   #For print("[+] I said a number between 1 and 10")
            except :    #To predict that the input is str
                if type(guessing) is str :  #to convert the input to str
                    print('\nI meant a'+Fore.RED+' valid number'+Fore.WHITE+' not this')          #For Print(" I meant a valid number not this") with colors
        if guessing == Empty:      #If inputs not empty
            print(Fore.RED+'\n[+]'+Fore.WHITE+'come on try something'+Fore.RED+' !!'+Fore.WHITE)  #For print("[+]come on try something !!") with colors
            
        clean +=1            # To make clean screen after many trying
        if clean == int(4):  # To clean screen after 4 trying
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            clean -=4
except KeyboardInterrupt:    #To exit from code usnig Ctrl+Shift+C
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
    
    
