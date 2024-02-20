# Corso Python WTU - Lezione 2 - 20/02/2024


# Given a list, create adjacents sublists of k length.
def create_adj_sublists(L,k):
    ret=[]
    for i in range(0,len(L)-k+1):
        ret.append(L[i:i+k])
    return ret
# L=[1,2,3,4,5,6,7,8,9]
# print(create_adj_sublists(L,2))
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]



# Given a list, creates contiguous sublists of k length.
# If the last sublist is not of k lenght, it will be the maximum minimum length given the list length.
def create_cont_sublists(L,k):
    ret=[]
    i=0
    while i<len(L):
        ret.append(L[i:i+k])
        i+=k
    return ret
# L=[1,2,3,4,5,6,7,8,9]
# print(create_cont_sublists(L,2))
# [[1, 2], [3, 4], [5, 6], [7, 8], [9]]




# per ordinare una lista in senso crescente
# senso crescente significa che gli elementi piu' grandi vanno alla fine, quindi if L[j]>L[j+1] allora 
# scambia l'elemento con indice j con l'elemento con indice j+1
def bubble_sort(L):
  # se creo una copia della lista, non modifico la lista iniziale. Se invece lavoro sulla stessa lista, 
  # la lista iniziale viene modificata. Gira il codice con e senza la prossima riga e 
  # vedi la differenza in cosa viene stampato
  L=L[:]
  # quando prendiamo i successivi o prossimi elemento, 
  # devo stare attento a dove parto e dove finisco
  for i in range(len(L)-1):
    for j in range(len(L)-1-i):
      if L[j]>L[j+1]:
        t=L[j]
        L[j]=L[j+1]
        L[j+1]=t

L=[1,4,5,2,3]
print(bubble_sort(L))
print(L)

