def prosti_djelioci(n):
    """za dati broj n štampa sve proste djelioce broja n"""
    for i in range(1,n+1):
        count = 0
        if n%i ==0:
            for j in range(1,i):
                if i%j == 0:
                    count += 1
        if count == 1:
            print(i)

prosti_djelioci(int(input("Unijeti broj n ")))
