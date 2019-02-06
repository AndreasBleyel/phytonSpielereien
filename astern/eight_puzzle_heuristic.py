coords = (
    (1, 1), (2, 1), (3, 1),
    (1, 2), (2, 2), (3, 2),
    (1, 3), (2, 3), (3, 3)
)

def h1(state):
    result = 0

    for index, item in enumerate(state):
        if item == 9:
            continue

        if (index + 1) != item:
            result += 1

    return result


def h2(state):
    result = 0

    for index, item in enumerate(state):
        if item == 9:
            continue

        if (index + 1) != item:
            current = coords[index]
            goal = coords[item - 1]
            result += abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    return result