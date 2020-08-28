
from util import Stack, Queue

def get_parents(node, ancestors):
    parent_list = []
    for pair in ancestors:
        if pair[1] == node:
            parent_list.append(pair[0])
    return parent_list
'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
#bft
def earliest_ancestor(ancestors, starting_node):
    if len(get_parents(starting_node, ancestors)) == 0:
        return -1
    queue = Queue()
    queue.enqueue({
        "cur_node": starting_node,
        'path': [starting_node]
    })
    visited = set()
    paths = []

    while queue.size() > 0:
        cur_child = queue.dequeue()
        cur_child_node = cur_child['path'][-1]
        cur_child_path = cur_child['path']
        if cur_child_node not in visited:
            visited.add(cur_child_node)
            parents = get_parents(cur_child_node, ancestors)
            if len(parents) > 0:
                for parent in parents:
                    new_path = list(cur_child_path)
                    new_path.append(parent)
                    queue.enqueue({
                        'cur_node': parent,
                        'path': new_path
                    })
            elif len(parents) == 0:
                paths.append(cur_child_path)
    if len(paths) == 1:
        return paths[0][-1]
    longest_path = paths[0]
    length = len(longest_path)
    for path in paths:
        if len(path) == length and path[-1] < longest_path[-1]:
            longest_path = path
        elif len(path) > length:
            longest_path = path

    return longest_path[-1]
    # if cur_child == starting_node:
    #     return -1
    # return path


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 9))


