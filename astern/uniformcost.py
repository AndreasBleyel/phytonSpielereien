from astern import graph_node as gNode

class Queue:

    def __init__(self):
        self.queue = list()

    #Element hinzufügen
    def enqueue(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    #letztes Element wegnehmen
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue Empty!")

    def size(self):
        return len(self.queue)

    #sortieren der Queue um nächsten Punkt mit niedrigsten Kosten als letztes zu haben
    def sortQueue(self):
        self.queue.sort(key=lambda x: x[2], reverse=True)

    def ortsnamen_in_q(self):
        for item in self.queue:
            print("Ort: {} - Kosten: {} ".format(item[1].state, item[2]))

for ort in gNode.graph:
    print(ort)

weiter = True

while weiter:
    start = input("\nStartpunkt: ")
    ziel = input("Zielort: ")

    queue = Queue()

    besucht = {}
    pfad = []

    start_ort = gNode.GraphNode(None, start, 0)

    queue.enqueue((None, start_ort, start_ort.path_cost))

    while queue.size() > 0:
        vorgaenger, aktueller_ort, kosten = queue.dequeue()
        if aktueller_ort.state in besucht and besucht[aktueller_ort.state] < kosten:
            continue

        if aktueller_ort.is_goal_node(ziel):
            print("Route")
            print("Gesamt km: " + str(aktueller_ort.path_cost))

            pfad.append(aktueller_ort.state)
            while aktueller_ort.parent is not None:
                pfad.append(aktueller_ort.parent.state)
                aktueller_ort = aktueller_ort.parent

            pfad.reverse()
            for ort_pfad in pfad:
                print(str(ort_pfad), end=' ')

            break

        nachfolger = aktueller_ort.get_child_nodes()

        for nachf in nachfolger:
            if nachf.state not in besucht:
                queue.enqueue( (nachf.parent, nachf, nachf.path_cost) )

        queue.sortQueue()
        queue.ortsnamen_in_q()
        print("\nBereits besucht: ")
        besucht[aktueller_ort.state] = aktueller_ort.path_cost

        for besuchter_ort in besucht:
            print(besuchter_ort, end=' ')

        print("\n--------")

    weiter = True if input("\n\nWeiter? J/N ").lower() == "j" else False
