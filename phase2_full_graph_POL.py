from igraph import *
import pandas as pd
# g = load("reply_network_subgraph.graphml")
g = Graph.Read_Pickle("graph_pickles/phase2_tweets_graph")
# g = Graph()
# g.add_vertex("1.0")
# g.add_vertex("2.0")
# g.vs[g.vs.find(name_eq = "2.0").index]["color"] = "purple"

neu0_df = pd.read_pickle("topic_sentiment_dfs/neu0_phase2")
neu1_df = pd.read_pickle("topic_sentiment_dfs/neu1_phase2")
neu2_df = pd.read_pickle("topic_sentiment_dfs/neu2_phase2")
neu3_df = pd.read_pickle("topic_sentiment_dfs/neu3_phase2")
neu4_df = pd.read_pickle("topic_sentiment_dfs/neu4_phase2")
neu5_df = pd.read_pickle("topic_sentiment_dfs/neu5_phase2")
neu6_df = pd.read_pickle("topic_sentiment_dfs/neu6_phase2")
neu7_df = pd.read_pickle("topic_sentiment_dfs/neu7_phase2")
neu8_df = pd.read_pickle("topic_sentiment_dfs/neu8_phase2")
neu9_df = pd.read_pickle("topic_sentiment_dfs/neu9_phase2")

pos0_df = pd.read_pickle("topic_sentiment_dfs/pos0_phase2")
pos1_df = pd.read_pickle("topic_sentiment_dfs/pos1_phase2")
pos2_df = pd.read_pickle("topic_sentiment_dfs/pos2_phase2")
pos3_df = pd.read_pickle("topic_sentiment_dfs/pos3_phase2")
pos4_df = pd.read_pickle("topic_sentiment_dfs/pos4_phase2")
pos5_df = pd.read_pickle("topic_sentiment_dfs/pos5_phase2")
pos6_df = pd.read_pickle("topic_sentiment_dfs/pos6_phase2")
pos7_df = pd.read_pickle("topic_sentiment_dfs/pos7_phase2")
pos8_df = pd.read_pickle("topic_sentiment_dfs/pos8_phase2")
pos9_df = pd.read_pickle("topic_sentiment_dfs/pos9_phase2")

neg0_df = pd.read_pickle("topic_sentiment_dfs/neg0_phase2")
neg1_df = pd.read_pickle("topic_sentiment_dfs/neg1_phase2")
neg2_df = pd.read_pickle("topic_sentiment_dfs/neg2_phase2")
neg3_df = pd.read_pickle("topic_sentiment_dfs/neg3_phase2")
neg4_df = pd.read_pickle("topic_sentiment_dfs/neg4_phase2")
neg5_df = pd.read_pickle("topic_sentiment_dfs/neg5_phase2")
neg6_df = pd.read_pickle("topic_sentiment_dfs/neg6_phase2")
neg7_df = pd.read_pickle("topic_sentiment_dfs/neg7_phase2")
neg8_df = pd.read_pickle("topic_sentiment_dfs/neg8_phase2")
neg9_df = pd.read_pickle("topic_sentiment_dfs/neg9_phase2")

neu0_vs = []
neu1_vs = []
neu2_vs = []
neu3_vs = []
neu4_vs = []
neu5_vs = []
neu6_vs = []
neu7_vs = []
neu8_vs = []
neu9_vs = []

pos0_vs = []
pos1_vs = []
pos2_vs = []
pos3_vs = []
pos4_vs = []
pos5_vs = []
pos6_vs = []
pos7_vs = []
pos8_vs = []
pos9_vs = []

neg0_vs = []
neg1_vs = []
neg2_vs = []
neg3_vs = []
neg4_vs = []
neg5_vs = []
neg6_vs = []
neg7_vs = []
neg8_vs = []
neg9_vs = []
def addVertices(df , vertex_array, color, topic, sentiment, polar):
    edgelist = []
    edgelabels_topic = []
    edgelabels_sentiment = []
    edgelabels_type = []
    e_start = g.ecount()
    # g.add_vertex(topic + sentiment)
    if(len(g.vs.select(name_eq = polar)) == 0): #add polar vertix if none exists
        g.add_vertex(polar)
    for index,row in df.head(len(df)).iterrows():
        if(row["type"] == "repliedto"):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0])[0].index # df node index whether or not it was newly created
        elif(row["type"] == "reply"):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0] + "r")[0].index # df node index whether or not it was newly created
        elif(row["type" == "tweet"]):
            last_v_index = g.vs.select(name_eq = str(row["Document_No"]).split(".")[0] + "t")[0].index # df node index whether or not it was newly created
        g.vs[last_v_index]["polar"] = polar
        vp = g.vs.select(name_eq = polar)[0]
        edgelabels_sentiment.append(sentiment)
        edgelabels_topic.append(topic)
        edgelabels_type.append("comm")
        edgelist.append((last_v_index, vp.index))
    g.add_edges(edgelist)
    e_end = g.ecount()
    g.es[e_start: e_end]["type"] = edgelabels_type
    g.es[e_start: e_end]["topic"] = edgelabels_topic
    g.es[e_start: e_end]["sentiment"] = edgelabels_sentiment

addVertices(neu0_df,neu0_vs ,"plum", "0", "neu", "neu")
addVertices(neu1_df,neu1_vs, "plum", "1", "neu", "neu")
addVertices(neu2_df,neu2_vs, "plum", "2", "neu", "neu")
addVertices(neu3_df,neu3_vs, "plum", "3", "neu", "neu")
addVertices(neu4_df,neu4_vs, "plum", "4", "neu", "neu")
addVertices(neu5_df,neu5_vs ,"plum", "5", "neu", "neu")
addVertices(neu6_df,neu6_vs, "plum", "6", "neu", "neu")
addVertices(neu7_df,neu7_vs, "plum", "7", "neu", "neu")
addVertices(neu8_df,neu8_vs, "plum", "8", "neu", "neu")
addVertices(neu9_df,neu9_vs, "plum", "9", "neu", "neu")

addVertices(pos0_df,pos0_vs ,"purple", "0", "pos", "isr")
addVertices(pos1_df,pos1_vs, "purple", "1", "pos", "isr")
addVertices(pos2_df,pos2_vs, "purple", "2", "pos", "isr")
addVertices(pos3_df,pos3_vs, "purple", "3", "pos", "isr")
addVertices(pos4_df,pos4_vs, "purple", "4", "pos", "isr")
addVertices(pos5_df,pos5_vs ,"purple", "5", "pos", "isr")
addVertices(pos6_df,pos6_vs, "purple", "6", "pos", "isr")
addVertices(pos7_df,pos7_vs, "purple", "7", "pos", "isr")
addVertices(pos8_df,pos8_vs, "purple", "8", "pos", "isr")
addVertices(pos9_df,pos9_vs, "purple", "9", "pos", "isr")

addVertices(neg0_df,neg0_vs ,"pink", "0", "neg", "isr")
addVertices(neg1_df,neg1_vs, "pink", "1", "neg", "pal")
addVertices(neg2_df,neg2_vs, "pink", "2", "neg", "pal")
addVertices(neg3_df,neg3_vs, "pink", "3", "neg", "neu")
addVertices(neg4_df,neg4_vs, "pink", "4", "neg", "pal")
addVertices(neg5_df,neg5_vs ,"pink", "5", "neg", "neu")
addVertices(neg6_df,neg6_vs, "pink", "6", "neg", "pal")
addVertices(neg7_df,neg7_vs, "pink", "7", "neg", "pal")
addVertices(neg8_df,neg8_vs, "pink", "8", "neg", "pal")
addVertices(neg9_df,neg9_vs, "pink", "9", "neg", "pal")

g.save("full_graphs_POL/phase2_polarized_full.graphml")
