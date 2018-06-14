from collections import defaultdict

class Vertex:
    def __init__ (self, key):
        self.key = key
        self.edge_list = {}

    def get_key (self):
        return self.key

    def add_neighbor (self, nbr, cost):
        if nbr.get_key() not in [x.get_key() for x in self.edge_list]:
            self.edge_list[nbr] = cost
            print "Adding neighbor %u -> %u (%u)" % (self.get_key(), nbr.get_key(), cost)

    def get_edges (self):
        return self.edge_list

    def show (self):
        print "\nVertex %u => " % (self.get_key()), 
        for nbr in self.edge_list:
            print "(%u:%u) " % (nbr.get_key(), self.edge_list[nbr]),

class Graph:
    def __init__(self, graph_dict):
        self.vertex_list = {}
        for v in graph_dict:
            self.add_vertex(v)
            for e in graph_dict[v]:
                self.add_edge(v, e, graph_dict[v][e])
                
    def get_vertex (self, key):
        return self.vertex_list[key] if key in self.vertex_list else None

    def add_vertex (self, key):
        if key not in self.vertex_list:
            v = Vertex(key)
            self.vertex_list[key] = v
            print "Adding vertex %u" % (key)

    def add_edge (self, from_vertex, to_vertex, cost):
        if from_vertex not in self.vertex_list:
            f = self.add_vertex(from_vertex)

        if to_vertex not in self.vertex_list:
            t = self.add_vertex(to_vertex)

        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], cost)

    def show (self):
        for v in self.vertex_list:
            self.vertex_list[v].show()
