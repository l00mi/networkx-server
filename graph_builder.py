import networkx as nx
import ijson
import gzip

config.VERSION="20160502"
config.PATH="/storage/datasets/"

def build_graph():
    parser = ijson.parse(bz2.open(config.PATH+'wikidata-'+config.VERSION+'-all.json.bz2', mode = 'rb'))
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2,3])
    G.add_edge(1,2)
    return G
