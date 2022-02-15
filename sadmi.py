def prestupna_godina(godina):
    """
    Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
    poruku
    """
    if godina%4==0:
        if godina < 100:
            print(godina, " je prestupna godina")
        else:
            if godina%100==0:
                if godina%400==0:
                    print(godina," je prestupna godina")
                else:
                    print(godina, " nije prestupna godina")
    else:
        print(godina, " nije prestupna godina")


prestupna_godina(int(input("Unesite godinu ")))