def prosjek(n):
    """
    Napisati metod double prosjekOcjena (int n) koji provjerava da li je broj n
    pozitivan i ako jeste, učitava n cijelih brojeva koje predstavljaju ocjene iz matematike za n
    učenika vašeg odjeljenja i izračunava prosječnu ocjenu za tih n učenika. Ako n nije pozitivan,
    metod vraća 0. 
    """
    suma=0
    if n>0:
        for i in range(0,n):
            suma+= int(input(""))
        return suma/n
    return 0

print("Prosjek je ",prosjek(int(input("unesite broj ucenika"))))

    

