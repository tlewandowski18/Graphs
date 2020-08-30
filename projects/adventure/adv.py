from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


#helper function to get edges. Takes room as argument. Returns object with keys equal to available directions and values equal to room in each direction
def get_neighbors(room):
    room_neighbors = {"completed": False}
    for exit in room.get_exits():
        room_neighbors[exit] = "?"
    
    return room_neighbors 

def traverse_world(player):
    traversal_dict = {}
    visited = [player.current_room.id]
    stack = Stack()
    stack.push(player.current_room)
    back_direction = []
    while stack.size() > 0:
        current = stack.pop()
        if f'{current.id}' not in traversal_dict:
            neighbors = get_neighbors(current)
            traversal_dict[f'{current.id}'] = neighbors
        current_directions = traversal_dict[f'{current.id}']
        if 'n' in current_directions and current_directions['n'] == '?':
            player.travel("n")
            traversal_path.append('n')
            back_direction.append("s")
            next_room = current.get_room_in_direction("n")
            if next_room.id not in visited:
                visited.append(next_room.id)
            traversal_dict[f'{current.id}']['n'] = next_room.id
            if f'{next_room.id}' not in traversal_dict:
                traversal_dict[f'{next_room.id}'] = get_neighbors(next_room)
            traversal_dict[f'{next_room.id}']['s'] = current.id
            stack.push(player.current_room)
        elif 's' in current_directions and current_directions['s'] == '?':
            player.travel("s")
            traversal_path.append('s')
            back_direction.append('n')
            next_room = current.get_room_in_direction('s')
            if next_room.id not in visited:
                visited.append(next_room.id)
            traversal_dict[f'{current.id}']['s'] = next_room.id
            if f'{next_room.id}' not in traversal_dict:
                traversal_dict[f'{next_room.id}'] = get_neighbors(next_room)
            traversal_dict[f'{next_room.id}']['n'] = current.id
            stack.push(player.current_room)
        elif 'w' in current_directions and current_directions['w'] == '?':
            player.travel("w")
            traversal_path.append('w')
            back_direction.append('e')
            next_room = current.get_room_in_direction('w')
            if next_room.id not in visited:
                visited.append(next_room.id)
            traversal_dict[f'{current.id}']['w'] = next_room.id
            if f'{next_room.id}' not in traversal_dict:
                traversal_dict[f'{next_room.id}'] = get_neighbors(next_room)
            traversal_dict[f'{next_room.id}']['e'] = current.id
            stack.push(player.current_room)
        elif 'e' in current_directions and current_directions['e'] == '?':
            player.travel("e")
            traversal_path.append('e')
            back_direction.append('w')
            next_room = current.get_room_in_direction('e')
            if next_room.id not in visited:
                visited.append(next_room.id)
            traversal_dict[f'{current.id}']['e'] = next_room.id
            if f'{next_room.id}' not in traversal_dict:
                traversal_dict[f'{next_room.id}'] = get_neighbors(next_room)
            traversal_dict[f'{next_room.id}']['w'] = current.id
            stack.push(player.current_room)
        elif len(visited) < 500:
            direction = back_direction.pop()
            player.travel(direction)
            traversal_path.append(direction)
            stack.push(player.current_room)
        #     traversal_dict[f'{current.id}']["completed"] = True
        # completed = True
        # for room in traversal_dict.values():
        #     if room["completed"] == False:
        #         completed = False
        # if not completed:
    # print(traversal_dict)
    print(len(visited))



    

traverse_world(player)

print(len(traversal_path))




# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
