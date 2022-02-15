def fudbal(zbir):
    """
    Petar je posmatrao fudbalsku utakmicu i na papiru zapisivao rezultat sa semafora
    poslije svakog gola. Npr. mogući zapis je: 1:0, 1:1, 1:2, 2:2, 2:3. Zatim je Petar sabrao sve
    zapisane brojeve: 1+0+1+1+1+2+2+2+2+3=15. Na osnovu datog zbira, napišite program koji
    odreñuje koliko je golova bilo na utakmici. Ulaz: U jednom redu dat je cio broj N – Petrov zbir (1
    ≤ N ≤1000). Izlaz: Štampati jedan cio broj – broj golova.
    """
    brojac = 0 
    while zbir > 0:
        brojac += 1
        zbir -=brojac
    print(brojac)

fudbal(int(input("unesite konacan zbir ")))