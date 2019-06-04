from igraph import *
import pandas as pd
# g = load("repliedto_subgraph.gml")
g = Graph.Read_Pickle("graph_pickles/phase3_replies_graph")
df = pd.read_pickle("topic_sentiment_pickles/phase3_tweets")
def addVertices(df , color):
    for index,row in df.head(len(df)).iterrows():
        if(len(g.vs) == 0): # condition to prevent next condition from throwing exception if vs is empty
            g.add_vertex(str(row["Document_No"]) + "t")
        elif(len(g.vs.select(name_eq = str(row["Document_No"]) + "t")) == 0): # i.e: if no vertex with same name exists
            g.add_vertex(str(row["Document_No"]) + "t") 
        g.vs[g.vs.select(name_eq = str(row["Document_No"]) + "t")[0].index]["color"] = color

addVertices(df,"green")
# layout = g.layout("kk")
# plot(g, layout=layout, vertex_size = 15)
print(len(g.vs))
g.write_pickle("graph_pickles/phase3_tweets_graph")
