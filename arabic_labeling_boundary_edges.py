from igraph import *
import pandas as pd
g = load("boundary_labeled_graphs/arabic_boundary_nodes.graphml")
vs = g.vs.select(topic_eq = "None")
for topic in vs:
    boundary_vs = g.vs.select(status_eq = "boundary" + topic["name"])
    for boundary_node in boundary_vs:
        incident_edges = g.incident(boundary_node)
        for edge in incident_edges:
            full_edge = g.es.select(edge)[0]
            if(full_edge.source == boundary_node.index): #means boundary node is src
                opp_node = g.vs.select(full_edge.target)[0]
            if(full_edge.target == boundary_node.index): #means boundary node is target
                opp_node = g.vs.select(full_edge.source)[0] 
            my_boundary = "boundary" + topic["name"]
            if(opp_node["status"][0:8] == "boundary" and opp_node["status"]!= my_boundary):
                g.es[edge]["status"] = "Eboundary" + topic["name"]
            elif(opp_node["status"] == "internal"+ topic["name"]):
                g.es[edge]["status"] = "Einternal" + topic["name"]

g.save("boundary_labeled_graphs/arabic_boundary_edges.graphml")