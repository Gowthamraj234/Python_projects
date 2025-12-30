# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:54:21 2024

@author: GOWTHAMRAJ P R
"""
#cand - candidates
#lov - list of voters
#vn - voter name
#vidn - voter id number
#iden - identity
#nam - name
#loc - list of candidates
#ctc - choose the candidate 
#cok - count of kiran
#coa - count of arjun
#nov - number of voters
#vpl - voted persons list

loc = {'kiran': 'a', 'arjun': 'b'}
lov = {'murugan': 1, 'janaki': 2, 'prem': 3}
cok = 0
coa = 0
nov = len(lov)
vpl = []

while nov >= 1:
    vidn = input("Enter the voter id number: ")

    while not vidn.isdigit():
        print("Invalid input. Please enter a valid voter id number.")
        vidn = input("Enter the voter id number: ")
    vidn = int(vidn)
    
    if vidn not in vpl:
        vpl.append(vidn)
        print(vpl)
        
        ctc = input("Enter 'a' for 'kiran' or 'b' for 'arjun': ")
        
        if ctc in loc.values():
            if ctc == 'a':
                cok += 1
            elif ctc == 'b':
                coa += 1
            else:
                print("Invalid candidate selected.")
        else:
            print("Invalid candidate selected.")
    else:
        print("This person has already voted.")
    
    nov -= 1

print("Votes for Kiran:", cok)
print("Votes for Arjun:", coa)

if cok > coa:
    print("The winner is Kiran")
elif coa > cok:
    print("The winner is Arjun")
else:
    print("Both Kiran and Arjun secured the same number of votes")