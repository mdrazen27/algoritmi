g = int(input("unesite broj galeona "))
s = int(input("unesite broj srpova "))
k = int(input("unesite broj knutova "))

def stanje_na_racunu(g,s,k):
    """
    jedan galeon vrijedi sedamnaest srpova, a jedan srp dvadeset
    devet knutova“. Napiši program koji za zadatu količinu galeona, srpova i knutova
    štampa kolika je ukupna količina tog novca izražena u knutovima
    """
    ukupno = k
    if g:
        ukupno += g*17*29
    if s:
        ukupno += s*29
    return ukupno

print(stanje_na_racunu(g,s,k))