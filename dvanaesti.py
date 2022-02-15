def armstrong(num):
    """
    Prirodan broj n je Armstrongov ako je jednak zbiru kubova svojih cifara. Npr. 371 je
    Armstrongov, jer je 3^3+7^3+1^3=371. Napisati metod boolean isArmstrong(int n) koji
    za dati broj n provjerava da li je Armstrongov, i ako jeste, vraća true, a ako nije, vraća
    false. 
    """
    sum = 0
    num1 =  num
    while num1 > 0:
        sum += (num1%10)**3
        num1 //= 10
    return sum==num

print(armstrong(int(input("unesite broj "))))
