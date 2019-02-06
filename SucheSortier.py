list = [0,1,2]
if list[0] is not None:
    print("a")
else: print("b")

def binary_search(list, value):
    erstes = 0
    letztes = len(list) - 1
    gefunden = False

    while erstes <= letztes and not gefunden:
        mitte = (erstes + letztes) // 2
        if list[mitte] == value:
            gefunden = True
        else:
            if value < list[mitte]:
                letztes = mitte - 1
            else:
                erstes = mitte + 1
    return mitte


list = [1, 2, 3, 4, 5, 6, 8, 10, 12, 56, 66, 78, 84, 99, 150, 250, 684, 7896, 12320]
print(binary_search(list, 12))


def selection_sort(list):
    for fillslot in range(len(list) - 1, 0, -1):
        pos_hochster_wert = 0
        for location in range(1, fillslot + 1):
            if list[location] > list[pos_hochster_wert]:
                pos_hochster_wert = location

        temp = list[fillslot]
        list[fillslot] = list[pos_hochster_wert]
        list[pos_hochster_wert] = temp


sel_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(sel_list)
print(sel_list)


# for i in range(len(sel_list)-1,0,-1):
#    print("i: " + str(i))
#    for location in range(1, i + 1):
#        print("loc: "+str(location))


## Link zur Präsentation von MergeSort
## https://drive.google.com/open?id=1A1nhH0AWNgHzWVJXg31MiW5e4BCylm4GTXQxgKgVbPM

def mergesort(list):
    if len(list) > 1:
        mitte = len(list) // 2
        links = list[:mitte]
        rechts = list[mitte:]


        mergesort(links)
        mergesort(rechts)

        i = 0
        j = 0
        k = 0

        while i < len(links) and j < len(rechts):
            if links[i] < rechts[j]:
                list[k] = links[i]
                i = i + 1
            else:
                list[k] = rechts[j]
                j = j + 1
            k = k + 1

        while i < len(links):
            list[k] = links[i]
            i = i + 1
            k = k + 1

        while j < len(rechts):
            list[k] = rechts[j]
            j = j + 1
            k = k + 1

mer_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergesort(mer_list)
print(mer_list)