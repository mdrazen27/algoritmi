def cifre_dva_broja(a3,a2,a1,b2,b1):
    """
    Date su cifre dva broja: jednog trocifrenog (a3, a2 i a1) i jednog dvocifrenog (b2 i b1).
    Cifre a1 i b1 su cifre jedinica, cifre a2 i b2 su cifre desetica, a a3 je cifra stotina. Ako je
    poznato da je zbir ta dva broja trocifren broj, odrediti cifre zbira.
    """
    broj1 = a3*100 + a2*10 + a1
    broj2 = b2*10 + b1
    zbir_brojeva = broj1 + broj2
    zbir_cifara = 0
    while zbir_brojeva > 0:
        zbir_cifara += zbir_brojeva % 10 
        zbir_brojeva //= 10
    return zbir_cifara

print(cifre_dva_broja(1,2,3,2,3))
print(cifre_dva_broja(1,2,3,4,5))
print(cifre_dva_broja(9,7,9,1,3))
