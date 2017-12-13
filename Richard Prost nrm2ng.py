#Numbri ära arvamise mäng. Arvuti genereerib arvu 1-5 ja sa pead 3 korraga ära arvama(v1.2)

import time
import sys
import random
import os

print("<*---------------------------*>")
print("Tervist! Kuidas ma teid kutsuda võin")
nimi = input("Tere! Minu nimi on: ")
time.sleep(0.5)
print("<*---------------------------*>")
print("Teretulemast minu mängu", nimi)
print("Sinu ülesanne on ära arvata number mille peale ma mõtlen!")
print("VIHJE: See on 1 ja 5 vahel.")
print("(3 PROOVI JÄREL)")
print("<*---------------------------*>")
time.sleep(2.5)

computernum = random.randrange(1, 5) 
arv1 = input('HMM.. Minu oletus on:') 

if int(arv1) == computernum:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Parema jalaga voodist astunud! Hästi tehtud.")
    time.sleep(0.5)
    print("MÄNG LÄBI")
    print("<*---------------------------*>")
    time.sleep(1)
    raise SystemExit
else:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Vale vastus!")
    time.sleep(1)
    print("Proovi uuesti! (2 PROOVI JÄREL)")
    time.sleep(0.5)
    print("<*---------------------------*>")
    
arv2 = input("Kurat! Minu teine oletus on:") 

if int(arv2) == computernum:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Eino kuradikurat, SA VÕITSID!")
    time.sleep(0.5)
    print("MÄNG LÄBI")
    print("<*---------------------------*>")
    time.sleep(1)
    raise SystemExit
else:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Vale!")
    time.sleep(1)
    print("Proovi uuesti! (1 PROOV JÄREL)")
    time.sleep(1)
    print("<*---------------------------*>")
    
arv3 = input("Oi isver! Minu viimane oletus on:") 

if int(arv3) == computernum:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Üle noatera! Sa võitsid!")
    time.sleep(0.5)
    print("MÄNG LÄBI")
    print("<*---------------------------*>")
    time.sleep(1)
    raise SystemExit
else:
    print("<*---------------------------*>")
    time.sleep(0.5)
    print("Vale!")
    time.sleep(1)
    print("Sa ei olegi nii tark kui sa paistad :)")
    time.sleep(0.5)
    print("MÄNG LÄBI")
    print("<*---------------------------*>")
    time.sleep(1)
    raise SystemExit




