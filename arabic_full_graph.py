from igraph import *
import pandas as pd

g = Graph.Read_Pickle("graph_pickles/arabic_tweets_graph")

neu0_df = pd.read_pickle("arabic_topic_dfs/america_df")
neu1_df = pd.read_pickle("arabic_topic_dfs/return_df")
neu2_df = pd.read_pickle("arabic_topic_dfs/arab_df")
neu3_df = pd.read_pickle("arabic_topic_dfs/violence_df")
neu4_df = pd.read_pickle("arabic_topic_dfs/religion_df")
neu5_df = pd.read_pickle("arabic_topic_dfs/zein_df")
neu6_df = pd.read_pickle("arabic_topic_dfs/zionism_df")
neu7_df = pd.read_pickle("arabic_topic_dfs/children_df")
neu8_df = pd.read_pickle("arabic_topic_dfs/other_df")

neu0_vs = []
neu1_vs = []
neu2_vs = []
neu3_vs = []
neu4_vs = []
neu5_vs = []
neu6_vs = []
neu7_vs = []
neu8_vs = []

pos0_vs = []
pos1_vs = []
pos2_vs = []
pos3_vs = []
pos4_vs = []
pos5_vs = []
pos6_vs = []
pos7_vs = []
pos8_vs = []

neg0_vs = []
neg1_vs = []
neg2_vs = []
neg3_vs = []
neg4_vs = []
neg5_vs = []
neg6_vs = []
neg7_vs = []
neg8_vs = []
def addVertices(df , vertex_array, color, topic):
    edgelist = []
    edgelabels_topic = []
    # edgelabels_sentiment = []
    edgelabels_type = []
    e_start = g.ecount()
    g.add_vertex(topic)
    for index,row in df.head(len(df)).iterrows():
        if(row["type"] == "repliedto"):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0])[0].index # df node index whether or not it was newly created
        elif(row["type"] == "reply"):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0] + "r")[0].index # df node index whether or not it was newly created
        elif(row["type" == "tweet"]):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0] + "t")[0].index # df node index whether or not it was newly created
        g.vs[last_v_index]["topic"] = topic
        v = g.vs.select(name_eq = topic)[0]
        # edgelabels_sentiment.append(sentiment)
        edgelabels_topic.append(topic)
        edgelabels_type.append("comm")
        edgelist.append((last_v_index, v.index))
    g.add_edges(edgelist)
    e_end = g.ecount()
    g.es[e_start: e_end]["type"] = edgelabels_type
    g.es[e_start: e_end]["topic"] = edgelabels_topic
    # g.es[e_start: e_end]["sentiment"] = edgelabels_sentiment

addVertices(neu0_df,neu0_vs ,"plum", "america")
addVertices(neu1_df,neu1_vs, "plum", "return")
addVertices(neu2_df,neu2_vs,"plum", "arabs")
addVertices(neu3_df,neu3_vs, "plum", "violence")
addVertices(neu4_df,neu4_vs, "plum", "religion")
addVertices(neu5_df,neu5_vs ,"plum", "zein")
addVertices(neu6_df,neu6_vs, "plum", "zionism")
addVertices(neu7_df,neu7_vs,"plum", "children")
addVertices(neu8_df,neu8_vs, "plum", "other")

g.save("full_graph_arabic/arabic_full.graphml")
