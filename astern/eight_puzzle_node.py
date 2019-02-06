class EightPuzzleNode:
    def __init__(self, parent, state, action=None, path_cost=0):
        self.parent = parent
        self.state = state
        self.action = action
        self.path_cost = path_cost

    @property
    def unique(self):
        result = ""

        for item in self.state:
            result += str(item)

        return result

    @property
    def empty_index(self):
        return self.state.index(9)

    def get_possible_turns(self):
        empty_index = self.empty_index

        if empty_index == 0:
            return (1, 3)
        elif empty_index == 1:
            return (0, 2, 4)
        elif empty_index == 2:
            return (1, 5)
        elif empty_index == 3:
            return (0, 4, 6)
        elif empty_index == 4:
            return (1, 3, 5, 7)
        elif empty_index == 5:
            return (2, 4, 8)
        elif empty_index == 6:
            return (3, 7)
        elif empty_index == 7:
            return (4, 6, 8)
        elif empty_index == 8:
            return (5, 7)

    def get_child_nodes(self):
        child_node = []
        turns = self.get_possible_turns()

        for turn in turns:
            next_state = self.state.copy()
            next_state[self.empty_index] = next_state[turn]
            next_state[turn] = 9
            child_node.append(EightPuzzleNode(self, next_state, turn, self.path_cost + 1))

        return child_node

    def is_goal_node(self):
        last_item = 0
        for item in self.state:
            if last_item > item:
                return False
            last_item = item

        return True