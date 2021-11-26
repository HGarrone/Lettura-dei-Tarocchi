#############################################################################
###############                  Tarocchi                       #############
#############################################################################

print('''
#################################################################################################
####    Questo programma è stato ideato e sviluppato nella sua interezza da Hobey Garrone.   ####
####       I diritti delle descrizioni dei tarocchi vanno a "tarocchiecartomanzia.com"       ####
#################################################################################################
''')


#############        LIBRERIE        ###############
import os
import sys
import random
import numpy as np
from math import *
from importlib.machinery import SourceFileLoader

#nel caso in cui il programma non trovasse il path corretto sostituirlo con file_path=<path_corretto>. Se utilizzate Windows utilizzate \\ anzichè \ nel path. 

#print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
file_path = pathname
full_path=os.path.abspath(pathname)

tarocchi = SourceFileLoader('Tarocchi', file_path+'\\Tarocchi.py').load_module()
EasterEgg = SourceFileLoader('EasterEgg', file_path+'\\EasterEgg.py').load_module()

#############     INIZIALIZZAZIONE     ############
  
yes=("yes", "y", "Y", "YES", "Yes", "si", "Si", "SI", "s")
no=("no", "n", "N", "NO", "No")
arcani=("Il Bagatto","La Papessa","La Imperatrice","Lo Imperatore","Il Papa","Gli Amanti","Il Carro","La Giustizia","Lo Eremita","La Ruota","La Forza","Lo Appeso","La Morte","La Temperanza","Il Diavolo","La Torre","La Stella","La Luna","Il Sole", "Il Giudizio", "Il Mondo", "Il Matto")
carte=[]
senso=("dritto", "rovescio")
array=[0]*22
esito=[]
ambiti={1:"Amore", 2:"Lavoro_e_denaro", 3:"Salute", 4:"Persone", 0:"Dettagli"}
ambiti_scelti=[]
############     SCELTA NUMERO CARTE        ##############

nome_utente=input("Qual'è il tuo nome?\n")

while True:
    try:
        numero_carte=int(input("\nQuante carte vuoi pescare da 1 a 4?\n"))
        if numero_carte >0 and numero_carte<=4:
            print("\nScegli", numero_carte, "numeri da 1 a 22.")
            break
        else:
            print("\nNon si scherza col destino!")
    except ValueError:
        print("\nNon si scherza col destino!")
        
##########   SCELTA VALORI CARTE E ARRAY CASUALE DI CUI LA SCELTA SARà L'INDICE #########
        
for i in range(0,numero_carte,1):        
    while True:
        try:
            carte.append(int(input(f"{i+1}° carta: ")))
            if carte[i] not in range(1,22):
               print("\nQuesto non va bene! Scegli un numero intero tra 1 e 22")    
               carte.pop(i)
               continue
            else:
               print("\n")
               break
        except ValueError:
            print(("\nQuesto non è un numero! Scegli un numero intero tra 1 e 22"))

possible_value_arcani=list(range(0,22))
#print("\npossible_value_arcani pre-ciclo è:", possible_value_arcani)

for i in range(0,22):
     array[i]=random.choice(possible_value_arcani)
     possible_value_arcani.remove(array[i])  
    
#print("\npossible_value_arcani è:", possible_value_arcani)
#print("\nL'array è:", array)
#print("\nGli arcani sono:", arcani, "\nlunghezza arcani=", len(arcani))
#print ("\nLe carte sono:", carte)
       
       
############ SCELTA AMBITI #######################


possible_value_ambiti=list(range(1,5))
#print(f" ambiti possibili={possible_value_ambiti}, lunghezza={len(possible_value_ambiti)}, tipo {type(possible_value_ambiti[0])}")

for i in range(0,numero_carte):

    chiave_ambito=random.choice(possible_value_ambiti)
    possible_value_ambiti.remove(chiave_ambito)
    #print(f"ciclo {i} ambiti possibili={possible_value_ambiti}, lunghezza={len(possible_value_ambiti)}")
    ambiti_scelti.append(ambiti[chiave_ambito])
    
#print("ambiti scelti:", ambiti_scelti)

######### ARCANI COME VALORI IN ARRAY CASUALE CON INDICI IN ARRAY CARTE #######
  
  
print("\nGli arcani maggiori che hai pescato sono:\n")
for num in range(0,numero_carte):
    val=array[carte[num]-num]           #index error
    array.remove(val)
    #print ("\nLe carte sono:", carte)
    #print ("\nL' esito è:", esito)
    #print ("\nArray sono:", array)
    indice_senso=random.randint(0,1)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("+++++++++++++++", arcani[val], "rivolta per", senso[indice_senso],"++++++++++++++++\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(tarocchi.immagine(arcani[val], senso[indice_senso]))
    arcano_senso=[arcani[val], senso[indice_senso]]
    esito=np.append(esito, arcano_senso)

#for i in range(0, numero_carte):   
#    print ("L'esito è:", esito[2*i], esito[2*i+1], "e gli ambiti:", ambiti_scelti[i]) 

for i in range(0, numero_carte):
    print(f"\n ---------------------------\n|{ambiti_scelti[i]}({esito[2*i]},{esito[2*i+1]})| :\n ---------------------------\n", tarocchi.descrizione(esito[2*i],esito[2*i+1], ambiti_scelti[i]))   
      

########      loop dettagli carte      ############

uscire= "no"
while True:
    sapere=input(f"\n{nome_utente}, vuoi sapere il significato delle carte?\n")
    if sapere in yes:
       break
    elif sapere in no:
       uscire=input("\nDesideri uscire dal programma?\n")
       if uscire in yes:
          print(f"\nAddio, {nome_utente}!")
          break
       elif uscire in no:
           print(f"\nDunque hai cambiato idea, {nome_utente}...\n")
           continue
       else:
          print("\nNon capisco! Rispondi si o no!")
          continue
    else:
       print("\nNon capisco! Rispondi si o no!")
       continue
  
while True:  
    if uscire not in yes and sapere in yes:
        while True:
            if numero_carte>1:
               print("Di quale arcano vuoi conoscere il significato?")
               if numero_carte==2:
                  carta_interessata=input("Scrivi prima o seconda.\n")
                  if carta_interessata == "prima" or carta_interessata == 1 or carta_interessata == "seconda" or carta_interessata == 2 :
                     break
                  else:
                      print("ripeti")
                      continue
               elif numero_carte==3:
                  carta_interessata=input("Scrivi prima, seconda o terza.\n")
                  if carta_interessata == "prima" or carta_interessata == 1 or carta_interessata == "seconda" or carta_interessata == 2 or carta_interessata == "terza" or carta_interessata == 3 :
                     break
                  else:
                      print("ripeti")
                      continue
               elif numero_carte==4:
                  carta_interessata=input("Scrivi prima, seconda, terza o quarta.\n")
                  if carta_interessata == "prima" or carta_interessata == 1 or carta_interessata == "seconda" or carta_interessata == 2 or carta_interessata == "terza" or carta_interessata == 3 or carta_interessata == "quarta" or carta_interessata == 4 :
                     break
                  else:
                      print("ripeti")
                      continue
            else:
               carta_interessata="prima"
               break
               
        if carta_interessata == "prima" or carta_interessata == 1 :
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#            print(esito[0],"rivolta per", esito[1])
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("\n --------------------------\n",esito[0],esito[1],"\n --------------------------\n",tarocchi.descrizione(esito[0],esito[1],ambiti[0]))
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        elif carta_interessata == "seconda" or carta_interessata == 2 :
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#            print(esito[2],"rivolta per",esito[3])
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("\n --------------------------\n",esito[2],esito[3],"\n --------------------------\n",tarocchi.descrizione(esito[2],esito[3],ambiti[0]))
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        elif carta_interessata == "terza" or carta_interessata == 3 :
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#            print(esito[4],"rivolta per",esito[5])
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("\n --------------------------\n",esito[4],esito[5],"\n --------------------------\n",tarocchi.descrizione(esito[4],esito[5],ambiti[0]))
#            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        elif carta_interessata == "quarta" or carta_interessata == 4 :
            print("\n --------------------------\n",esito[6],esito[7],"\n --------------------------\n",tarocchi.descrizione(esito[6],esito[7],ambiti[0]))
        else:
            print("Errore!")
            
    else:
        break
        
    altra=input("\nVuoi sapere il significato di un'altra carta?")
    if altra in yes:
       continue
    elif altra in no:
       print(f"\nArrivederci, {nome_utente}!")
       break
    else:
       print("\nLo interpreto come un no! Arrivederci!")
       break

######Easter Egg###########

if numero_carte ==4:
    if carte[0]==carte[1] and carte[1]==carte[2] and carte[2]==6 or carte[1]==carte[2] and carte[3]==carte[2] and carte[3]==6 :
       EasterEgg.devil(nome_utente)
elif numero_carte ==3:
    if carte[0]==carte[1] and carte[1]==carte[2] and carte[2]==6:
       EasterEgg.devil(nome_utente)    