# twitter_polarization
This project performs topic and sentiment analysis on an arabic & english datasets from the hashtags #JerusalemEmbassy and #القدس_عاصمة_فلسطين_الابدية and then
creates graphml files that visualize the dataset and political sides it contains. The following steps are a walk-through for the mentioned process.
## English dataset
This dataset is divided into 3 phases: 
1. Phase 1: Dec 6 2017 to Jan 20 2018.
2. Phase 2: Jan 21 2018 to May 09 2018.
3. Phase 3: May 10 2018 to May 24 2018.

The English dataset can be found in *dataset/phase1* , *dataset/phase2* and *dataset/phase3*. Each phase contains 3 csv files: 1 for replies, and 1 for the tweets that are replied to, and a third for non-reply tweets. 
The following is the sequence to follow for recreating the project for the English dataset:
1. topicSentimentEnglish.py creates an LDA model and assigns each tweet a topic and adds a sentiment column. 
The resulting dataframes can be found in the folder *topic_sentiment_pickles* . 
2. topic_sentiment_dfs.ipynb is a notebook that separates all tweets that belong to the same topic with the same sentiment in a dataframe (e.g: the dataframe neg3_phase1 contains all the tweets from topic 3 with a negative sentiment in phase 1). The resulting dataframes can be found in the folder *topic_sentiment_dfs*.  
3. wordCloudGeneratorEnglish.py contains the code to generate wordclouds from the dataframes in topic_sentiment_dfs folder. The resulting wordclouds can be found in the folder *wordclouds*
4. Creating the graph files: to create the graphs for each phase the following files should be run in the order specified below (Note that phaseX means phase1 or phase2 or phase3):
   1. phaseX_repliedto_graph.py 
   2. phaseX_replies_graph.py
   3. phaseX_tweets_graph.py
   4. phaseX_full_graph_POL.py (This groups nodes according to political pole)
   
      OR
   
   4. phaseX_full_graph_TS.py (This groups nodes according to topic + sentiment)
   
 The resulting graph files can be found in *full_graphs_POL* and *full_graphs_TS* folders depending on the selected step v
 
5. To label boundary nodes and edges and get the boundary score, the following files should be run in the order specified below:
   1. phaseX_labeling_boundary_nodes.py 
   2. phaseX_labeling_boundary_edges.py
   3. phaseX_boundary_score_calculation.py
   
   The resulting files can be found in *boundary_labeled_graphs*

## Arabic dataset 
This dataset covers tweets from the phase defined above as phase 3. The Arabic dataset can be found in *dataset/arabic*
The following is the sequence to follow for recreating the project for the Arabic dataset:
1. arabic_topic_extraction.ipynb performs manual topic mapping through looking for keywords in tweets. The resulting grouping can be found in *arabic_topic_dfs* folder
2. Creating the graph files: to create the graphs for the Arabic dataset the following files should be run in the order specified below
   1. arabic_repliedto_graph.py 
   2. arabic_replies_graph.py
   3. arabic_tweets_graph.py
   4. arabic_full_graph.py
  The resulting graphs can be found in the *full_graph_arabic* folder
3. To label boundary nodes and edges and get the boundary score, the following files should be run in the order specified below:
   1. arabic_labeling_boundary_nodes.py 
   2. arabic_labeling_boundary_edges.py
   3. arabic_boundary_score_calculation.py
   
   The resulting files can be found in *boundary_labeled_graphs*
