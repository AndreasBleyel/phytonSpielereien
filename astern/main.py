from astern import graph_node as gn
from astern import eight_puzzle_node as epn
from astern import astar_search as search
from astern import graph_heuristic as gh
from astern import eight_puzzle_heuristic as eh

#root = gn.GraphNode(None, "Frankfurt")
#node = search.astar_search(root, gh.h1)

root = epn.EightPuzzleNode(None, [7,2,4,5,9,6,8,3,1])
node = search.astar_search(root, eh.h2)
#node = search.astar_search(root, eh.h1)

path = []
while True:
    if node:
        path.append(node.action)

    node = node.parent

    if node == None:
        break

path.reverse()
print(len(path))
print(path)


