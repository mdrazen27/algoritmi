def m_djeljivo_sa_n(m,n):
    """
    Napisati kod koji učitava dva cijela broja x i y štampa poruku „x je djeljiv sa y” ili „x nije
    djeljiv sa y“. Npr. „15 je djeljiv sa 3“ ili „15 nije djeljiv sa 4“.
    """
    if m%n==0:
        print(m, " je djeljiv sa ", n)
    else:
        print(m, " nije djeljiv sa ", n)

m_djeljivo_sa_n(int(input("Unesi broj x ")), int(input("Unesi broj y ")))

