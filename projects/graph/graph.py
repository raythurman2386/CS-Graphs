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
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()

        # Create a queue for BFT
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited.add(starting_vertex)

        while queue.size() > 0:
            # Dequeue a vertex
            # from the queue and print
            s = queue.dequeue()
            print(s)

            # Get all adjacent vertices of the dequeued vertex
            # If it hasnt been visited mark visited and enqueue it
            for i in self.vertices[s]:
                if i not in visited:
                    queue.enqueue(i)
                    visited.add(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Keep track of visited vertices
        visited = set()
        # Similar implementation to the bft,
        # Except dft will use a stack instead of a queue
        # Create a stack for DFT
        stack = Stack()
        stack.push(starting_vertex)
        visited.add(starting_vertex)

        while stack.size() > 0:
            s = stack.pop()
            print(s)

            for i in self.vertices[s]:
                if i not in visited:
                    stack.push(i)
                    visited.add(i)

    def dft_recursive(self, starting_vertex, v=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = v
        visited.add(starting_vertex)
        print(starting_vertex)

        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        # Create an empty set to track visited verticies
        visited = list()
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            cur_vertice = q.dequeue()
            prev_vert = cur_vertice[-1]

            if prev_vert == destination_vertex:
                return cur_vertice

            if prev_vert not in visited:
                neighbors = self.get_neighbors(prev_vert)

                for neighbor in neighbors:
                    new_vert = list(cur_vertice)
                    new_vert.append(neighbor)
                    q.enqueue(new_vert)

                    if neighbor == destination_vertex:
                        return new_vert

                visited.append(prev_vert)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = list()
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            cur_vertice = s.pop()
            visited.append(cur_vertice)
            for i in self.get_neighbors(cur_vertice):
                if i not in visited:
                    s.push(i)
                if i is destination_vertex:
                    visited.append(i)
                    return visited

    def dfs_recursive(self, starting_vertex, destination_vertex, v=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        if path is None:
            path = []  # because needs to be ordered
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        # check if it's our target node, if so return
        if starting_vertex == destination_vertex:
            return path
        # iterate over neighbors
        # check if visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # if not, recurse with a path
                result = self.dfs_recursive(
                    neighbor, destination_vertex, path, visited)
        # if this recursion returns a path,
                if result is not None:
                    # return from here
                    return result
        return None


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
    print(graph.vertices)
    print(graph.get_neighbors(2))

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
    print("\n*** BFT ***")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n*** DFT ***")
    graph.dft(1)
    print("\n*** DFT Recursion ***")
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
