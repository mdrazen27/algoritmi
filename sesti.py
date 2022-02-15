def naci_broj_sa_ktom_cifrom(br):
    """
    Dat je cio broj k (1<=k<=180) i niz cifara 10111213...9899 koji se dobija kada se svei
    dvocifreni brojevi redom zapišu jedna iza drugog. Za dato k, odrediti dvocifreni broj koji sadrži
    k-tu cifru u datom nizu. Npr., za k=7, traženi broj je 13   
    """
    if (br-1)%2 == 0:
        return int(10+(br-1)/2)
    else:
        return int(10+(br-2)/2)


print(naci_broj_sa_ktom_cifrom(int(input("Unesite polozaj k-te cifre  "))))