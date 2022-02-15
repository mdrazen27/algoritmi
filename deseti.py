def domino(N):
    """
    Napišite program koji će odrediti ukupan broj tačkica na svim pločicama u potpunom
    skupu domina veličine N. Vaš program treba da učita jedan prirodan broj N (1 ≤ N ≤ 1000)
    veličinu potpunog skupa domina. Program treba da štampa ukupan broj tačkica na svim
    pločicama u potpunom skupu domina veličine N. Ne postoje dvije iste domine
    """
    ukupno = 0
    for i in range(1,N+1):
        for j in range(0,i+1):
            ukupno+= i+j
    return ukupno

print(domino(int(input("Unesite velicinu skupa domina"))))
