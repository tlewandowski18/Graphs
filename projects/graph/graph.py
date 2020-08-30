"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex (dequeue from queue)
            cur = queue.dequeue()
            # Check if the current vertex has not been visited:
            if cur not in visited:
                # print the current vertex
                print(cur)
                # Mark the current vertex as visited
                visited.add(cur)
                    # Add the current vertex to a visited_set
                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(cur):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex (pop from stack)
            cur = stack.pop()
            # Check if the current vertex has not been visited:
            if cur not in visited:
                # print the current vertex
                print(cur)
                # Mark the current vertex as visited
                visited.add(cur)
                    # Add the current vertex to a visited_set
                # push up all the current vertex's neighbors (so we can visit them next
                for neighbor in self.get_neighbors(cur):
                    stack.push(neighbor)
        


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex 
        queue = Queue()
        visited_vertices = set()
        # Create an empty set to track visited verticies
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            # set the current vertex to the LAST element of the PATH
            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path
                # Mark the current vertex as visited
                visited_vertices.add(current_vertex)
                    # Add the current vertex to a visited_set
                # Queue up NEW paths with each neighbor:
                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # take current path
                    # append the neighbor to it
                    # queue up NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push the PATH TO starting_vertex 
        stack = Stack()
        stack
        visited_vertices = set()
        # Create an empty set to track visited verticies
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # while the queue is not empty:
        while stack.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            # set the current vertex to the LAST element of the PATH
            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path
                # Mark the current vertex as visited
                visited_vertices.add(current_vertex)
                    # Add the current vertex to a visited_set
                # Queue up NEW paths with each neighbor:
                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # take current path
                    # append the neighbor to it
                    # queue up NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
