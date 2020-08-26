
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    queue.enqueue(starting_node)
    path = [starting_node]
    counter = 0
    while queue.size() > 0:
        cur_child = queue.dequeue()
        new_path = list(path)
        for pair in ancestors:
            if pair[1] == cur_child:
                queue.enqueue(pair[0])
                new_path.append(pair[0])
        if len(path) == len(new_path):
            counter += 1
        else:
            counter = 0
            path = list(new_path)

    if cur_child == starting_node:
        return -1
    return path[-counter]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 8))


