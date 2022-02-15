def lozinka(str):
    """Lozinka je jaka ako je njena dužina najmanje 8 simbola, i sadrži mala slova, velika slova i cifre.
    Napisati program koji provjerava da li je lozinka jaka. Ulaz: Unosi se jedna riječ, dužine ne veće od
    100, koja sadrži mala i velika slova i cifre. Izlaz: Štampati YES ili NO,"""
    print(str)
    if len(str) < 8 and len(str) > 100:
        return False
    else:
        malo_slovo, veliko_slovo, cifra = 0, 0, 0
        for i in range(len(str)):
            if str[i] <= "z" and str[i] >= "a":
                malo_slovo = 1
            elif str[i] <= "Z" and str[i] >= "A":
                veliko_slovo = 1
            elif str[i] <= "9" and str[i] >= "0":
                cifra = 1
        if malo_slovo == 1 and veliko_slovo == 1 and cifra == 1: 
            return True 
        else:
            return False

if lozinka( input("Unesi lozinku :")):
    print("YES")
else: 
    print("NO")
