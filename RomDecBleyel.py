# Es soll ein Kommandozeilenprogramm entwickelt werden, welches römische Zahlen in arabische Zahlen
# konvertiert und umgekehrt. Der Programmablauf soll folgendermaßen aussehen:
# Die Benutzerin wird gegrüßt und dannach gefragt, ob Römisch>Arabisch oder Arabisch>Römisch konvertiert
# werden soll.
# Nach der Auswahl wird die Benutzerin gebeten eine Zahl einzugeben (entweder eine römische Zahl oder eben
# eine arabische Zahl).
# Es wird geprüft, ob die Eingabe korrekt ist, ansonsten wird die Eingabeaufforderung wiederholt mit einem
# Hinweis (ZB Falsche Eingabe, bitte wiederholen).
# Die eingegebene Zahl wird entsprechend konvertiert und ausgegeben.
# Das Programm soll mit den römischen Ziffern I, V, X, L, C, D, M umgehen können und Zahlen bis 5000
# unterstützen.

import re

def dec_to_rom(dec_value):
    result_roman = ""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    i = 0
    while dec_value > 0:
        for _ in range(dec_value // val[i]):
            result_roman += syb[i]
            dec_value -= val[i]
        i += 1
    print(result_roman)


def rom_to_dec(rom_value):
    conv_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result_decimal = 0
    for i in range(len(rom_value)):
        if i > 0 and conv_table[rom_value[i]] > conv_table[rom_value[i - 1]]:
            result_decimal += conv_table[rom_value[i]] - 2 * conv_table[rom_value[i - 1]]
        else:
            result_decimal += conv_table[rom_value[i]]
    print(result_decimal)


print("Hallo Unbekannt")

while True:
    conversion_typ = input("Für Römisch --> Arabisch drücke [1].\nFür Arabisch- --> Römisch drücke [2]\nJede andere Eingabe zum beenden")
    if conversion_typ != "1" and conversion_typ != "2":
        print("Bye")
        break

    if conversion_typ == "1":
        while True:
            user_input = input("römische Zahl eingeben von 0 bis 5000").upper()

            if re.match('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', user_input) is not None:
                rom_to_dec(user_input)
                break
            else:
                print("Keine römische Zahl erkannt")

    else:
        while True:
            user_input = input("arabische Zahl eingeben von 0 bis 5000")
            try:
                val = (int(user_input))
                if val > 5000 or val < 0:
                    print("Zahl muss zwischen 0 und 5000 liegen")
                else:
                    dec_to_rom(val)
                    break

            except ValueError:
                print("keine arabische ganze Zahl eingegeben")
