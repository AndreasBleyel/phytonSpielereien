import re
import clipboard

def writedata():
    newfile = open("output.txt", "w+")
    finaldata2 = re.sub(' - ', '', newdata)
    finaldata = re.sub('- ', '', finaldata2)
    newfile.write(finaldata)
    newfile.close()

    clipboard.copy(finaldata)

    print("Done\n")
    print(finaldata)

fname = input("Dateinamen eingeben: (ENTER für Zwischenablage)")
if fname == "":
    zw = clipboard.paste()
    newdata = " ".join(zw.split())
    writedata()
else:
    try:
        with open(fname, "r") as f:
            data = f.read()
            newdata = " ".join(data.split())
            writedata()
    except FileNotFoundError:
        print("File not found")


