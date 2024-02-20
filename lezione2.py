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
