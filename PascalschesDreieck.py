# Ü5. Pascalsches Dreieck (mittel)

anzahl_zeilen = int(input("Gewünschte Anzahl an Zeilen eingeben"))
zeile = [1]

for i in range(anzahl_zeilen):
    print(zeile)
    neue_zeile = []
    neue_zeile.append(zeile[0])
    for i in range(len(zeile) - 1):
       neue_zeile.append(zeile[i] + zeile[i + 1])
    neue_zeile.append(zeile[-1])
    zeile = neue_zeile
