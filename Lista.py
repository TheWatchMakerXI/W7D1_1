def lunghezza_parole(lista_parole):
    lista_lunghezze = [len(parola) for parola in lista_parole]
    return lista_lunghezze
#la funzione len in python fa si che restituisca un intero che sia la quantita' di lettere di ogni parola in questo caso, ma si puo' usare anche in altri modi

A = ["Harry", "Hermione", "Ron", "Hagrid", "Voldemort"]
B = lunghezza_parole(A)
print(B)  