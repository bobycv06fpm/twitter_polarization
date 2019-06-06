from igraph import *
import pandas as pd
g = load("full_graph_arabic/arabic_full.graphml")
g.delete_vertices(1900) #to delete an extra node that is floating without a topic due to issue with df format
vs = g.vs.select(topic_eq = "None")
print(len(vs))
for topic in vs: #for each community Gi
    # print(topic)
    for member_id in g.neighbors(topic.index): #for each community member id
        member = g.vs.select(member_id)[0] #get full community member
        for neighbor_id in g.neighbors(member_id): # for each of neighbor'd ids
            neighbor = g.vs.select(neighbor_id)[0] #get full neighbor
            if (neighbor["topic"] == "None" and neighbor["name"]!= member["topic"]): #other topic node
                member["status"] = "boundary"+ topic["name"]
            elif (neighbor["topic"] != "None" and neighbor["topic"] != member["topic"]): #normal node from other topic/reply
                member["status"] = "boundary"+ topic["name"]
for v in g.vs:
    if(v["status"] is None):
        if (v["topic"] == "None"): #if topic node
            v["status"] = "boundary" + v["name"]
        else:
            v["status"] = "internal"+ v["topic"]
g.save("boundary_labeled_graphs/arabic_boundary_nodes.graphml")        