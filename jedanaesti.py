def heming(num):
    """
    Prirodan broj n je Hemingov ako svi njegovi prosti djelioci pripadaju skupu {2,3,5}. Prvi
    Hemingov broj je 2, pa zatim idu 3, 4=2*2, 5, 6=2*3, 8=2*2*2, 9=3*3, 10=2*5, 12=2*2*3,
    15=3*5, itd. Npr. 14 nije Hemingov broj jer je 14=2*7, pa prosti djelioci broja 14 su 2 i 7 , a 7
    ne pripada skupu {2, 3, 5}. Napisati metod boolean isHemming(int n) koji za dati broj
    n provjerava da li je Hemingov, i ako jeste, vraća true, a ako nije, vraća false.
    """
    if num==1:
        return False
    if num%2 == 0:  
        while num%2==0:
            num=num/2
    if num%3 == 0:  
        while num%3==0:
            num=num/3
    if num%5 == 0:  
        while num%5==0:
            num=num/5
    return num==1
    
print(heming(int(input("Unesite broj "))))