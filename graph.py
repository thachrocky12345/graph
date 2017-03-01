from collections import defaultdict
grids = [
    ['1', 'B', 'a', 'b', 'T'],
    ['T', 'T', 'C', 'H', 'B'],
    ['H', 'A', 'H', 'B', 'E'],
    ['E', 'C', 'D', 'U', 'I']
]
string_input = 'THACHBUI'

class Node(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def is_connect(self, node):
        if abs(node.x - self.x) <= 1 and abs(node.y - self.y) <= 1 and node.x != self.x:
            return True
        return False

    def __str__(self):
        return "{} - {} - {}".format(self.x, self.y, self.value)

class Grids(object):
    _nodes = None
    _letters = None
    def __init__(self, grid_matrix, string_input):
        self.grids = grid_matrix
        self.string =string_input

    @property
    def nodes(self):
        if self._nodes is not None:
            return self._nodes
        self._nodes = []
        for x, row in enumerate(self.grids):
            for y, value in enumerate(row):
                node = Node(x, y, value)
                self._nodes.append(node)
        return self._nodes

    @property
    def letters_path(self):
        if self._letters is not None:
            return self._letters
        self._letters = []
        for character in self.string:
            temp = []
            for node in self.nodes:
                if node.value == character:
                    temp.append(node)
            if len(temp) == 0:
                return None
            self._letters.append(temp)
        return self._letters

    def find_path(self, node, path=[]):

        while True:

            path = [self.letters_path[0][1]]

            for nodes, character in zip(self.letters_path[1:], self.string[1:]):
                for node in nodes:
                    if node.is_connect(path[-1]) and node.value == character:
                        path.append(node)
                        break


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))