from igraph import *
import pandas as pd
g = Graph(directed = True)
users_df= pd.read_pickle("users_pickles/p2_users_df_with_polar")
g.add_vertex("pal")
pal_index = g.vs.select(name_eq = "pal")[0].index
g.add_vertex("neu")
pal_index = g.vs.select(name_eq = "neu")[0].index
g.add_vertex("isr")
pal_index = g.vs.select(name_eq = "isr")[0].index
def addVertices(df):
    edgelist = []
    for index,row in df.head(len(df)).iterrows():
        if(len(g.vs) == 0):
            g.add_vertex(row["username1"])
            g.add_vertex(row["username1"])
            index =  g.vs.select(name_eq = row["username1"])[0].index
            g.vs[index]["polar"] = row["p1"]
            polar_index = g.vs.select(name_eq = row["p1"])[0].index
            edgelist.append((index, polar_index))
        if(len(g.vs.select(name_eq = row["username1"])) == 0): #no vertex for same username exists
            g.add_vertex(row["username1"])
            index =  g.vs.select(name_eq = row["username1"])[0].index
            g.vs[index]["polar"] = row["p1"]
            polar_index = g.vs.select(name_eq = row["p1"])[0].index
            edgelist.append((index, polar_index))
        if(len(g.vs.select(name_eq = row["username2"])) == 0): #no vertex for same username exists
            g.add_vertex(row["username2"])
            index =  g.vs.select(name_eq = row["username2"])[0].index
            g.vs[index]["polar"] = row["p2"]
            polar_index = g.vs.select(name_eq = row["p2"])[0].index
            edgelist.append((index, polar_index))
    g.add_edges(edgelist)

def addEdges(df):
    edgelist = []
    for index,row in df.head(len(df)).iterrows():
        repliedto_index = g.vs.select(name_eq = row["username1"])[0].index
        reply_index = g.vs.select(name_eq = row["username2"])[0].index
        edgelist.append((reply_index, repliedto_index))
    g.add_edges(edgelist)

addVertices(users_df)
addEdges(users_df)

# layout = g.layout("kk")
# plot(g, layout=layout, vertex_size = 20)

g.save("users_graphs/p2_users_graph_with_polar.graphml")