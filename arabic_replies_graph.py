from igraph import *
import pandas as pd
# g = load("repliedto_subgraph.gml")
g = Graph.Read_Pickle("graph_pickles/arabic_repliedto_graph")
df = pd.read_pickle("topic_sentiment_pickles/arabic_replies")
def addVertices(df , color):
    edgelist = []
    edgelabels_topic = []
    edgelabels_sentiment = []
    edgelabels_type = []
    e_start = g.ecount()
    for index,row in df.head(len(df)).iterrows():
        if(len(g.vs) == 0): # condition to prevent next condition from throwing exception if vs is empty
            g.add_vertex(str(row["Document_No"]) + "r")
        elif(len(g.vs.select(name_eq = str(row["Document_No"]) + "r")) == 0): # i.e: if no vertex with same name exists
            g.add_vertex(str(row["Document_No"]) + "r") 
        g.vs[g.vs.select(name_eq = str(row["Document_No"]) + "r")[0].index]["color"] = color
        last_v_index = g.vs.select(name_eq = str(row["Document_No"]) + "r")[0].index # df node index whether or not it was newly created
        repliedto_index = g.vs.select(name_eq = str(row["Document_No"]))[0].index
        # g.add_edges([(last_v_index, repliedto_index)])
        edgelabels_sentiment.append("reply")
        edgelabels_topic.append("reply")
        edgelabels_type.append("reply")
        edgelist.append((last_v_index, repliedto_index))
    g.add_edges(edgelist)
    e_end = g.ecount()
    g.es[e_start: e_end]["type"] = edgelabels_type
    g.es[e_start: e_end]["topic"] = edgelabels_topic
    g.es[e_start: e_end]["sentiment"] = edgelabels_sentiment

addVertices(df,"red")
layout = g.layout("kk")
plot(g, layout=layout, vertex_size = 15)
print(len(g.vs))
g.write_pickle("graph_pickles/arabic_replies_graph")
