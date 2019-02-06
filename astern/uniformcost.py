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
        vorgaenger, ort_node, kosten = queue.dequeue()
        if ort_node.state in besucht and besucht[ort_node.state] < kosten:
            continue

        if ort_node.is_goal_node(ziel):
            print("Route")
            print("Gesamt km: "+ str(ort_node.path_cost))

            pfad.append(ort_node.state)
            while ort_node.parent != None:
                pfad.append(ort_node.parent.state)
                ort_node = ort_node.parent

            pfad.reverse()
            for ort_pfad in pfad:
                print(str(ort_pfad), end=' ')

            break

        nachfolger = ort_node.get_child_nodes()

        for nachf in nachfolger:
            if nachf.state not in besucht:
                queue.enqueue( (nachf.parent, nachf, nachf.path_cost+kosten) )

        queue.sortQueue()
        besucht[ort_node.state] = ort_node.path_cost

    weiter = True if input("\n\nWeiter? J/N ").lower() == "j" else False
