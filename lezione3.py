# Corso Python WTU - Lezione 3 - 21/02/2024

L=[1,2,3,4]

print(L)

#  attenzione - quando eliminiamo un certo elemento all'indice i,
# automaticamente tutti gli altri elementi "slittano" nel rispettivo indice

i=0
x=1

# rimuove per valore
L.remove(x)
# rimuove per indice
L.pop(i)

print(L)

"""
Due variabili che hanno nomi diversi possono puntare allo stesso oggetto.
Se due persone si chiamano Maria Rossi ed entrambe abitano nella stessa casa, quindi stessa citta', stessa via e stesso indirizzo,
questa e' solo una coincidenza. Infatti, due persone si possono chiamare con nomi diversi ma abitare allo stesso indirizzo.

Quindi bisogna porsi la domanda: per "stesso oggetto", intendo lo stesso oggetto in memoria? O lo stesso contenuto dell'oggetto?

Due oggetti possono avere lo stesso identico contenuto (ovvero, stessi elementi, con stesso ordine, con stessa lunghezza) ed essere in indirizzi di memoria diversi.
Quindi ne segue che:
(1) Se due oggetti sono in indirizzi di memoria diversi, possono avere lo stesso contenuto, come no. Ma questo non e' garantito. 
Esempio:
A=[1,2,3]
B=[1,2,3]

E' solo una coincidenza il fatto che A e' uguale a B, uguale nel senso di "lo stesso contenuto". 
Quindi stesso contenuto, diversi indirizzi di memoria. Siccome sono in diversi indirizzi di memoria, 
anche se all'interno sono identici, sono di fatti due oggetti diversi.
E' come dire che due persone hanno la stessa personalita' solo perche' hanno lo stesso nome. 
Stesso nome, personalita' diverse.
Oppure stesso nome, personalita' uguale - ma questa e' solo una coincidenza e non e' garantito.

Se invece ho:

A=[1,2,3]
B=[1,2,4]

questi non solo sono due oggetti diversi solo per il fatto che sono in due indirizzi di memoria diversi, 
ma anche il loro contenuto e' diverso.


(2) Se due oggetti si trovano allo stesso indirizzo di memoria, sicuramente anche il loro contenuto sara' uguale. Questo e' garantito.
Esempio:
A=[1,2,3]
B=A

Se modifico A, modifico anche B.
Se modifico B, modifico anche A.
Il contenuto di A sara' sempre uguale a quello di B.
In entrambi i casi sto modificando non A o B, ma l'oggetto in memoria al quale puntano. 

Le variabili A e B si dice che puntano allo stesso oggetto in memoria. Siccome in un indirizzo di memoria si puo' trovare solo un oggetto, 
ne segue che noi siamo sicuri che anche il suo contenuto sara' uguale.

Se per indirizzo di memoria intendo il corpo di una persona, nel corpo di una persona puo' vivere una sola persona. 
Quindi se quella persona si chiama Maria Rossi, o decide di cambiare nome, o ha un nickname Mary2003, MariTheBest97 o @marynevermind, sempre quella persona e'. 
Quindi "modificando il corpo" di MariTheBest97, modifico automaticamente il corpo di Mary2003 e di Maria Rossi.
Se Mary2003 decide di andare in palestra per dimagrire, sara' dimagrita anche @marynevermind. E cosi via.

Infatti A e B in questo caso si chiamano alias - variabili/nomi diversi per indicare lo stesso oggetto in memoria.

"""

#*********************


s='oggi, facciamo, corso python, wtu'
char_speciale=','
parole=s.split(char_speciale)

print(f'Il carattere speciale che hai utilizzato e\': {char_speciale}')
print(parole)

# esempio
'ciao oggi e\' soleggiato'
# backslash (\) e' un carattere di escape che dice "considera questo carattere letteralmente 
# e non come un carattere che ha significato per il linguaggio di programmazione"


# Crea un programma che, data una lista di caratteri speciali char_speciali e una stringa s, 
# splitta quella stringa s per qualsiasi carattere speciale in char_speciali

char_speciali=[',', '.', ':']
s='Oggi, no aspetta. Vorrei: una bottiglia d\'acqua. Ok, va bene.'

for i in range(len(char_speciali)):
  char_speciale=char_speciali[i]
  risultato=s.split(char_speciale)
  print(f'Il carattere speciale che hai utilizzato e\': {char_speciale}')
  print(risultato)
  print()


# ARGOMENTI & PARAMETRI

# ESEMPIO A
# x e' il parametro di f
# nella definizione di funzione, parliamo di parametri
# dietro le quinte, quando f(x) viene invocata, l'argomento di f(x) viene assegnato ad x
# quindi x=y
def f(x):
  return x
  
y=2
# y e' l'argomento di f
# nella chiamata (o invocazione) della funzione, quello che viene passato e' un argomento
z=f(y)




# ESEMPIO B
# x e' il parametro di f
# nella definizione di funzione, parliamo di parametri
# quindi x=2
def f(x):
  return x

# passiamo l'argomento t al parametro z, quindi
# z=t
def g(z):
  return z

t=2
# y e' l'argomento di f
# nella chiamata (o invocazione) della funzione, quello che viene passato e' un argomento
x=f(g(t))


# ALTRO ESEMPIO - per dimostrare che il modo in cui chiamo i parametri puo' essere diverso dal modo in cui chiamo gli argomenti
# nota- il passaggio di parametri/argomento avviene in modo ordinale, 
# cioe' il primo argomento viene assegnato al primo parametro e cosi via, quindi in questo caso

# cosa accade dietro le quinte quando invoco calcola_qualcosa
# X=L1
# Y=L2
# k=k4
# dichiarazione di funzione
# def calcola_qualcosa(X, Y, k):
#   pass

# invocazione di funzione
# calcola_qualcosa(L1, L2, k4)



# morale della storia: non importa come chiamo i parametri, l'importante e' che siano ordinati nel modo corretto


  
#*************



# Conta occorrenze di una lettera in stringa
# Scrivi una funzione conta_lettera che accetta come parametro l che e' la lettera da cercare nella stringa s, 
# e ritorna il numero di volte (occorrenze) in cui compare nella stringa
# Ottieni input da terminal/prompt

# DOMANDE PER PROGETTARE SOLUZIONE
# 1. Cosa mi serve come input per fare questo lavoro/calcolo? INPUT
# 2. Cosa voglio ritornare? Che tipo di dato sara'? OUTPUT
# 3. Come faccio questa operazione? COME/CALCOLO


# nota - e' solo una pura coincidenza il fatto che il nome dei parametri e' uguale al nome degli argomenti
def conta_lettera(s,l):
  cont=0
  for x in s:
    if x==l:
      cont = cont + 1
      # oppure
      # cont+=1
  return cont
    

s=input('Inserisci stringa: ')
l=input('Inserisci lettera: ')
n_occorrenze=conta_lettera(s,l)
print(n_occorrenze)



#*****************

# Scrivi una funzione conta_lettere che accetta come parametro lettere che e' una lista di lettera (non una sola lettera) 
# da cercare nella stringa s, e ritorna il numero di volte (occorrenze) in cui la generica lettera compare nella stringa s
# Ottieni input da terminal/prompt

# Ci siamo resi conto che in realta' possiamo generalizzare questa soluzione non modificando la soluzione iniziale, 
# ma riutilizzando proprio la soluzione iniziale. questo ci permette di mantenere il codice riutilizzabile e scalabile

# splitta per carattere speciale (parametrico)
carattere_speciale=input("inserisci carattere separaratore:")
lettere=input('Inserisci lettere separate da virgola senza spazio: ').split(carattere_speciale)
print(lettere)

for lettera in lettere:
  n_occorrenze=conta_lettera(s,lettera)
  print(n_occorrenze)


"""
se avessi invece creato tanti if, o tante variabili, tante quanti sono il numero di input, 
avrei creato un programma impossibile da scalare o riutilizzare. 
Quindi l'astuzia e' farsi questa domanda: come posso aumentare le funzionalita' del mio programma, 
senza aumentare di troppo la complessita' della soluzione in proporzione all'input?
Cioe' se ho k input, non posso di certo creare k variabili o if.

Quindi posso pensare a dei modi di generalizzare la soluzione cominciando a parlare di k input invece di 4 input, ad esempio.
Come? Posso cominciare a notare le cose specifiche che utilizzo nel mio programma. 
Quantita' specifiche, numeri prefissati, oggetti inizializzati etc. spesso bisogna generalizzare il piu' possibile 
e avere troppe oggetti/numeri concreti (aiuta all'inizio ad imparare a programmare, sicuramente) 
# tuttavia quando il programma cresce, non rende il codice riutilizzabile.

Se utilizzo un numero concreto/specifico, ad esempio 7, posso chiamarlo x.
Se utilizzo una lista specifica [6,3,0] posso generalizzarla e chiamarla L.
Sostituire lo specifico con il generico/parametrico - questa e' la strategia. 
Ne segue che piu' cose specifiche/prefissate ho, meno scalabile e riutilizzabile sara' il mio programma.

Un modo per generalizzare e' questo che abbiamo appena visto sopra: creo una soluzione che vale per un caso specifico, 
e poi applico qualche tipo di iterazione per applicare quella specifica soluzione n volte 

"""
