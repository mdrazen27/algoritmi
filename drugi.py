def cif_jedinica_jednaka_cif_hilj(a):
    """
    Dat je četvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake,
    štampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra
    hiljada. Ako te dvije cifre nisu jednake, štampati zbir kvadrata svih cifara. 
    """
    zbir = 0
    if a//1000 == a%10:
        srednje_dvije_cifre= (a%1000)//10
        zbir = srednje_dvije_cifre**2
    else:
        
        while a > 0 :
            zbir += (a%10)**2
            a //= 10
    print(zbir)

cif_jedinica_jednaka_cif_hilj(int(input("Unesite cetvorocifreni broj "))) 