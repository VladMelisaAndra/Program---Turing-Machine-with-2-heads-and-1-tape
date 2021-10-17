"""
GRUPA 143: Echipa formata din:
              Vlad Melisa-Andra
              Kayed Amar
              Buzescu Alexandru-Gabriel
"""


"""
!OBSERVATII!

Starile de accept si reject se vor numi intotdeauna(in configuratia masinii) q_accept respectiv q_reject.
Vom considera prima stare care apare in configuratie ca fiind starea initiala a masinii.
Se considera "_" ca fiind blank space.
Configuratia va fi citita din configuration.txt.
Tape-ul va fi citit tape.txt
Acest program nu accepta comentarii in configuration.txt, cu exceptia faptului ca ne-am scris grupa si numele nostru la inceputul lui.
"""

states=[] # Multimea starilor
sigma=[] # Alfabetul inputului
gamma=[] # Alfabetul benzii
delta1=[] # Functia de tranzitie a primului Head
delta2=[] # Functia de tranzitie a celui de al doilea Head
tape=[] # Tape-ul din tape.txt


def add_state(line): # Adaugam starea in states
    line = line.strip()     # Stergem spatiile albe din linie
    states.append(line)  # Adaugam starea extrasa in structura noastra de stari


def add_sigma(line): # Adaugam un element in alfabetul inputului
    line = line.strip()     # Stergem spatiile albe din linie
    sigma.append(line)      # Adaugam elementul in structura noastra pentru alfabetul inputului


def add_gamma(line): # Adaugam un element in alfabetul benzii
    line = line.strip()     # Stergem spatiile albe din linie
    gamma.append(line)      # Adaugam elementul in structura alfabetului benzii


def add_transition_1(line): # Adaugam o tranzitie in delta1
  line = line.split(" ")    # Separam linia in functie de spatii
  delta1.append({"state1":line[0],"state2":line[1],"citim":line[2],"scriem":line[3],"directie":line[4]})  # In structura delta1 adaugam un dictionar de forma: {starea_1: valoare_stare1, starea_2: val_stare2, citim: valoare_de_citit, scriem: valoare_de_scris, directie: directia_tranzitiei}


def add_transition_2(line): # Adaugam o tranzitie in delta2
  line = line.split(" ")    # Separam linia in functie de spatii
  delta2.append({"state1":line[0],"state2":line[1],"citim":line[2],"scriem":line[3],"directie":line[4]})  # In structura delta2 adaugam un dictionar de forma: {starea_1: valoare_stare1, starea_2: val_stare2, citim: valoare_de_citit, scriem: valoare_de_scris, directie: directia_tranzitiei}
  

def citire_reguli(): # Citim fisierul de configuratie
  with open("configuration.txt","r") as f:  # Deschidem fisierul "configuration.txt" pentru a il citi
    global start_state    # Declaram o variabila globla start_state
    start_state = "-1"      # Aceasta variabila globala are valoarea "-1"
    linie = f.readline()  # Citim prima linie din fisier
    
    while linie != "":    # Cat timp nu am ajuns la sfarsitul fisierului
      linie = linie.strip()   # Taiem spatiile din stanga si dreapta liniei citite
      
      if linie=="States:":    # Citim starile masinii
        linie = f.readline()  # Citim linia urmatoare
        linie = linie.strip() # Stergem spatiile din linia urmatoare
        
        while linie!="End":   # Cat timp mai avem stari de citit
          if linie != '':     # Daca linia nu reprezinta un spatiu gol
            if start_state=="-1":   # Daca starea initiala nu a fost inca determinata
              start_state=linie  # Consideram starea de start prima stare citita
            add_state(linie)   # Adaugam starea in states
          linie = f.readline().strip()  # Citim urmatoarea linie si stergem spatiile
      
      elif linie == 'Input_alphabet:': # Citim alfabetul inputului
        linie = f.readline()  # Citim o linie
        linie = linie.strip() # Stergem spatiile din linia citita
          
        while linie != "" and linie != "End":   # Cat timp nu am ajuns la sfarsitul fisierul si nu am dat de cuvantul "End"
          add_sigma(linie) # Adaugam elementul citit in structura noastra pentru sigma
          linie = f.readline().strip() # Citim urmatoarea linie si eliminam spatiile din stanga si dreapta liniei
          
      elif linie=="Tape_alphabet:": # Citim alfabetul benzii
        linie = f.readline()  # Citim o linie
        linie = linie.strip() # Stergem spatiile din linia citita
          
        while linie != "" and linie != "End":   # Cat timp nu am ajuns la sfarsitul fisierul si nu am dat de cuvantul "End"
          add_gamma(linie) # Adaugam elementul citit in structura noastra pentru gamma
          linie = f.readline().strip() # Citim urmatoarea linie si eliminam spatiile
          
      elif linie=="Transition_head_1:": # Functia de tranzitie a primului head
        linie = f.readline()    # Citim o linie
        linie = linie.strip()   # Stergem spatiile linioe
        
        while linie!="End":   # Cat timp nu am ajuns la cuvantul "End"
          if linie != '':     # Daca linia citita nu este un goala
            add_transition_1(linie) # Adaugam tranzitia in delta1
          linie = f.readline().strip()  # Citim urmatoarea linie si stergem spatiile
      
      elif linie=="Transition_head_2:": # Functia de tranzitie a celui de-al doilea head
        linie = f.readline()    # Citim o linie
        linie = linie.strip()   # Stergem spatiile liniei citite
        while linie!="End":     # Cat timp nu am ajuns la cuvantul "End"
          if linie != '':       # Daca linia citita nu este una goala
            add_transition_2(linie)   # Adaugam tranzitia in delta2
          linie = f.readline().strip()  # Citim urmatoarea linie si eliminam spatiile
    
      linie = f.readline()  # Citim o linie


def citire_tape(): # Functia de citit tape-ul din fisierul "tape.txt"
  with open("tape.txt","r") as g:  # Deschidem fisierul respectiv
    cuvant = g.readline() # Citim tape-ul ca si cuvant
    global tape   # Declaram o variabila globala numita tape
    tape = [x for x in cuvant] # Variabila tape devine caracterele din variabila cuvant


def verificare_stare_accept(i): # Verificam daca starea i este stare de accept 
  if i == "q_accept": 
    return True   # Daca este stare de accept returnam adevarat
  return False    # Altfel returnam fals
  
  
def verificare_stare_reject(i): # Verificam daca starea i este stare de reject
  if i == "q_reject":
    return True   # Daca este stare de reject returnam adevarat
  return False    # Altfel returnam fals
  

def blocaj(state): # Functie care verifica daca ne-am blocat(suntem in stare de accept/reject)
  if state == "q_accept" or state == "q_reject":
    return True   # Returnam adevarat in caz afirmativ
  return False    # Altfel returnam fals
  

def next_state_1(stare,head1,litera):   # Cautam urmatoarea stare din delta1, daca exista
  for dict in delta1:   # Parcurgem starile din delta1
    if litera == dict["citim"] and stare==dict["state1"]: # Daca gasim starea cu litera din tape[head1] corespunzatoare si starea in care am ajunge cu acea litera coincide
      tape[head1]=dict["scriem"]  # tape[head1] devine dict["scriem"]
      return [dict["state2"],dict["directie"]]    # Returnam starea si directia
  return [False,False]    # Altfel daca nu gasim starea, returnam o lista cu doua elemente false


def next_state_2(stare,head2,litera):   # Cautam urmatoarea stare din delta2, daca exista
  for dict in delta2:   # Parcurgem starile din delta2
    if litera == dict["citim"] and stare==dict["state1"]: # Daca gasim starea cu litera din tape[head2] corespunzatoare si starea in care am ajunge cu acea litera coincide
      tape[head2]=dict["scriem"]  # tape[head2] devine dict["scriem"]
      return [dict["state2"],dict["directie"]]    # Returnam starea si directia
  return [False,False]    # Altfel daca nu gasim starea, returnam o lista cu doua elemente false


def validare():   # Metoda de validare
  head1 = head2 = 0  # Initializam cele doua capete cu 0
  global stare_curenta  # Declaram o variabila gloaba numita "stare_curenta"
  stare_curenta =  start_state  # Initializam aceasta stare curenta cu starea de inceput
  i=1   # Ne luam si o variabila contor pe care o numim i si o folosim pentru a afisa indicele pasului curent pe care il efectueaza programul
  while blocaj(stare_curenta)==False:   # Cat timp starea noastra curenta nu prezinta un blocaj/mai putem trece in alte stari
    print("Pasul ",i)  # Facem simularea computatiei masinii Turing, afisand la fiecare pas cum se modifica variabilele din program
    i=i+1
    print(tape)   # Afisam tape
    print("head 1 = ",head1," head 2 = ",head2) # Afisam cele doua capete
    print("Stare curenta=", stare_curenta)  # Afisam starea curenta
    print("\n\n")
    
    x,directie=next_state_1(stare_curenta,head1,tape[head1])  # "x" reprezinta starea urmatoare a starii curente iar "directie" == directia prin care se ajunge la x din stare_curenta
    if x != False:  # Daca exista o stare urmatoare
      stare_curenta = x   # Starea curenta va deveni urmatoarea stare
      if directie=="R":   # Daca directia este right
        head1 = head1+1   # Atunci mergem cu head1 in dreapta
      else:      # Altfel, directia este left
        if head1!=0:  # Verificam intai daca putem merge in stanga cu head1
        
          head1 = head1-1   # Daca putem, atunci mergem cu head1 in stanga
          
    if stare_curenta!="q_reject":   # Daca starea curenta nu este starea finala de reject
      y,directie=next_state_2(stare_curenta,head2,tape[head2])  # Atunci y == starea urmatoare a starii curente si directie == directia prin care ajungem la y din stare_curenta
      if  y!= False:    # Daca exista o stare urmatoare dupa starea curenta
        stare_curenta = y   # Noua stare curenta va deveni y
        if directie=="R":   # Daca directia este right
          head2 = head2+1   # Mergem cu head2 in dreapta
        else:     # Altfel daca directia este left
          if head2!=0:    # Intai verificam daca se poate merge cu head2 in stanga
          
            head2 = head2-1   # Daca se poate, atunci mergem cu head2 in stanga

  print("Pasul ",i)  # Partea de final a simularii(ultimul pas)
  print(tape)   # Afisam tape-ul final
  print("head 1 = ",head1," head 2 = ",head2)
  print("Stare curenta=", stare_curenta)
  print("\n\n")        
 

    
     
citire_reguli()
#print(states)
#print(sigma)
#print(gamma)
#print(delta1)
#print("\n\n")
#print(delta2)
#print("\n\n")
#print(start_state)

citire_tape() 

#print(tape)
#print("\n\n")
validare()

if stare_curenta == "q_accept":
  print("A fost acceptat")
else:
  print("Nu a fost acceptat")


