def F7(n):
    if n==0 or n==1 :
        return n
    else:
        return F7(n-1)+F7(n-2)
nbr=int(input("entrer l'indice "))
print(F7(nbr))