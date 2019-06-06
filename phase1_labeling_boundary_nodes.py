from igraph import *
import pandas as pd
g = load("full_graphs_POL/phase1_polarized_full.graphml")
g.delete_vertices(g.vs.select(name_eq = "0t")[0].index) #to delete an extra node that is floating without a topic due to issue with df format
vs = g.vs.select(polar_eq = "None")
g.vs["status"] = None
print(len(vs))
for pole in vs: #for each community Gi
    # if(pole["name"] != "neu"): # uncomment and indent following block to exclude non-polarized tweets
    for member_id in g.neighbors(pole.index): #for each community member id
        member = g.vs.select(member_id)[0] #get full community member
        for neighbor_id in g.neighbors(member_id): # for each of neighbor'd ids
            neighbor = g.vs.select(neighbor_id)[0] #get full neighbor
            if (neighbor["polar"] != "None" and neighbor["polar"] != member["polar"] and member["polar"]!= "neu"): #normal node from other pole/reply
                member["status"] = "boundary"+ member["polar"]
for v in g.vs:
    # if (v["name"] != "neu" and v["polar"] != "neu"):  # uncomment and indent following block to exclude non-polarized tweets
    if(v["status"] is None):
        if (v["polar"] == "None"): #if pole node
            v["status"] = "boundary" + v["name"]
        else:
            v["status"] = "internal"+ v["polar"]
g.save("boundary_labeled_graphs/phase1_boundary_nodes.graphml")        