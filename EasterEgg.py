
############# Libraries #################
import os
import sys
import random
import numpy as np
import math
import re
from datetime import date
########################################
########## inizialization ##############
########################################

#nel caso in cui il programma non trovasse il path corretto sostituirlo con file_path=<path_corretto>. Se utilizzate Windows utilizzate \\ anzichè \ nel path. 

#print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
file_path = pathname
full_path=os.path.abspath(pathname)



##################################################################################################################################


def devil(nome_utente):

    file_in_w = open(file_path+"\\Patto col diavolo.txt","w")
    file_in_w.write(f"\n{nome_utente},\n\nha venduto volontariamente la propria anima al Diavolo in cambio della possibilità di ignorare l'esito della lettura dei Tarocchi.\n\n\n\tFirma\t\t\t\t\t\t\t\tData\n\t  Il Diavolo\t\t\t\t\t\t\t{date.today()}\n")
    file_in_w.close()
    
    print('''
MNMMMMMMMMMNMMMNMNhyyhmMMMMNodssNMMNmso---+hNMNMMMMMhmMMMMNd\n
MNMMMMMMMMMNMMMMy--..::/odNNmmNmNNy/-/----..hMMNMMMMNNMMMMMm\n
NMMMMMMMNMMMMMMo..--::+-.-:odNMNy-..://--:..+mNMMMMMMdmMMMMM\n
MMMNMMMMMMMNMMN..--::ooo-.--+ddh--.-odNh.:..+mNNmMMNMMmNMMMM\n
MMMMMMMMMMMNMMN:..::hMNm+::::---::+odMMy-:..dMMdNMNNMMmmMMMN\n
MMMNNMMMMMMMMMMm+--:yMNo+:--.----`/.:mN::.-oMMNMMNhNNMMmNMMN\n
MMMMMMMMMMMMNMNMNy-/+Mh``:`.:``-``-``sm-/::mmMMNhNNMmmMmNNMM\n
MMMMMMNMNMMMomNMMMo::Ny``.:-.-:--:`..+N/:-omNMmsoMMNmNMmmNMM\n
MMMMMMNMMMMNh/oyhs//yMhyy-:/s::s+--dhhMNs/:sys+/dMNNMMMdNMMM\n
NMMMMMNMMMMNdNhoo+ydMMNNMs`:/sd::`oMNMMNNmyssydNMNMNMMMMNhdN\n
MMMMMMMMMMNmmMMMMNNNMMMMdm.`/hm/.`shdMMNNMNdhNNMNMMMMMMMNMMN\n
MMMMMMNMNMMMMMMMNMMMMNMMh``-s/+y/``-NMMNNNmhyNNMNMNMNMMMMNdm\n
MMMMMNmNmmNNmNNMMNNMMMNNy``.N+/y+``/NNNNNNNNdMMMNMNMMMMMMMMM\n
MMMNMMMMMMMNhmMMMMMNMMNMMd.`/-.--.oNMNNNMMMMMMMMNMMMMMMNMMMN\n
MMMMMMMMMMMMMNMMMMMMMMMMMMh-:+:::/MMMMNMMMMMMMMMMMMMMMMMMMMM\n
MMNMMMMMdMMMMMMMNMMMMMMMMMd`.:`:`:MMMMMMMMMNmMMMNNMMMMMMMMMM\n
MMMMMNMMMMMMMMMMMNMMMMMMMMN.`s+s`+NMMMMMMMMNNNMMMMMMNmMMMMMM\n
NMMMNMMNMMNMMMMMNNMNMMMMMMms-/:/oyMMMMMMMMNNNNMMMMmMMNMmMMMM\n
MMMMMMMNMMMMMMMNNMNNNMMMMMMNN+-sMMMMMMMNMMMMNNNMMMMMNMMMMMMM\n
MMMMMMMMMMMMMNMMMMNdmNhyydNMMyoyMMMMNNNmMNNNMmmNMMMMMMNMMNMM\n
MMmMMMMMMMMMMNNNMMNhs+/:::+hmNmmMms+//+++oNMMNddMMMMMNMMMNMM\n
MMMMmMMMMMMMMMMMMdo:://:::/+sMMMd/:::::/+`sMMmMMMMMMMMMMMNMM\n
MMMMMMMMMMMNNMMMN:.``......-/NMN+///.```:`yNMMMMMMMMMMMNNMMM\n
MMMMMMMMMMMMMNNMMMmyo:-..````:d+-.`..-:+sdMMMMMNMMMMMMMMMMMM\n
MMMMMMMMMMMNNMNmNMMMMNhsooo:``o-`./ooydMMMMMMmNMMMMMMMNMMMMM\n
MMMMMMMMMMMMNNMMNddMMd````````/``.-:.//NMMNmNMMMMMMNMNMMMMMd\n
MMMMMNMMMNMMMNdMMMNdhm/```` ``+`````-`sNdmNMMMMMMMMNMMMMMMMM\n
MNMMMMMNMMMMMMMdNMMMMmho:````--:```.+ymmMMMMNNMMMMMNMMMMMMMM\n
hNMMMMMMMMMMMMMMmmMMMN/+//:-`h::`.://oomMMmmMMMMMMMMMMMMMMMM\n
MNmMMMNMNMNMMMMMMMddMM-````.`d//````.sNMmdNMMMMMMMMMMMMMMNMM\n
MdmNMNNMMMMNMMMMMMMNdds``````sd/` ``.hmdNMMMMmNMmhsyMMMMMMMM\n
NMNMmdMMMNNNMMMMMMMMMNdy/.```-y```--+ooyMMMMMMNo:--sMMMMMMNM\n
MNdMMNNdNMMNMMMMMMMMMM/.:::-`-``.:-.``.sMMMMMMho/:/mMMMMMMMM\n
MMNmMMNNMNdMMMMMMMMMMMdo-````.-`` ``-omMMMMMMMMMddNMMMMMMMMM\n
MMNmMMMMMmmNNNMMMMMMMMMMNmy+./dy+/+dNMMMMMMMMMMMMMMMMMMMMMMM\n
MMMNmMMMMMMMmmNMMMMMMMMMMMMmsysyhMMMMMMMMMMMMMMMMNMMMMMMMMMM\n
                                                            \n
                                                            \n
Patto accettato, sei libero di scegliere il tuo destino!AHAHAH\n
                                                            \n
                                                            \n
''')
     