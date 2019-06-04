import matplotlib.pyplot as plt 
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS
# read the pickle we want to generate a word cloud for
df = pd.read_pickle("topic_sentiment_dfs\\pos2_phase3")
comment_words = ' '
stopwords = list(STOPWORDS) 
stopwords = stopwords + ["trump", "jerusalemembassy", "jerusalem", "embassy", "harsh", "critic", "finds","common", "trump decision"]

for val in df["Text"]:
    val = str(val)
    # removing urls
    if ("https" in val):
      val_arr = val.split("https")
      val = val_arr[0]
    if ("0" in val or "x" in val or "@" in val):
      val = ""


    # split the value 
    tokens = val.split() 

    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
        
    for words in tokens: 
        comment_words = comment_words + words + ' '

# generate word cloud
wordcloud = WordCloud(width = 800, height = 800, font_path='arial',
				background_color ='white', 
				stopwords = stopwords, 
				min_font_size = 10).generate(comment_words) 

# plot the WordCloud image					 
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud)
# plt.savefig('wordclouds/phase3/pos2.png') 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 
