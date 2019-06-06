from igraph import *
import pandas as pd
g = load("boundary_labeled_graphs/phase2_boundary_nodes.graphml")
vs = g.vs.select(polar_eq = "None")
for polar in vs:
    boundary_vs = g.vs.select(status_eq = "boundary" + polar["name"]) #get boundary vertices of each polar
    for boundary_node in boundary_vs:
        incident_edges = g.incident(boundary_node)
        for edge in incident_edges:
            full_edge = g.es.select(edge)[0]
            if(full_edge.source == boundary_node.index): #means boundary node is src
                opp_node = g.vs.select(full_edge.target)[0]
            if(full_edge.target == boundary_node.index): #means boundary node is target
                opp_node = g.vs.select(full_edge.source)[0] 
            my_boundary = "boundary" + polar["name"] #name of my community's boundary nodes
            if(opp_node["status"][0:8] == "boundary" and opp_node["status"]!= my_boundary and opp_node["polar"] != 'None' and boundary_node["polar"] != 'None'): #if boundary node from diff community
                g.es[edge]["status"] = "Eboundary" + polar["name"]
            elif(opp_node["status"] == "internal"+ polar["name"]): #if internal node from my community
                g.es[edge]["status"] = "Einternal" + polar["name"]

g.save("boundary_labeled_graphs/phase2_boundary_edges.graphml")