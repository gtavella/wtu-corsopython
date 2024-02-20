# Lezione 1 - 19/02/2024


# operatore di assegnamento: assegno il valore 5 alla variabile x. non ritorna niente
x=5

# operatore di equivalenza: risponde alla domanda, e' vero che la variabile x e' uguale al valore 5? ritorna un booleano
# e' vero che e' vero che x e' uguale a 5?
x==5

# operatore diverso da: risponde alla domanda, e' vero che la variabile x e' diversa dal valore 5? ritorna un booleano
# siccome x e' uguale a 5, e' vero che x e' diverso da 5? no, e' falso che x e' diverso da 5.
# quindi e' vero che e' falso che x e' diverso da 5, cioe' e' vero che e' vero che x e' uguale a 5
x!=5


#***********

# Qual e' il valore di y? 7
x=5
y=x+1
y+=1

#***************

# Quali sono gli elementi della lista L? [1,1,0]
L=[0,0,0]
L[0]=1
A=L
A[1]=1


#************

# Che valore ha z? 9
def f(x):
  return x**2

def g(x):
  return x+1

x=2
z=f(g(x))



#*************


# condizionali 

nome='Giuseppe'
if nome=='Giorgia':
  print('Benvenuta Giorgia')
elif nome=='Giuseppe':
  print('Benvenuto Giuseppe')
else:
  print('Guarda la prossima volta')




#****************


# data una lista L, seleziona una sottolista R di L che parte dall'indice j e finisce all'indice n
# detto anche "loop parametrico", molto frequente  negli esercizi d'esame
# anche utilizzato per creare una copia dei valori di una lista
L=['a', 'b', 'c', 'd']
#  0     1    2    3     
R=[]

j=0
n=len(L)
for i in range(j,n):
  R.append(L[i])



#**************


# salva il massimo tra due numeri
# z contiene il piu' grande tra due numeri
x=3
y=1
z=x

if x>y:
  z=x
else:
  z=y


#**********

# richiesta: verifica che una lista e' non crescente

# parto dal definire cosa e' una lista crescente
# una lista e' crescente quando l'elemento attuale e' strettamente minore del prossimo
# L[i] < L[i+1]
# esempio: 1,2,3,4,5,6..

# poi nego la condizione di crescenza, quindi ottengo che una lista e' non crescente (quindi quello che mi interessa) 
# quando o l'elemento attuale e' uguale al prossimo, o l'elemento attuale e' maggiore del prossimo
# L[i] >= L[i+1]
# esempio: 6,5,5,4,2,1
# esempio: 6,4,3,2,1

# quindi in una lista non crescente, tutti gli elementi devono essere in quest'ultimo modo.
# di conseguenza, se anche solo due elementi sono crescenti, posso dire che la lista non e' non crescente


#*************



