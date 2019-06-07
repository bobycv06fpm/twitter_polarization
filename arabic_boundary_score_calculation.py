from igraph import *
import pandas as pd
g = load("boundary_labeled_graphs/arabic_boundary_edges.graphml")
vs = g.vs.select(topic_eq = "None")
sum_node_values = 0
sum_boundary_nodes = 0
for topic in vs:
    boundary_vs = g.vs.select(status_eq = "boundary" + topic["name"]) #get topic's boundary nodes
    internal_vs = g.vs.select(status_eq = "internal" + topic["name"])
    total_vs = g.vs.select(topic_eq =  topic["name"])
    print(topic["name"] + ": ")
    print(len(internal_vs) / len(total_vs) )
    sum_boundary_nodes+=len(boundary_vs)
    node_value = 0
    for boundary_node in boundary_vs: #for each boundary node in this topic, calculate di and db
        incident_edges = g.incident(boundary_node)
        boundarySum = 0
        internalSum = 0
        for edge in incident_edges:
            full_edge = g.es.select(edge)[0]
            if(full_edge["status"][0:9] == "Eboundary"):
                boundarySum +=1
            else:
                internalSum +=1
        node_value += (internalSum / (internalSum + boundarySum)) - 0.5
    sum_node_values += node_value
print(sum_node_values)
print(sum_boundary_nodes)
print(sum_node_values / sum_boundary_nodes)



