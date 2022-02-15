def kisjelina(h,s,o):
    """
    Napisati metod int kiselina(int h, int s, int o) koji za 3 data pozitivna cijela
    broja h, s i o koji redom predstavljaju broj molekula vodonika (H), sumpora (S) i kiseonika (O),
    vraća koliko se najviše molekula sumporne kiseline (H2SO4) može dobiti od datih molekula.
    Npr., ako je h=4, o=3 i s=10, odgovor je 2. 
    """
    a=h//2
    b=o//4
    if a<=s and a<=b:
        return a
    elif s<=a and s<=b:
        return s
    else:
        return b

h=int(input("Unesi broj molekula vodonika"))
s=int(input("Unesi broj molekula sumpora")) 
o=int(input("Unesi broj molekula kiseonika"))
print(kisjelina(h,s,o)) 
