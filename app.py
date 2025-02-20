# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:49:06 2025

@author: romar
"""

import random
import time 
from datetime import datetime
from tkinter import * 
from playsound import playsound


nombre_aleatoire = random.randint(0, 1)
i = 0
liste_logs = {}
fenetre = Tk()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

while i < 10 :
    nombre_aleatoire = random.randint(0,1)
    print(nombre_aleatoire)
    i+=1 
    current_dateTime = datetime.now()
    if nombre_aleatoire == 1 :
        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(padx=30, pady=30)
        Label(Frame1, text="Mouvement détécté",background="red").pack(padx=10, pady=10) 
        liste_logs[current_dateTime] = "Mouvement détecté"
        playsound("../Detecteur de mouvement/1645.mp3")
     
        
        
        
     
    else :
     
        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack( padx=30, pady=30)
        Label(Frame1, text="Aucun mouvement",background="green").pack(padx=10, pady=10) 
        liste_logs[current_dateTime] = "Aucun mouvement détecté"
         
        time.sleep(1)  
           
fenetre.mainloop()    
print("Date et heures des mouvements : ")
with open('logs.txt',"w") as f :
  for keys,values in liste_logs.items():
    print(keys," : ",values) 
    msg = f"{keys} : {values}\n"
    f.write(msg)
    