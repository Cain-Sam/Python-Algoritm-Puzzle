import heapq


class Node:
    """
    Node class used to represent one spot on the board and all the nodes it is connected to
    """
    def __init__(self, x, y, value):
        self.coord = (x, y)
        self.value = value
        self.connection = []
        self.count = 0
        self.path = []

    def add_connection(self, node):
        """
        Add another node to the list of nodes connected to this one
        """
        self.connection.append(node)


def solve_puzzle(puzzle, source, destination):
    """
    Return one of the shortest paths from one given coordinate to another. It will only use free spaces on the board,
    going around blocked paths.

    Returns this path a list of coordinates.

    Board should be given as a list of lists with '-' representing a free space and '#' Representing and empty space.

    Source should be given as a tuple with two numbers representing the starting coordinate

    Destination should be given as a tuple with two numbers representing the ending coordinate
    """

    # Creating a graph of connected nodes based on the given board

    head = 'null'
    goal = 'null'
    node_graph = []

    # Creating a list of lists for node objects to be filled into
    for x in range(len(puzzle)):
        node_graph.append([])

        # Appending nodes to the list while also checking and setting our starting and ending nodes
        for y in range(len(puzzle[0])):
            cur_node = Node(x, y, puzzle[x][y])
            if x == source[0] and y == source[1]:
                head = cur_node
            if x == destination[0] and y == destination[1]:
                goal = cur_node
            node_graph[x].append(cur_node)

    # Adding connections to each node if there is an unblocked node next to it
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if x - 1 >= 0:
                if node_graph[x-1][y].value == '-':
                    node_graph[x][y].add_connection(node_graph[x-1][y])
            if y - 1 >= 0:
                if node_graph[x][y - 1].value == '-':
                    node_graph[x][y].add_connection(node_graph[x][y-1])
            if x + 1 < len(puzzle):
                if node_graph[x + 1][y].value == '-':
                    node_graph[x][y].add_connection(node_graph[x+1][y])
            if y + 1 < len(puzzle[0]):
                if node_graph[x][y + 1].value == '-':
                    node_graph[x][y].add_connection(node_graph[x][y+1])

    # Setting up our min-heap that will be used to find the shortest path
    visited = []
    unvisited = []
    cur_node = head

    # An incrementing number used to arbitrarily choose a path if there are multiple shortest paths
    tie_breaker = 0

    result = None

    head.path.append(head.coord)

    # If either the starting or ending node are blocked, return None
    if head.value == '#' or goal.value == '#':
        return None

    # Edge case if starting and ending node are the same node that isn't blocked
    if head == goal:
        return [head.coord]

    # Using a min-heap to find the shortest path, going through each node and recording the lowest count needed to get
    # there, moving outwards from the starting node and stopping when reaching the goal
    while cur_node != goal:
        if cur_node not in visited:
            visited.append(cur_node)

            # Since we start at the beginning node, we know this connection has been reached in the minimum steps
            for connect in cur_node.connection:
                if connect not in visited:
                    if not connect.path:
                        # Adding the path so far to the path of connected nodes
                        for x in cur_node.path:
                            connect.path.append(x)
                        connect.path.append(connect.coord)
                    connect.count = cur_node.count + 1
                    # Putting these paths into a list
                    heapq.heappush(unvisited, (connect.count, tie_breaker, connect))
                    tie_breaker += 1
        if len(unvisited) > 0:
            obj = (heapq.heappop(unvisited))
        # If we have run out of pathways without reaching the goal, then it is blocked, and we return None
        else:
            return None

        # Our next node to check will be one of the nodes with the shortest distance
        # obj[2] is the shortest connected path and will be checked next
        cur_node = obj[2]
        result = cur_node.path
    return result


"""
2D Representation of the board:
-  -  -  -  -
-  -  #  -  -
-  -  -  -  -
#  -  #  #  -
-  #  -  -  -
"""
board = [['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'], ['-', '-', '-', '-', '-'],
         ['#', '-', '#', '#', '-'], ['-', '#', '-', '-', '-']]

print(solve_puzzle(board, (0, 2), (2, 2)))
print(solve_puzzle(board, (0, 0), (4, 4)))
print(solve_puzzle(board, (0, 0), (4, 0)))
