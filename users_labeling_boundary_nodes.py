from igraph import *
import pandas as pd
g = load("users_graphs/p1_users_graph_with_polar.graphml")
# g = load("users_graphs/p2_users_graph_with_polar.graphml")
# g = load("users_graphs/p3_users_graph_with_polar.graphml")
vs = g.vs.select(polar_eq = "None")
g.vs["status"] = None
print(len(vs))
for pole in vs: #for each community Gi
    if (pole != "neu"):
        # print(topic)
        for member_id in g.neighbors(pole.index): #for each community member id
            member = g.vs.select(member_id)[0] #get full community member
            for neighbor_id in g.neighbors(member_id): # for each of neighbor'd ids
                neighbor = g.vs.select(neighbor_id)[0] #get full neighbor
                if (neighbor["polar"] != "None" and neighbor["polar"] != member["polar"]): #normal node from other pole/reply
                    member["status"] = "boundary"+ member["polar"]
for v in g.vs:
    if(v["status"] is None):
        if (v["polar"] == "None"): #if pole node
            v["status"] = "boundary" + v["name"]
        else:
            v["status"] = "internal"+ v["polar"]
g.save("boundary_labeled_graphs/phase1_users_boundary_nodes.graphml") 
# g.save("boundary_labeled_graphs/phase2_users_boundary_nodes.graphml"
# g.save("boundary_labeled_graphs/phase3_users_boundary_nodes.graphml"       