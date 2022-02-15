def kapetan_flint(unos):
    """
    Određuju se krajnje kordinate na osnovu niza ciji su clanovi string smjer North, South, East, West i
    broj koraka npr. "North 3" "East 4"
    """
    x, y = 0, 0
    for i in range(len(unos)):
        razdvojeno = unos[i].split(" ")
        smjer = razdvojeno[0]
        koraci =int(razdvojeno[1])
        if smjer == "North":
            y += koraci
        elif smjer == "South":
            y -= koraci
        elif smjer == "West":
            x += koraci
        elif smjer == "East":
            x -= koraci
    print(x, y)
    

kapetan_flint(["North 5","South 1","West 3"]) 

kapetan_flint(["South 2","East 5","West 5","North 14","South 12"])