import networkx as nx
class UrlGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    def add_relation(self, src_url, dest_url):
        self.graph.add_edge(src_url, dest_url)
    def get_links_from(self, url):
        return list(self.graph.successors(url))
    def get_links_to(self, url):
        return list(self.graph.predecessors(url))
