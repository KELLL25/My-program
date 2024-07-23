import time
import os
import subprocess
import random
poäng = 0
subprocess.run("cls", shell=True)

User = open("userbas.txt", "a")
Passwords = open("passbas.txt", "a")
writeruser = open("userbas.txt", "a")
writerpass = open("passbas.txt", "a")
US = open("userbas.txt")
PS = open("passbas.txt")


starta = input("Do you wish to start? :[j][n] ")
subprocess.run("cls", shell=True)
if starta == "j":
    print("Welcome")
    time.sleep(1)
    skapa_logga = input("Do you have an account or do you need to make one: [make] [logg] ")
    #--------------------------------------------------
    if skapa_logga == "make": #skapa nya användare
        subprocess.run("cls", shell=True)
        AnvändarNamn = input("User Name:")
        time.sleep(1)
        Lösenord = input("Password: ")
        writeruser.write(AnvändarNamn)
        writerpass.write(Lösenord)
        starta = "Poop"
        #----------------------------------------------
    if skapa_logga == "logg": # Logga in användare
        subprocess.run("cls", shell=True)
        logps = PS.read()
        logus = US.read()
        logANV = input("UserName: ")
        time.sleep(0.5)
        logLös = input("Password: ")
        if logANV == logus:
            print("Loading")
            if logLös == logps:
                AnvändarNamn = logus
                starta = "Poop"
            else:
                print("Wrong Password X")
        else:
            print("Wrong Username X")
        #-------------------------------------------------

if starta == "Poop":
    print("Welcome " + (AnvändarNamn))
    time.sleep(5)
    subprocess.run("cls", shell=True)
    while True:
        US.close()
        PS.close()
        PoopWhile = input("")
        if PoopWhile == "cls": #clear
            subprocess.run("cls", shell=True)
        if PoopWhile == "pass":
            passWordcheck = input("Wright your Password: ")
            if passWordcheck == Lösenord:
                print("here are your passwords")
                print(Lösenord)
        if PoopWhile == "quit":
            quit()
        if PoopWhile == "help":
            print("cls = clear ")
            print("pass = All your passowrds")
            print("spel = A game")
            print("quit = Quit")
 
        if PoopWhile == "spel": # spel
            subprocess.run("cls", shell=True)
            print("Welcome to guess the number")
            botsiffra = random.randrange(1, 100)
            subprocess.run("cls", shell=True)
            siffra_du_gissat = input("what numeber do you think it is [1, 100]: ")
            if siffra_du_gissat == botsiffra:
                print("Congratts you got it")
                time.sleep(0.5)
                spela_igen = input("Do you wish to play again [j][n] ")
                if spela_igen == "j":
                    subprocess.run("cls", shell=True)
                    infspel = True
                    while infspel:
                        botsiffra = random.randrange(1, 100)
                        siffra_du_gissat = input("what numeber do you think it is [1, 100]: ")
                        if siffra_du_gissat == botsiffra:
                            poäng = poäng + 1
                            print("Congratts you got it")
                            print("if you whant to go back wright: [back]")
                            time.sleep(2)
                            subprocess.run("cls", shell=True)
                        else:
                            print("Damit you got it wrong")
                            print("if you whant to go back wright: [back]")
                            time.sleep(2)
                            subprocess.run("cls", shell=True)
                        if siffra_du_gissat =="back":
                            infspel = False
                            print("the game just ended!")
            else:
                print("Damit you got it wrong")
                time.sleep(0.5)
                spela_igen = input("Do you wish to play again [j][n] ")
                if spela_igen == "j":
                    subprocess.run("cls", shell=True)
                    infspel = True
                    while infspel:
                        botsiffra = random.randrange(1, 100)
                        siffra_du_gissat = input("what numeber do you think it is [1, 100]: ")
                        if siffra_du_gissat == botsiffra:
                            poäng = poäng + 1
                            print("Congratts you got it")
                            print("if you whant to go back wright: [back]")
                            time.sleep(2)
                            subprocess.run("cls", shell=True)
                        else:
                            print("Damit you got it wrong")
                            print("if you whant to go back wright: [back]")
                            time.sleep(2)
                            subprocess.run("cls", shell=True)
                        if siffra_du_gissat =="back":
                            infspel = False
                            print("the game just ended!")
else:
    quit()
